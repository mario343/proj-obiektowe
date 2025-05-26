import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


BASE_URL = "http://localhost:3000"


def test_login_no_credentials(driver):
    driver.get(BASE_URL)

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")
    assert login_button.is_displayed()
    assert login_button.is_enabled()

    login_button.click()
    time.sleep(1)

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_root = driver.find_element(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    toast_color = toast_root.value_of_css_property("background-color")
    assert "rgba(220, 38, 38, 1)" in toast_color

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nie udało się zalogować')]")

    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()


def test_login_fields_error_login(driver):

    username = f"user{int(time.time())}"

    driver.get(BASE_URL)
    username_input = driver.find_element(By.XPATH, "//input[@type='text']")

    assert username_input.is_displayed()

    username_input.send_keys(username)

    assert username_input.get_attribute("value") == username

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    assert login_button.is_enabled()
    login_button.click()
    time.sleep(1)
    error_message = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")
    assert error_message.is_displayed()

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nie udało się zalogować')]")

    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()
    assert toast_text_2.text == error_message.text


def test_login_fields_error_password(driver):
    password = "password123"

    driver.get(BASE_URL)
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")

    assert password_input.is_displayed()

    password_input.send_keys(password)

    assert password_input.get_attribute("value") == password

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    assert login_button.is_enabled()
    login_button.click()
    time.sleep(1)
    error_message = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")
    assert error_message.is_displayed()

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nie udało się zalogować')]")

    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()
    assert toast_text_2.text == error_message.text


def test_login_fields_error_wrong_credentials(driver):
    username = f"user{int(time.time())}"
    password = "password123"

    driver.get(BASE_URL)
    username_input = driver.find_element(By.XPATH, "//input[@type='text']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)

    assert username_input.get_attribute("value") == username
    assert password_input.get_attribute("value") == password
    assert password_input.get_attribute("type") == "password"

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    assert login_button.is_enabled()
    login_button.click()
    time.sleep(1)

    error_message = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nieprawidłowa nazwa użytkownika lub hasło')]")
    assert error_message.is_displayed()

    toast_group = driver.find_element(By.XPATH, "//div[@data-scope='toast']")
    assert toast_group.is_displayed()

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nie udało się zalogować')]")

    toast_text_2 = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Nieprawidłowa nazwa użytkownika lub hasło')]")

    assert toast_text.is_displayed()
    assert toast_text_2.is_displayed()
    assert toast_text_2.text == error_message.text


def test_login_fields_success(driver):
    username = "jest"
    password = "swietnie"

    driver.get(BASE_URL)
    username_input = driver.find_element(By.XPATH, "//input[@type='text']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")

    username_input.send_keys(username)
    password_input.send_keys(password)

    assert username_input.get_attribute("value") == username
    assert password_input.get_attribute("value") == password
    assert password_input.get_attribute("type") == "password"

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    assert login_button.is_enabled()
    login_button.click()
    time.sleep(1)

    toast_root = driver.find_element(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    toast_bg_color = toast_root.value_of_css_property("background-color")
    assert "rgba(22, 163, 74, 1)" in toast_bg_color

    toast_text = driver.find_element(
        By.XPATH, "//div[contains(text(), 'Zalogowano')]")
    assert toast_text.is_displayed()

    success_message = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Witaj')]")
    assert success_message.is_displayed()


def test_logout_button_colors(driver):
    driver.get(BASE_URL)
    time.sleep(1)

    logout_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Wyloguj')]")
    assert logout_button.is_displayed()
    assert logout_button.is_enabled()

    button_color = logout_button.value_of_css_property("color")
    bg_button_color = logout_button.value_of_css_property("background-color")
    assert "rgba(255, 255, 255, 1)" in button_color
    assert "rgba(24, 24, 27, 1)" in bg_button_color

    actions = ActionChains(driver)
    actions.move_to_element(logout_button).perform()
    time.sleep(1)

    bg_hover_button_color = logout_button.value_of_css_property(
        "background-color")

    assert "color(srgb 0.0941176 0.0941176 0.105882 / 0.9)" in bg_hover_button_color


def test_logout(driver):
    driver.get(BASE_URL)
    time.sleep(1)

    logout_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Wyloguj')]")
    assert logout_button.is_displayed()
    assert logout_button.is_enabled()

    logout_button.click()
    time.sleep(2)

    login_text = driver.find_element(
        By.XPATH, "//h2[contains(text(), 'Logowanie')]")
    assert login_text.is_displayed()
    assert login_text.text == "Logowanie"
