package main

import (
	"nbp-proxy/controller"
	"github.com/labstack/echo/v4"
)

func main() {
	e := echo.New()
	controller.RegisterCurrencyRoutes(e)
	e.Logger.Fatal(e.Start(":8080"))
}
