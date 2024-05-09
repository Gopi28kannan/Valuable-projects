from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest

#this code run command prompt use pytest command
class Test_webpage:
     
     driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     worker_id = "1234"
     url='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
     
     def test_get_url(self):
          self.driver.get(self.url)
          print("url collected")
          self.driver.maximize_window()
          
     def test_login(self):
          try:
               #wait for visible username box
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys('Admin')
               time.sleep(1)
               self.driver.find_element(By.NAME, value="password").send_keys('admin123')
               time.sleep(1)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #no such element exception from login errors
          except NoSuchElementException as selenium_error:
               print("login errors :\n",selenium_error)
     
     def test_add_employee(self):
          try:
               action = ActionChains(self.driver)
               wait = WebDriverWait(self.driver, 20)
               #click pim
               wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))).click()
               time.sleep(2)
               #click add employee
               wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Add Employee'))).click()
               time.sleep(2)
               #add employee details
               self.driver.find_element(By.NAME, value="firstName").send_keys('Gopi')
               self.driver.find_element(By.NAME, value="lastName").send_keys('Kannan')
               time.sleep(2)
               
               employee_id = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')
               action.move_to_element(employee_id)
               #clear default employee id and fill new employee id and use keyboard keys
               action.send_keys(Keys.TAB).pause(1).send_keys(Keys.BACKSPACE).pause(1).send_keys(self.worker_id).perform()
               time.sleep(2)
               #click save
               self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
               print("employee successfully added\n")
          #no such element exception from add employee
          except NoSuchElementException as selenium_error:
               print("add_employee errors : \n",selenium_error)
               
     def test_fill_personal_details(self):
          try:
               #next wait for visible in personal details
               wait = WebDriverWait(self.driver, 20)
               Other_id = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')))
               Other_id.send_keys('11124')
               time.sleep(2)
               Driver_license_number = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')
               Driver_license_number.send_keys('TN65AZ162')
               License_expiry_date = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
               License_expiry_date.send_keys('2023-12-22')
               ssn_number = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input')
               ssn_number.send_keys('3977 8800 0234')
               sin_number = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input')
               sin_number.send_keys('377 880 234')
               action = ActionChains(self.driver)
               
               #click nationality and select india
               nationality = self.driver.find_element(By.XPATH,'//label[text()="Nationality"]//following::div[4]')
               action.move_to_element(nationality).perform()
               time.sleep(1)
               action.send_keys_to_element(nationality,"i").pause(1).key_up(Keys.SHIFT).perform()
               action.key_down(Keys.DOWN).pause(1).perform()
               action.key_down(Keys.DOWN).perform()
               action.key_down(Keys.ENTER).perform()
               time.sleep(1)

               #click marital status and select sinle
               marital_status = self.driver.find_element(By.XPATH,'//label[text()="Marital Status"]//following::div[4]')
               action.move_to_element(marital_status).perform()
               action.send_keys_to_element(marital_status,"s").pause(2).key_down(Keys.ENTER).perform()
               time.sleep(1)
               
               date_of_birth = self.driver.find_element(By.XPATH,'//label[text()="Date of Birth"]//following::div[3]//input')
               date_of_birth.send_keys('1999-02-28')
               Gender = self.driver.find_element(By.XPATH,'//label[text()="Gender"]//following::div[5]//span').click()
               Military_service = self.driver.find_element(By.XPATH,'//label[text()="Military Service"]//following::div[1]//input')
               Military_service.send_keys("No")
               time.sleep(2)
               Save = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')
               Save.click()
               print("employee personal details sucessfully added and saved")
          #no such element exception from employee personal details
          except NoSuchElementException as selenium_error:
               print("personal details errors : \n",selenium_error)
               
     def test_shutdown(self):
          time.sleep(8)
          print("window closed")
          self.driver.quit()
