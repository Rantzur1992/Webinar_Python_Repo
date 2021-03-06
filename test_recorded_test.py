from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.testproject.classes import DriverStepSettings, StepSettings
from src.testproject.decorator import report_assertion_errors
from src.testproject.enums import SleepTimingType
from src.testproject.sdk.drivers import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


"""
This pytest test was automatically generated by TestProject
    Project: My first Project
    Package: TestProject.Generated.Tests.MyFirstProject
    Test: Recorded Test
    Generated by: Ran Tzur (ran.tzur+webinar@testproject.io)
    Generated on 02/26/2021, 12:15:11
"""


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(
                              project_name="My first Project",
                              job_name="Generated Python code",
                              chrome_options=options)
    step_settings = StepSettings(timeout=15000,
                                 sleep_time=500,
                                 sleep_timing_type=SleepTimingType.Before)
    with DriverStepSettings(driver, step_settings):
        yield driver
    driver.quit()


@report_assertion_errors
def test_main(driver):
    reporter = driver.report()
    reporter.disable_auto_test_reports(disabled=True)
    reporter.disable_command_reports(disabled=True)
    # Test Parameters
    # Auto generated application URL parameter
    ApplicationURL = "https://example.testproject.io/web/"

    # 1. "f'Navigate to \\'{ApplicationURL}\\''"
    # "Navigates the specified URL (Auto-generated)"
    driver.get(f'{ApplicationURL}')

    # 2. "Click 'Enter your full name'"
    enter_your_full_name = driver.find_element(By.CSS_SELECTOR,
                                               "#name")
    enter_your_full_name.click()

    # 3. "Type 'Ran Tzur' in 'Enter your full name'"
    enter_your_full_name = driver.find_element(By.CSS_SELECTOR,
                                               "#name")
    enter_your_full_name.send_keys("Ran Tzur")

    # 4. "Click 'Enter your password'"
    enter_your_password = driver.find_element(By.CSS_SELECTOR,
                                              "#password")
    enter_your_password.click()

    # 5. "Type '12345' in 'Enter your password'"
    enter_your_password = driver.find_element(By.CSS_SELECTOR,
                                              "#password")
    enter_your_password.send_keys("12345")

    # 6. "Click 'Login1'"
    login1 = driver.find_element(By.CSS_SELECTOR,
                                 "#login")
    login1.click()
    reporter.disable_command_reports(disabled=False)

    # 7. "Click 'country'"
    country = driver.find_element(By.CSS_SELECTOR,
                                  "#country")
    country.click()

    # 8. "Select the 'CG' option in 'country'"
    country = driver.find_element(By.CSS_SELECTOR,
                                  "#country")
    Select(country).select_by_value("CG")

    # 9. "Click 'country'"
    country = driver.find_element(By.CSS_SELECTOR,
                                  "#country")
    country.click()

    # 10. "Click 'Enter your address'"
    enter_your_address = driver.find_element(By.CSS_SELECTOR,
                                             "#address")
    enter_your_address.click()

    # 11. "Type 'Test Address' in 'Enter your address'"
    enter_your_address = driver.find_element(By.CSS_SELECTOR,
                                             "#address")
    enter_your_address.send_keys("Test Address")

    # 12. "Click 'Enter your email'"
    enter_your_email = driver.find_element(By.CSS_SELECTOR,
                                           "#email")
    enter_your_email.click()

    # 13. "Type 'test@test.io' in 'Enter your email'"
    enter_your_email = driver.find_element(By.CSS_SELECTOR,
                                           "#email")
    enter_your_email.send_keys("test@test.io")

    # 14. "Click 'Enter your phone number'"
    enter_your_phone_number = driver.find_element(By.CSS_SELECTOR,
                                                  "#phone")
    enter_your_phone_number.click()

    # 15. "Type '1234567' in 'Enter your phone number'"
    enter_your_phone_number = driver.find_element(By.CSS_SELECTOR,
                                                  "#phone")
    enter_your_phone_number.send_keys("1234567")

    # 16. "Click 'Save1'"
    save1 = driver.find_element(By.CSS_SELECTOR,
                                "#save")
    save1.click()

    # 17. "Get text from 'Logout1'"
    logout1 = driver.find_element(By.CSS_SELECTOR,
                                  "#logout")
    step_output = logout1.text
    assert step_output == "Logout"

    # 18. "Click 'Logout1'"
    logout1 = driver.find_element(By.CSS_SELECTOR,
                                  "#logout")
    logout1.click()
    reporter.step(description="Final Step", message="This is the final step to execute", passed=True, screenshot=True)
    reporter.test(name="My Own Report", passed=True)
