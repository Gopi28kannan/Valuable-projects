from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import time
import pytest

class Test_webpage:
     
     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
     emp_id = "1234"

     def test_get_url(self):
          self.driver.maximize_window()
          self.driver.get(self.url)
          print("url collected")

     def test_login(self):
          #login orangehrm
          try:
               #wait for visibile input box
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys('Admin')
               time.sleep(2)
               self.driver.find_element(By.NAME, value="password").send_keys('admin123')
               time.sleep(2)
               self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
               print("logged in successfully")
          #no such element exception from login errors
          except NoSuchElementException as selenium_error:
               print("login errors ;\n",selenium_error)

     def test_search_employee(self):
          #search employee in employee list
          try:
               print("use employee id and name to search")
               #wait for visible in show pim
               wait = WebDriverWait(self.driver, 20)
               wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'))).click()
               time.sleep(2)
               #enter search for name
               self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys("Gopi Kannan")               
               #enter search fo remployee id
               self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input').send_keys(self.emp_id)
               #click to search
               self.driver.find_element(By.XPATH,'//button[2]').click()
               print("employee details collected")
          #no such element exception from  search employee
          except NoSuchElementException as selenium_error:
               print("search_employee :\n",selenium_error)

     def test_delete_employee(self):
          #delete for employee
          try:
               print("collect employee details for delete")
               #move for searched employee list
               action = ActionChains(self.driver)
               time.sleep(3)
               #select for employee list
               click_employee = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div')
               action.move_to_element(click_employee).perform()
               time.sleep(2)
               #click delete button
               self.driver.find_element(By.XPATH,'//div//div//div//div//div//div//div//div//div[2]//button[1]').click()
               time.sleep(2)
               #confirm to yes delete for employee
               self.driver.find_element(By.XPATH,'//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]').click()
               print("employee successfully deleted")
               print("deleted employee")
          #no such element exception from delete employee
          except NoSuchElementException as selenium_error:
               print("delete_employee : \n",selenium_error)

     def test_shutdown(self):
          time.sleep(10)
          print("window closed")
          self.driver.quit()
