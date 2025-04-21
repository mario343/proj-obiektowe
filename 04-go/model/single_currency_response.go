package model

type SingleCurrencyResponse struct {
	Table    string `json:"table"`
	Currency string `json:"currency"`
	Code     string `json:"code"`
	Rates    []struct {
		No            string  `json:"no"`
		EffectiveDate string  `json:"effectiveDate"`
		Mid           float64 `json:"mid"`
	} `json:"rates"`
}