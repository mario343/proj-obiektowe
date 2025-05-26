import time
from selenium.webdriver.common.by import By


BASE_URL = "http://localhost:3000"


def test_register_no_credentials(driver):
    driver.get(BASE_URL)

    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()

    register_button.click()
    time.sleep(1)

    modal = driver.find_element(By.XPATH, "//div[@role='dialog']")
    assert modal.is_displayed()

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")

    assert register_button_modal is not None
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_root = driver.find_element(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    toast_color = toast_root.value_of_css_property("background-color")
    assert "rgba(220, 38, 38, 1)" in toast_color

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")

    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()


def test_register_username_credentials_only(driver):
    username = f"user{int(time.time())}"

    driver.get(BASE_URL)

    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()

    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    assert modal.is_displayed()

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")

    assert username_input is not None

    username_input.send_keys(username)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")

    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()

    register_button_modal.click()
    time.sleep(2)

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_root = driver.find_element(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    toast_color = toast_root.value_of_css_property("background-color")
    assert "rgba(220, 38, 38, 1)" in toast_color

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")

    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()


def test_register_password_credentials_only(driver):
    password = f"user{int(time.time())}"

    driver.get(BASE_URL)

    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()

    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    assert modal.is_displayed()

    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")

    assert password_input is not None

    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")

    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()

    register_button_modal.click()
    time.sleep(2)

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_root = driver.find_element(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    toast_color = toast_root.value_of_css_property("background-color")
    assert "rgba(220, 38, 38, 1)" in toast_color

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")

    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_short_credentials(driver):
    username = "t"
    password = "123"

    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_long_password_short_name(driver):
    username = "1"
    password = "asjdhjksahdklhaskjdhasjkhdkjsahdkjashkdhaskjhdkjashdkjashdkhsajdsadasdas"
    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_short_password_long_name(driver):
    username = "1dsadsadsasadasdsadasdasdsadsadasdsadasdsadas"
    password = "1234"
    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_good_password_long_name(driver):
    username = "1dsadsadsasadasdsadasdasdsadsadasdsadasdsadas"
    password = "1234567"
    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć max. 16 znaków, a hasło max. 32')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć max. 16 znaków, a hasło max. 32')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_good_password_long_name(driver):
    username = "123456"
    password = "1dsadsadsasadasdsadasdasdsadsadasdsadasdsadas"
    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć max. 16 znaków, a hasło max. 32')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć max. 16 znaków, a hasło max. 32')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_long_credentials(driver):
    username = "asjdhjksahdklhaskjdhasjkhdkjsahdkjashkdhaskjhdkjashdkjashdkhsaj"
    password = "asjdhjksahdklhaskjdhasjkhdkjsahdkjashkdhaskjhdkjashdkjashdkhsajdsadasdas"
    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć max. 16 znaków, a hasło max. 32')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć max. 16 znaków, a hasło max. 32')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_short_password_good_username(driver):
    username = "KSAUBN 1jdadasdnmv"
    password = "123"

    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_good_password_short_username(driver):
    username = "1"
    password = "KSAUBN 1jdadasdnmv"

    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()
    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika musi mieć min. 3 znaki, a hasło min. 6')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text


def test_register_good_credentials(driver):
    username = f"user{int(time.time())}"
    password = "GdzieSaTeZnaki?"
    driver.get(BASE_URL)

    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None
    username_input.send_keys(username)
    password_input.send_keys(password)

    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")
    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()
    register_button_modal.click()

    time.sleep(2)
    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Rejestracja zakończona')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Zarejestrowano pomyślnie')]")
    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    toast_root = driver.find_element(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    toast_color = toast_root.value_of_css_property("background-color")
    assert "rgba(255, 255, 255, 1)" in toast_color


def test_register_already_registered_user(driver):
    username = "jest"
    password = "swietnie"
    driver.get(BASE_URL)

    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")

    assert register_button.is_displayed()
    assert register_button.is_enabled()

    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")

    assert username_input is not None
    assert password_input is not None

    username_input.send_keys(username)
    password_input.send_keys(password)
    register_button_modal = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj użytkownika')]")

    assert register_button_modal.is_displayed()
    assert register_button_modal.is_enabled()

    register_button_modal.click()
    time.sleep(2)

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")

    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Błąd rejestracji')]")
    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Użytkownik już istnieje')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()

    error_text = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Użytkownik już istnieje')]")

    assert error_text.is_displayed()
    assert error_text.text == toast_text_2.text
