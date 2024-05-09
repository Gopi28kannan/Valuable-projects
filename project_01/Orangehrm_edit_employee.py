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

class Test_webpage:

     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
     emp_id = "1234"

     def test_get_url(self):
          self.driver.maximize_window()
          self.driver.get(self.url)
          print("url collected and open webpage")

     def test_login(self):
          #login orange hrm
          try:
               #wait for visible username box
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys('Admin')
               time.sleep(2)
               self.driver.find_element(By.NAME, value="password").send_keys('admin123')
               time.sleep(2)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #no such element exception from login errors
          except NoSuchElementException as selenium_error:
               print("login errors :\n",selenium_error)

     def test_search_employee(self):
          #search employee
          try:
               
               #wait for visible in pim
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))).click()
               time.sleep(2)
               #send employee name
               self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Gopi Kannan")               
               #send employee id
               self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys(self.emp_id)
               print("use for collected employee details and employee searching")
               #click search
               self.driver.find_element(By.XPATH,'//button[2]').click()
               print("employee details catch and searched")
          #no such element exception from search employee
          except NoSuchElementException as selenium_error:
               print("search_employee errors ;\n",selenium_error)

     def test_edit_employee(self):
          #edit employee
          try:
               print("employee is visible \nedit and update for contact details")
               #wait for visible in employee list
               wait = WebDriverWait(self.driver, 20)
               action = ActionChains(self.driver)
               time.sleep(3)
               click_edit = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]')
               action.move_to_element(click_edit).perform()
               time.sleep(2)
               #click to edit employee
               click_edit.click()
               #wait for visible contact details link
               wait.until(EC.visibility_of_element_located((By.LINK_TEXT,'Contact Details'))).click()
               time.sleep(3)
               #fill street 1
               self.driver.find_element(By.XPATH,'//label[text()="Street 1"]//following::div[1]//input').send_keys('A-12')
               #fill street 2
               self.driver.find_element(By.XPATH,'//label[text()="Street 2"]//following::div[1]//input').send_keys('Emaneswaram')
               #fill city
               self.driver.find_element(By.XPATH,'//label[text()="City"]//following::div[1]//input').send_keys('Paramakudi')
               #fill state
               self.driver.find_element(By.XPATH,'//label[text()="State/Province"]//following::div[1]//input').send_keys('Tamil Nadu')
               #fill postal code
               self.driver.find_element(By.XPATH,'//label[text()="Zip/Postal Code"]//following::div[1]//input').send_keys('623 701')
               #select nationality and click india
               nationality = self.driver.find_element(By.XPATH,'//label[text()="Country"]//following::div[4]')
               action.move_to_element(nationality).perform()
               time.sleep(1)
               action.send_keys_to_element(nationality,"i").pause(1).key_up(Keys.SHIFT).perform()
               action.key_down(Keys.DOWN).pause(1).perform()
               action.key_down(Keys.ENTER).perform()
               time.sleep(1)
               #fill mobile number
               self.driver.find_element(By.XPATH,'//label[text()="Mobile"]//following::div[1]//input').send_keys('9244186721')
               #fill gmail
               self.driver.find_element(By.XPATH,'//label[text()="Work Email"]//following::div[1]//input').send_keys('admin@gmail.com')
               time.sleep(2)
               #click to save
               self.driver.find_element(By.XPATH,'//div[4]//button').click()
               print("contact details successfully saved")
          #no such element exception from edit employee errors
          except NoSuchElementException as selenium_error:
               print("edit_employee errors :\n",selenium_error)
                  
     def test_shutdown(self):
          time.sleep(8)
          print("window closed")
          self.driver.quit()
