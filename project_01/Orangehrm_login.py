from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

class Test_webpage1:

     driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          
     def test_get_url(self):
          #get url
          self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
          print("url collected")
          #maximize window
          self.driver.maximize_window()

     def test_login(self):
          #use try in login process
          try:
               #use wait some loading issues
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys('Admin')
               time.sleep(1)
               self.driver.find_element(By.NAME, value="password").send_keys('admin123')
               time.sleep(1)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #No such element exception from login errors
          except NoSuchElementException as selenium_error:
               print("login errors ;\n",selenium_error)

     def test_shutdown(self):
          #close window
          time.sleep(4)
          print("closed window")
          self.driver.quit()
