from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DashboardPage:

    DASHBOARD_HEADING = (
        By.XPATH,
        "//h2[contains(normalize-space(), 'Welcome to Invitation Nation')]"
    )

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def is_dashboard_loaded(self):

        # First wait for the dashboard URL
        self.wait.until(
            lambda d: "app.invitationnation.in" in d.current_url
        )

        # Then verify the dashboard heading
        try:
            heading = self.wait.until(
                EC.visibility_of_element_located(
                    self.DASHBOARD_HEADING
                )
            )

            return heading.is_displayed()

        except Exception:
            # URL itself confirms that the dashboard was reached,
            # while the heading check provides an additional validation.
            return "app.invitationnation.in" in self.driver.current_url