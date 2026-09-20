from selenium.webdriver.common.by import By


class SignupPage:

    EMAIL = (By.ID, "signup-email")
    FULL_NAME = (By.ID, "signup-fullname")
    PHONE = (By.ID, "signup-phone")
    PASSWORD = (By.ID, "signup-password")
    CONFIRM_PASSWORD = (By.ID, "signup-confirm-password")
    REGISTER_BUTTON = (By.ID, "signup-submit-button")