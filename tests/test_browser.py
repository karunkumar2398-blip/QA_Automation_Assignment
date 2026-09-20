import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import BASE_URL, EMAIL, PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from utils.driver_factory import create_driver
from utils.google_sheet_logger import log_result


# ============================================================
# TEST CASE 1
# Login and verify User Dashboard
# ============================================================

def test_login_and_dashboard():
    start_time = time.time()
    driver = create_driver()

    status = "FAIL"
    failure_reason = ""

    try:
        # Open homepage
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 20)

        # Click Sign In / Signup
        signin_button = wait.until(
            EC.element_to_be_clickable(
                (By.ID, "user-signin-signup")
            )
        )

        original_window = driver.current_window_handle

        signin_button.click()

        # Wait for login window
        wait.until(
            lambda d: len(d.window_handles) == 2
        )

        # Switch to login window
        for window in driver.window_handles:
            if window != original_window:
                driver.switch_to.window(window)
                break

        # Login
        login_page = LoginPage(driver)
        login_page.login(EMAIL, PASSWORD)

        # Verify dashboard
        dashboard_page = DashboardPage(driver)

        assert dashboard_page.is_dashboard_loaded(), \
            "User Dashboard did not load successfully"

        assert "app.invitationnation.in" in driver.current_url, \
            f"Unexpected dashboard URL: {driver.current_url}"

        status = "PASS"

        print("\nTEST CASE 1: PASS")

    except Exception as e:
        failure_reason = f"{type(e).__name__}: {str(e)}"

        print("\nTEST CASE 1: FAIL")
        print("Failure reason:", failure_reason)

        driver.save_screenshot(
            "test_case_1_failure.png"
        )

        raise

    finally:
        execution_time = time.time() - start_time

        print(
            f"Test Case 1 execution time: "
            f"{execution_time:.2f} seconds"
        )

        log_result(
            test_case="Test Case 1 - Login and Dashboard",
            status=status,
            execution_time=execution_time,
            failure_reason=failure_reason
        )

        driver.quit()


# ============================================================
# TEST CASE 2
# Invitations -> Commercial -> Template -> Live Demo
# Verify new window and return to original window
# ============================================================

def test_invitation_live_demo():
    start_time = time.time()
    driver = create_driver()

    status = "FAIL"
    failure_reason = ""

    try:
        wait = WebDriverWait(driver, 20)

        # ----------------------------------------------------
        # 1. Open homepage
        # ----------------------------------------------------

        driver.get(BASE_URL)

        # ----------------------------------------------------
        # 2. Click Invitations
        # ----------------------------------------------------

        invitations = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//span[normalize-space()='Invitations']"
                )
            )
        )

        invitations.click()

        time.sleep(2)

        # ----------------------------------------------------
        # 3. Open Commercial category
        # ----------------------------------------------------

        commercial_locator = (
            By.CSS_SELECTOR,
            "a.occasion-overlay[href='/invitations/commercial']"
        )

        commercial_category = wait.until(
            EC.presence_of_element_located(
                commercial_locator
            )
        )

        print("\nCommercial category found")

        driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center'
            });
            """,
            commercial_category
        )

        time.sleep(1)

        print("Opening Commercial category...")

        # JavaScript click because normal Selenium click
        # was timing out on this element
        driver.execute_script(
            "arguments[0].click();",
            commercial_category
        )

        # ----------------------------------------------------
        # 4. Find The Abstract Edge template
        # ----------------------------------------------------

        template_locator = (
            By.XPATH,
            "//h3[normalize-space()='The Abstract Edge']"
        )

        template = wait.until(
            EC.visibility_of_element_located(
                template_locator
            )
        )

        print("The Abstract Edge template found")

        # ----------------------------------------------------
        # 5. Find complete template card
        # ----------------------------------------------------

        card_locator = (
            By.XPATH,
            "//h3[normalize-space()='The Abstract Edge']"
            "/ancestor::div[contains(@class,'collection-card')][1]"
        )

        template_card = wait.until(
            EC.presence_of_element_located(
                card_locator
            )
        )

        print("Template card found")

        driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center'
            });
            """,
            template_card
        )

        time.sleep(1)

        # ----------------------------------------------------
        # 6. Click the template card
        # ----------------------------------------------------

        print("Opening The Abstract Edge...")

        driver.execute_script(
            "arguments[0].click();",
            template_card
        )

        time.sleep(2)

        # ----------------------------------------------------
        # 7. Find Live Demo button
        # ----------------------------------------------------

        live_demo_locators = [
            (
                By.CSS_SELECTOR,
                "button.demo-live-btn"
            ),
            (
                By.XPATH,
                "//button[contains(normalize-space(.),'Live Demo')]"
            ),
            (
                By.XPATH,
                "//*[contains(@class,'demo-live-btn')]"
            )
        ]

        live_demo_button = None

        for locator in live_demo_locators:

            try:
                live_demo_button = WebDriverWait(
                    driver,
                    5
                ).until(
                    EC.presence_of_element_located(locator)
                )

                if live_demo_button:
                    break

            except Exception:
                continue

        assert live_demo_button is not None, \
            "Live Demo button was not found after opening the template"

        print("Live Demo button found")

        # ----------------------------------------------------
        # 8. Scroll Live Demo into view
        # ----------------------------------------------------

        driver.execute_script(
            """
            arguments[0].scrollIntoView({
                behavior: 'instant',
                block: 'center'
            });
            """,
            live_demo_button
        )

        time.sleep(1)

        # ----------------------------------------------------
        # 9. Store original window
        # ----------------------------------------------------

        original_window = driver.current_window_handle
        original_windows = set(driver.window_handles)

        # ----------------------------------------------------
        # 10. Click Live Demo
        # ----------------------------------------------------

        print("Clicking Live Demo...")

        driver.execute_script(
            "arguments[0].click();",
            live_demo_button
        )

        # ----------------------------------------------------
        # 11. Wait for new window/tab
        # ----------------------------------------------------

        wait.until(
            lambda d:
            len(d.window_handles) > len(original_windows)
        )

        new_windows = (
            set(driver.window_handles)
            - original_windows
        )

        assert new_windows, \
            "Live Demo did not open a new window"

        new_window = new_windows.pop()

        # Switch to new window
        driver.switch_to.window(new_window)

        print("Live Demo window opened")
        print("Live Demo URL:", driver.current_url)
        print("Live Demo title:", driver.title)

        # ----------------------------------------------------
        # 12. Verify Live Demo page
        # ----------------------------------------------------

        wait.until(
            lambda d: d.current_url != ""
        )

        assert driver.current_url != BASE_URL, \
            "Live Demo did not navigate to a new page"

        assert driver.title.strip() != "", \
            "Live Demo page title is empty"

        print("Live Demo page verified")

        # ----------------------------------------------------
        # 13. Close Live Demo window
        # ----------------------------------------------------

        driver.close()

        print("Live Demo window closed")

        # ----------------------------------------------------
        # 14. Return to original window
        # ----------------------------------------------------

        driver.switch_to.window(original_window)

        assert driver.current_window_handle == original_window, \
            "Could not return to original window"

        print("Returned to original window")

        status = "PASS"

        print("\nTEST CASE 2: PASS")

    except Exception as e:
        failure_reason = f"{type(e).__name__}: {str(e)}"

        print("\nTEST CASE 2: FAIL")
        print("Failure reason:", failure_reason)

        driver.save_screenshot(
            "test_case_2_failure.png"
        )

        raise

    finally:
        execution_time = time.time() - start_time

        print(
            f"Test Case 2 execution time: "
            f"{execution_time:.2f} seconds"
        )

        log_result(
            test_case="Test Case 2 - Invitation Live Demo",
            status=status,
            execution_time=execution_time,
            failure_reason=failure_reason
        )

        driver.quit()