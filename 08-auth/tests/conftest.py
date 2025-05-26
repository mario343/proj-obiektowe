import pytest
import requests
from selenium import webdriver


BASE_URL = "http://localhost:3000"
API_URL = "http://localhost:8080"


@pytest.fixture(scope="session", autouse=True)
def ensure_test_user():
    url = f"{API_URL}/auth/register"

    payload = {
        "username": "jest",
        "password": "swietnie"
    }

    try:
        response = requests.post(url, json=payload)
        if response.status_code not in (200, 201, 409):  # 409 = already exists
            raise Exception(
                f"Failed to create test user: {response.status_code}")
    except Exception as e:
        print(f"[ERROR] Could not ensure test user: {e}")


@pytest.fixture(scope="module")
def driver():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
