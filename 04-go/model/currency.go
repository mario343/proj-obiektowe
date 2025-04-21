package model

type Currency struct {
	Currency      string  `json:"currency"`
	Code          string  `json:"code"`
	Mid           float64 `json:"mid"`
	EffectiveDate string  `json:"effectiveDate"`
}
