package controller

import (
	"nbp-proxy/service"
	"github.com/labstack/echo/v4"
	"net/http"
)

func RegisterCurrencyRoutes(e *echo.Echo) {
	e.GET("/api/currencies/:table", getCurrencyTable)
	e.GET("/api/currency/:code", getCurrencyByCode)
}

func getCurrencyTable(c echo.Context) error {
	table := c.Param("table")
	rates, err := service.FetchNBPRatesByTable(table)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
	}
	return c.JSON(http.StatusOK, rates)
}

func getCurrencyByCode(c echo.Context) error {
	code := c.Param("code")
	table := c.QueryParam("table")
	if table == "" {
		table = "A"
	}
	rate, err := service.FetchSingleCurrencyRate(table, code)
	if err != nil {
		return c.JSON(http.StatusInternalServerError, map[string]string{"error": err.Error()})
	}
	return c.JSON(http.StatusOK, rate)
}