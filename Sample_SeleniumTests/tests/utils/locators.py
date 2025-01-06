#locator.py
from selenium.webdriver.common.by import By

class HomePageLocators:
    """Locators for elements on the Home Page"""
   
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LIST_GROUP = By.CSS_SELECTOR, "ul.list-group>li"
    BADGE= (By.CSS_SELECTOR, "span.badge")
    DROPDOWN_MENU =(By.CSS_SELECTOR, "#dropdownMenuButton")
    MENU_OPTION=(By.CSS_SELECTOR, "div.dropdown-menu>a")
    DIV4_BUTTON=(By.CSS_SELECTOR, "#test-4-div>button")
    TEST5_BUTTON=(By.CSS_SELECTOR, "#test5-button")
    ALERT=( By.CSS_SELECTOR, "#test5-alert")
    TABLE =(By.CSS_SELECTOR, ".table")
    
