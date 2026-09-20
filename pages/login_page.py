from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    EMAIL = (By.ID, "signin-email")
    PASSWORD = (By.ID, "signin-password")
    LOGIN_BUTTON = (By.ID, "signin-submit-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def wait_for_login_page(self):
        self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )

    def enter_email(self, email):
        element = self.wait.until(
            EC.element_to_be_clickable(self.EMAIL)
        )
        element.clear()
        element.send_keys(email)

    def enter_password(self, password):
        element = self.wait.until(
            EC.element_to_be_clickable(self.PASSWORD)
        )
        element.clear()
        element.send_keys(password)

    def click_login(self):
        self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        ).click()

    def login(self, email, password):
        self.wait_for_login_page()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()