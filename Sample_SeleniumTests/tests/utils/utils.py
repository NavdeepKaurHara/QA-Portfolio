# utils.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    """
    This function creates an webdriver instance
    """
    try:
        # Set up the WebDriver
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run headless Chrome
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        # Initialize the WebDriver
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        # Yield the driver instance to the test functions
        yield driver
        # Teardown code
        driver.quit()
    except Exception as e:
        return f"Error: {str(e)}"


def navigate(driver):
    """
    This function navigates to Home page.
    param driver: The WebDriver instance.
    As file URL is same for all tests that why hardcoded in function
    otherwise file_url can be a param
    """
    try:
        # Convert file path to a file URL
        file_url = r"C:\Users\User\TechnicalAssesment\QE-index.html"
        # Navigate to the home page
        driver.get(file_url)
    except Exception as e:
        return f"Error: {str(e)}"


def wait_for_element_to_be_present(driver, locator_type, locator_value, timeout):
    """
    Waits for an element to be visible on the page.
    param driver: The WebDriver instance.
    param locator_type: The type of the locator (e.g., By.CSS_SELECTOR).
    param locator_value: The value of the locator.
    param timeout: The maximum time to wait (default is 10 seconds).
    return: The WebElement if visible, otherwise raises a TimeoutException.
    """
    try:
        wait = WebDriverWait(driver, timeout)
        return wait.until(EC.presence_of_element_located((locator_type, locator_value)))
    except Exception as e:
        return f"Error: {str(e)}"


def wait_for_elements_to_be_present(driver, locator_type, locator_value, timeout):
    """
    Waits for an elements to be visible on the page.
    param driver: The WebDriver instance.
    param locator_type: The type of the locator (e.g., By.CSS_SELECTOR).
    param locator_value: The value of the locator.
    param timeout: The maximum time to wait (default is 10 seconds).
    return: The WebElements if visible, otherwise raises a TimeoutException.
    """
    try:
        wait = WebDriverWait(driver, timeout)
        return wait.until(
            EC.presence_of_all_elements_located((locator_type, locator_value))
        )
    except Exception as e:
        return f"Error: {str(e)}"


def wait_for_button_to_be_clickable(driver, locator_type, locator_value, timeout):
    """
    Waits for button to be clickable on the page.
    param driver: The WebDriver instance.
    param locator_type: The type of the locator (e.g., By.CSS_SELECTOR).
    param locator_value: The value of the locator.
    param timeout: The maximum time to wait (default is 10 seconds).
    return: The button once clickable, otherwise raises a TimeoutException.
    """
    try:
        wait = WebDriverWait(driver, timeout)

        return wait.until(EC.element_to_be_clickable((locator_type, locator_value)))
    except Exception as e:
        return f"Error: {str(e)}"


def get_table_cell_value(driver, table_locator, row_index, col_index):
    """
    Gets the value of the cell
    param driver: The WebDriver instance.
    param table_locator: The value of the locator
    param row_index: The row index of the cell.
    param col_index: The column index of the cell.
    return: The value of the cell.
    """
    try:
        # Find the table by ID
        table = driver.find_element(By.CSS_SELECTOR, table_locator)
        # Get the tbody element (to exclude header rows in thead)
        tbody = table.find_element(By.TAG_NAME, "tbody")
        rows = tbody.find_elements(By.TAG_NAME, "tr")
        # Check if row exists
        if row_index < len(rows):
            row = rows[row_index]
            cols = row.find_elements(By.TAG_NAME, "td")
            # Check if column exists
            if col_index < len(cols):
                # Return the cell value (text)
                return cols[col_index].text
            else:
                raise IndexError("Column index out of range")
        else:
            raise IndexError("Row index out of range")
    except Exception as e:
        return f"Error: {str(e)}"
