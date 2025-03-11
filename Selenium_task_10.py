from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# using OOPs approach, creating proper classes and methods for writing my automation scripts

class PythonAutomation:
    def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) #creating driver object from selenium webdriver

 # start method to launch automation
    def start(self):
       #Using try-except exception handling method
       try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(5)
            return True
       except:
           print("Unable to start Automation")
           return False

   # Enter login details to login to website
    def login(self):

        if self.start():
           # Find and fill the Username field
           username_input = self.driver.find_element(By.NAME, "user-name")
           username_input.send_keys("standard_user")

           # Find and fill the Password field
           password_input = self.driver.find_element(By.NAME, "password")
           password_input.send_keys("secret_sauce")

           # Login to the webpage
           password_input.send_keys(Keys.RETURN)  # Press Enter
           sleep(3)  # Wait for the page to load
           return  True

        else:
            print("Could not login")
            return False

    # Fetching Homepage Url
    def fetch_homepage_url(self):
            if self.start():  # calling start() method to start automation
                return self.driver.current_url  # returns the title
            else:
                print("Error: Unable to fetch the url!")
                return False  # returns the False
    # Fetching homepage title
    def fetch_homepage_title(self):
           if self.start():  # calling start() method to launch automation
               return self.driver.title  # returns the title of homepage
           else:
               print("Error: Unable to fetch the title!")
               return False  # returns the False

    # Fetching Login Url
    def fetch_login_url(self):
            if self.login():  # calling login() method to login to the site
                return self.driver.current_url  # returns the current url
            else:
                print("Error: Unable to fetch the url!")
                return False  # returns the False

    #Extracting contents to a txt file
    def extract_contents(self):
        #Extract contents and save it to a txt file
        webpage_task_11=self.driver.page_source
        with open ("webpage_task_11.txt","w",encoding="utf-8") as file:
            file.write(webpage_task_11)

   # Create shutdown method to close the browser instance
    def shutdown(self):
       self.driver.quit()







