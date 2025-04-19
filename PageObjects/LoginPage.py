# import necessary modules
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

#importing exception packages
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

#Import modules to support explicit wait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import data and locators from other packages containing Zen login page Data and Locators
from TestData.data import ZenLoginData
from TestLocators.locators import ZenLoginLocators

#Main class Login page for zen portal to perform the login and logout operations
class LoginPage:
    #create driver object
    driver=webdriver.Chrome(service= Service(ChromeDriverManager().install()))
    #create wait object for using Explicit waits
    wait= WebDriverWait(driver,10)

    #Relevant methods for Zen Login Page
    def start(self):
        self.driver.implicitly_wait(10)
        self.driver.get(ZenLoginData.zen_url)
        self.driver.maximize_window()
        return True

    #method to login using valid credentials
    def login(self):

        #using try and except block to catch exceptions
        try:
            if self.start() is True:

                #enter username
                self.wait.until(EC.presence_of_element_located((By.XPATH,ZenLoginLocators.email_locator))).send_keys(ZenLoginData.username)

                #enter password
                self.wait.until(EC.presence_of_element_located((By.XPATH,ZenLoginLocators.password_locator))).send_keys(ZenLoginData.password)

                #click submit button
                self.wait.until((EC.element_to_be_clickable((By.XPATH,ZenLoginLocators.submitbutton_locator)))).click()

            return self.driver.current_url

        except (NoSuchElementException,ElementNotVisibleException) as e:
            print("Login Unsuccessful", e)

    # method to login using invalid credentials
    def invalid_login(self):
        try:
                # enter username
                self.wait.until(EC.presence_of_element_located((By.XPATH, ZenLoginLocators.email_locator))).send_keys(
                    ZenLoginData.username)

                # enter invalid password
                self.wait.until(
                    EC.presence_of_element_located((By.XPATH, ZenLoginLocators.password_locator))).send_keys(
                    ZenLoginData.invalid_password)

                # click submit button
                self.wait.until((EC.presence_of_element_located((By.XPATH, ZenLoginLocators.submitbutton_locator)))).click()

                return self.driver.current_url

        except (NoSuchElementException, ElementNotVisibleException) as e:
            print("Login Failed", e)

    #method to check if the username box is visible
    def visible_username(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ZenLoginLocators.email_locator)))
        return True

    # method to check if the password box is visible
    def visible_password(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH, ZenLoginLocators.password_locator)))
        return True

    # method to check if the submit button is clickable
    def submit_button_clickable(self):
        self.wait.until((EC.element_to_be_clickable((By.XPATH, ZenLoginLocators.submitbutton_locator))))
        return True

    # method to check if the logout button is clickable
    def logout_button_clickable(self):
        self.wait.until(EC.presence_of_element_located((By.XPATH,ZenLoginLocators.closepopup_locator))).click()
        self.wait.until(EC.element_to_be_clickable((By.ID, ZenLoginLocators.profiledropdown_locator))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, ZenLoginLocators.logout_locator)))
        return True

    #method to logout of zen portal
    def logout(self):
        try:
            self.wait.until(EC.element_to_be_clickable((By.XPATH,ZenLoginLocators.logout_locator))).click()
            sleep(2)
            return True

        except (NoSuchElementException,ElementNotVisibleException) as e:
            print("Failed to Logout",e)

    def stop(self):
        self.driver.quit()
        return True














