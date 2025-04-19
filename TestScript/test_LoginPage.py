#Importing necessary modules from the PageObject and Test Data folders
import TestData.data
from PageObjects.LoginPage import LoginPage

#Test case to start automation
def test_start():
    assert LoginPage().start() == True
    print("Test Passed:Automation start successful")

#Test case to check if the username box is visible
def test_visible_username():
    assert LoginPage().visible_username() is True
    print("Test Passed: Visible username ")

#Test case to check if the password box is visible
def test_visible_password():
    assert LoginPage().visible_password() is True
    print("Test Passed: Visible Password ")

#Test case to check if the submit button is enabled
def test_submit_button_clickable():
    assert LoginPage().submit_button_clickable() is True
    print("Test Passed: Submit button Clickable")

#Test case to check if the login works
def test_login():
    assert LoginPage().login() == TestData.data.ZenLoginData.zen_url
    print("Test Passed:Login successful")

#Test case to check if the logout button is enabled
def test_logout_button_clickable():
    assert LoginPage().logout_button_clickable() is True
    print("Test Passed: Logout button Clickable")

#Test case to check if the logout works
def test_logout():
    assert LoginPage().logout() == True
    print("Test Passed:Logout successful with valid credentials")

#Test case to check if the login fails with invalid password
def test_invalid_login():
    assert LoginPage().invalid_login()== TestData.data.ZenLoginData.zen_url
    print("Test Passed:Login Unsuccessful with invalid password")

#Test case to stop automation
def test_stop():
    assert LoginPage().stop() == True
    print("Test Passed: Automation stopped")



