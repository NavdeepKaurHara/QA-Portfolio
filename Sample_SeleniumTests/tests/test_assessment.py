# test_assessment.py

from utils.locators import HomePageLocators 
from utils.utils import (
 driver,
 get_table_cell_value,
 navigate,
wait_for_element_to_be_present,
    wait_for_elements_to_be_present,
    wait_for_button_to_be_clickable,
)

def test_login(driver):
    # navigation to the Home page
    navigate(driver)
    # Assertion for Title of the page
    assert "Home" in driver.title
    # locate email field
    email = driver.find_element(*HomePageLocators.EMAIL_INPUT)
    # Assertion for email Field Presence
    assert email.is_displayed(), "Email field is not displayed"
    # locate password field
    password = driver.find_element(*HomePageLocators.PASSWORD_INPUT)
    # Assertion for password field presence
    assert password.is_displayed(), "Password field is not displayed"
    #locate sign in button
    loginButton = driver.find_element(*HomePageLocators.LOGIN_BUTTON)
    # Assertion for login/sign in button
    assert loginButton.is_displayed(), "Login button is not displayed "
    # Enter Email and Password
    email.send_keys("email@gmail.com")
    password.send_keys("password")

def test_list_group(driver):
    # navigation to Home page
    navigate(driver)
    # Waits for an element to be visible on the page
    listItems = wait_for_elements_to_be_present(
        driver, *HomePageLocators.LIST_GROUP, 10
    )
    # Assert the number of list item is as expected
    assert len(listItems) == 3, "List Items are not 3"
    secondItem = listItems[1]
    # get badge text
    badge = secondItem.find_element(*HomePageLocators.BADGE)
    # get second list item text
    secondItemText = listItems[1].text
    secondListItem = secondItemText.replace(badge.text, "").strip()
    # Assert the item text without badge is as expected
    assert secondListItem == "List Item 2", "Second Item is not List Item 2"
    # Assert the badge text  is as expected
    assert badge.text == "6", "Badge text is not 6"

def test_dropdown(driver):
    # navigate to Home page
    navigate(driver)
    # Waits for an element to be visible on the page
    dropdownMenu = wait_for_element_to_be_present(
        driver, *HomePageLocators.DROPDOWN_MENU, 10
    )
    # get default value of dropdown
    menu = dropdownMenu.text
    # Assertion for default value of dropdown
    assert menu == "Option 1", "Default value is not Option 1"
    # open the dropdown by clicking
    dropdownMenu.click()
    menuOptions = wait_for_elements_to_be_present(
        driver, *HomePageLocators.MENU_OPTION, 10
    )
    # Select "Option 3" from the list
    menuOptions[2].click()

def test_buttons(driver):
    # navigate to Home page
    navigate(driver)
    # Waits for buttons to be visible on the page
    div4Buttons = wait_for_elements_to_be_present(
        driver,*HomePageLocators.DIV4_BUTTON, 10
    )
    # Assert that first button is enabled
    assert div4Buttons[0].is_enabled() == True, "First button is not enabled"
    # Assert that second button is disabled
    assert div4Buttons[1].is_enabled() == False, "Second button is not disabled"

def test_alert(driver):
    # navigate to Home page
    navigate(driver)
    # wait for the button to be clickable
    test5Button = wait_for_button_to_be_clickable(
        driver,*HomePageLocators.TEST5_BUTTON, 10
    )
    # click the button
    test5Button.click()
    # wait for the alert 
    alert = wait_for_element_to_be_present(driver,*HomePageLocators.ALERT, 10)
    # assert that success message is displayed
    assert alert.is_displayed(), "Alert message is not displayed"
    # assert the text of the success message is as expected
    assert alert.text == "You clicked a button!", "Alert message is not as expected"
    # assert that button is disabled after the click
    assert test5Button.is_enabled() == False, "Button is not disabled after the click"

def test_cell_value(driver):
    # navigate to Home page
    navigate(driver)
    # Waits for table to be visible on the page
    wait_for_elements_to_be_present(driver, *HomePageLocators.TABLE, 10)
    # Use the method to find the value of the cell at coordinates 2, 2
    cellValue = get_table_cell_value(driver, ".table", 2, 2)
    # Assert the value of the cell is as expected
    assert cellValue == "Ventosanzap", " Cell(2,2) value is not Ventosanzap"
