package service

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"nbp-proxy/model"
)

var httpClient = &http.Client{}

func doRequest(url string, target any) error {
	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		return err
	}

	req.Header.Set("Accept", "application/json")
	req.Header.Set("User-Agent", "NBP-Go-Client/1.0")

	resp, err := httpClient.Do(req)
	if err != nil {
		return err
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		return fmt.Errorf("NBP API returned status code %d", resp.StatusCode)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return err
	}

	return json.Unmarshal(body, target)
}

func FetchNBPRatesByTable(table string) ([]model.Currency, error) {
	url := fmt.Sprintf("https://api.nbp.pl/api/exchangerates/tables/%s/?format=json", table)

	var response []model.TableResponse
	if err := doRequest(url, &response); err != nil {
		return nil, err
	}

	if len(response) == 0 {
		return nil, fmt.Errorf("no data returned for table %s", table)
	}

	for i := range response[0].Rates {
		response[0].Rates[i].EffectiveDate = response[0].EffectiveDate
	}

	return response[0].Rates, nil
}

func FetchSingleCurrencyRate(table, code string) (*model.Currency, error) {
	url := fmt.Sprintf("https://api.nbp.pl/api/exchangerates/rates/%s/%s/?format=json", table, code)

	var result model.SingleCurrencyResponse
	if err := doRequest(url, &result); err != nil {
		return nil, err
	}

	if len(result.Rates) == 0 {
		return nil, fmt.Errorf("no rate data found for %s", code)
	}

	rate := result.Rates[0]
	return &model.Currency{
		Currency:      result.Currency,
		Code:          result.Code,
		Mid:           rate.Mid,
		EffectiveDate: rate.EffectiveDate,
	}, nil
}
