from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    DASHBOARD_HEADING = (
        By.XPATH,
        "//h2[normalize-space()='Welcome to Invitation Nation']"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_dashboard_loaded(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.DASHBOARD_HEADING)
        ).is_displayed()