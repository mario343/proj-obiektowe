import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

BASE_URL = "http://localhost:3000"


def test_login_button_present(driver):

    time.sleep(1)
    driver.get(BASE_URL)
    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    color = login_button.value_of_css_property("color")
    bg_color = login_button.value_of_css_property("background-color")
    assert login_button.is_enabled()
    assert "rgba(255, 255, 255, 1)" in color
    assert "rgba(24, 24, 27, 1)" in bg_color
    assert login_button is not None


def test_register_button_present(driver):

    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")

    assert register_button.is_displayed()

    color = register_button.value_of_css_property("color")
    bg_color = register_button.value_of_css_property("background-color")
    assert "rgba(255, 255, 255, 1)" in color
    assert "rgba(0, 33, 90, 1)" in bg_color
    assert register_button.is_enabled()
    assert register_button is not None


def test_login_button_on_hover(driver):

    driver.get(BASE_URL)
    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    actions = ActionChains(driver)
    actions.move_to_element(login_button).perform()

    color = login_button.value_of_css_property("color")
    bg_color = login_button.value_of_css_property("background-color")
    assert "rgba(255, 255, 255, 1)" in color
    assert "color(srgb 0.0941176 0.0941176 0.105882 / 0.9)" in bg_color
    assert login_button.is_enabled()
    assert login_button is not None


def test_register_button_on_hover(driver):

    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")

    assert register_button.is_displayed()

    actions = ActionChains(driver)
    actions.move_to_element(register_button).perform()

    color = register_button.value_of_css_property("color")
    bg_color = register_button.value_of_css_property("background-color")
    assert "rgba(255, 255, 255, 1)" in color
    assert "rgba(77, 100, 140, 1)" in bg_color
    assert register_button.is_enabled()
    assert register_button is not None


def test_modal_register_button_present_on_hover(driver):

    driver.get(BASE_URL)

    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")
    assert modal is not None

    register_button_modal = modal.find_element(
        By.XPATH, ".//button[contains(text(), 'Zarejestruj użytkownika')]")

    assert register_button_modal is not None
    assert register_button_modal.is_displayed()

    actions = ActionChains(driver)
    actions.move_to_element(register_button_modal).perform()

    color = register_button_modal.value_of_css_property("color")
    bg_color = register_button_modal.value_of_css_property("background-color")
    assert "rgba(255, 255, 255, 1)" in color
    assert "color(srgb 0.0941176 0.0941176 0.105882 / 0.9)" in bg_color
    assert register_button_modal.is_enabled()
    assert register_button_modal is not None


def test_register_modal_present(driver):
    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")
    assert modal.is_displayed()

    register_text = driver.find_element(
        By.XPATH, ".//h2[contains(text(), 'Rejestracja')]")
    assert register_text.is_displayed()

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")
    assert username_input is not None
    assert password_input is not None


def test_input_focus_behavior(driver):
    driver.get(BASE_URL)

    username_input = driver.find_element(By.XPATH, "//input[@type='text']")

    username_input.click()
    time.sleep(1)

    active_elem = driver.execute_script("return document.activeElement")
    assert active_elem == username_input


def test_error_message_color(driver):
    driver.get(BASE_URL)

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    assert login_button.is_enabled()
    login_button.click()
    time.sleep(1)
    error_message = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")
    assert error_message.is_displayed()

    error_color = error_message.value_of_css_property("color")
    assert "rgba(239, 68, 68, 1)" in error_color


def test_error_dissapear_after_reload(driver):
    driver.get(BASE_URL)

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()

    assert login_button.is_enabled()
    login_button.click()
    time.sleep(1)

    error_message = driver.find_element(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]")
    assert error_message.is_displayed()

    driver.execute_script("location.reload()")
    time.sleep(1)

    error_elements = driver.find_elements(
        By.XPATH, "//p[contains(text(), 'Nazwa użytkownika i hasło nie mogą być puste')]"
    )
    assert len(error_elements) == 0


def test_login_page_title(driver):
    driver.get(BASE_URL)

    login_text = driver.find_element(
        By.XPATH, "//h2[contains(text(), 'Logowanie')]")
    assert login_text.is_displayed()
    assert login_text.text == "Logowanie"


def test_login_page_title(driver):
    driver.get(BASE_URL)

    login_text = driver.find_element(
        By.XPATH, "//h2[contains(text(), 'Logowanie')]")
    assert login_text.is_displayed()
    assert login_text.text == "Logowanie"


def test_login_fields_present(driver):

    driver.get(BASE_URL)

    login_text = driver.find_element(
        By.XPATH, "//label[contains(text(), 'Nazwa użytkownika')]")
    assert login_text.is_displayed()
    assert login_text.text == "Nazwa użytkownika*"

    password_text = driver.find_element(
        By.XPATH, "//label[contains(text(), 'Hasło')]")
    assert password_text.is_displayed()
    assert password_text.text == "Hasło*"

    username_input = driver.find_element(By.XPATH, "//input[@type='text']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")
    assert username_input is not None
    assert password_input is not None


def test_login_fields_working(driver):

    username = f"user{int(time.time())}"
    password = "password123"

    driver.get(BASE_URL)
    username_input = driver.find_element(By.XPATH, "//input[@type='text']")
    password_input = driver.find_element(By.XPATH, "//input[@type='password']")

    assert username_input.is_displayed()
    assert password_input.is_displayed()

    username_input.send_keys(username)
    password_input.send_keys(password)

    assert username_input.get_attribute("value") == username
    assert password_input.get_attribute("value") == password
    assert password_input.get_attribute("type") == "password"


def test_register_modal_inputs_working(driver):

    username = f"user{int(time.time())}"
    password = "password123"

    driver.get(BASE_URL)
    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]")
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(
        By.XPATH, "//div[@data-scope='popover' and @role='dialog']")

    username_input = modal.find_element(By.XPATH, ".//input[@type='text']")
    password_input = modal.find_element(
        By.XPATH, ".//input[@type='password']")

    assert username_input.get_attribute("type") == "text"

    username_input.send_keys(username)
    password_input.send_keys(password)

    assert username_input.get_attribute("value") == username
    assert password_input.get_attribute("value") == password
    assert password_input.get_attribute("type") == "password"


def test_register_modal_closing(driver):
    driver.get(BASE_URL)

    register_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zarejestruj się')]"
    )
    register_button.click()
    time.sleep(1)

    modal = driver.find_element(By.XPATH, "//div[@role='dialog']")
    assert modal.is_displayed()

    backdrop = driver.find_element(By.CLASS_NAME, "css-14cmakv")
    backdrop.click()
    time.sleep(1)

    assert not modal.is_displayed()


def test_toast_max_number(driver):
    driver.get(BASE_URL)

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()
    assert login_button.is_enabled()

    login_button.click()
    login_button.click()
    login_button.click()
    login_button.click()
    time.sleep(1)

    toast_group = driver.find_elements(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    assert len(toast_group) == 3


def test_toast_two_calls(driver):
    driver.get(BASE_URL)

    login_button = driver.find_element(
        By.XPATH, "//button[contains(text(), 'Zaloguj')]")

    assert login_button.is_displayed()
    assert login_button.is_enabled()

    login_button.click()
    login_button.click()

    time.sleep(1)

    toast_group = driver.find_elements(
        By.XPATH, "//div[@data-scope='toast' and @data-part='root']")

    assert len(toast_group) == 2
