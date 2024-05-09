from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

class Test_webpage:

     @pytest.fixture
     def booting_function(self):
          self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          yield
          self.driver.close()
     
     def test_invalid_login(self,booting_function):
          wait = WebDriverWait(self.driver, 20)
          #get url
          self.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
          time.sleep(2)
          #maximize window
          self.driver.maximize_window()
          print("url collected \n")
          wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys('Admin')
          time.sleep(1)
          self.driver.find_element(By.NAME, value="password").send_keys('invalid password')
          time.sleep(1)
          self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
          print("invalid credentials")

          print("invalid login run successfully")
                    
