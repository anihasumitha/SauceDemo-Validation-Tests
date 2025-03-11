# import all necessary modules
from Selenium_task_10 import PythonAutomation

# test data
url = "https://www.saucedemo.com"
# create an object from the Python Automation Class
myPythonAutomation = PythonAutomation(url)

class TestPythonAutomation:

    #Test for positive homepage url
   def test_positive_homepage_url(self):
       expected_url = "https://www.saucedemo.com"
       actual_url = myPythonAutomation.fetch_homepage_url()
       assert expected_url == actual_url
       print("SUCCESS: Test Positive Homepage URL Passed")

    #Test for negative homepage url
   def test_negative_homepage_url(self):
       expected_url = "https://www.saucedmo.com"
       actual_url = myPythonAutomation.fetch_homepage_url()
       assert expected_url != actual_url
       print("SUCCESS: Test Negative Homepage URL Passed")

    #Test for positive login url
   def test_positive_login_url(self):
       expected_url = "https://www.saucedemo.com/inventory.html"
       actual_url = myPythonAutomation.fetch_login_url()
       assert expected_url == actual_url
       print("SUCCESS: Test Positive Login URL Passed")

    #Test for negative login url
   def test_negative_login_url(self):
       expected_url = "https://www.saucedemo.com"
       actual_url = myPythonAutomation.fetch_login_url()
       assert expected_url != actual_url
       print("SUCCESS: Test Negative Login URL Passed")

    #Test for positive homepage title
   def test_positive_title(self):
       expected_title = "Swag Labs"
       actual_title = myPythonAutomation.fetch_homepage_title()
       assert expected_title == actual_title
       print("SUCCESS: Test Positive Homepage Title Passed")

    #Test for negative homepage url
   def test_negative_title(self):
       expected_title = "GUVI"
       actual_title = myPythonAutomation.fetch_homepage_title()
       assert  expected_title != actual_title
       print("SUCCESS: Test Negative Homepage Title Passed")



