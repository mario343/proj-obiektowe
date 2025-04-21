package model

type TableResponse struct {
	Table         string           `json:"table"`
	No            string           `json:"no"`
	EffectiveDate string           `json:"effectiveDate"`
	Rates         []Currency `json:"rates"`
}