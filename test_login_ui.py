import allure
from utils.driver_factory import get_driver
from pages.login_page import LoginPage

@allure.feature("UI Login")
def test_valid_login():
    driver = get_driver()
    driver.get("https://example.com")
    login = LoginPage(driver)
    login.login("admin", "password")
    driver.quit()