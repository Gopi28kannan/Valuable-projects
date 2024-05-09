from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Data import data
from Locators import locator
import time
import pytest

class Test_orangehrm:

    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_1_get_url(self):
        self.driver.get(data.web_data().url)
        time.sleep(2)
        self.driver.maximize_window()

    def test_2_forget_password(self):
        wait = WebDriverWait(self.driver, 20)
        try:
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator.web_locators().c_forget))).click()
            time.sleep(2)
            self.driver.find_element(By.NAME, locator.web_locators().c_username1).send_keys(data.web_data().username)
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR,locator.web_locators().c_submit).click()
            print("forget password and reset password link, successfully completed")
            time.sleep(5)
            #back the webpage two times and show login page 
            self.driver.back()
            time.sleep(2)
            self.driver.back()
            time.sleep(3)

        except NoSuchElementException as error:
            print("forget password error :",error)

    def test_3_login(self):
        # still wait upto 20 seconds
        wait = WebDriverWait(self.driver, 20)
        #try method use login process
        try:
            #still wait visibility of element located
            wait.until(EC.visibility_of_element_located((By.XPATH, locator.web_locators().c_username))).send_keys(data.web_data().username)
            self.driver.find_element(By.XPATH, locator.web_locators().c_password).send_keys(data.web_data().password)
            time.sleep(2)
            self.driver.find_element(By.CSS_SELECTOR, locator.web_locators().c_submit).click()
            print("logged in successfully")
        #no such element exception from login errors
        except NoSuchElementException as selenium_error:
               print("login errors ;\n",selenium_error)

    def test_4_validate_title_adminpage(self):
        wait = WebDriverWait(self.driver, 20)
        #validate admin page title and validate admin page options and display output console
        try:
             wait.until(EC.visibility_of_element_located((By.XPATH,locator.web_locators().c_admin))).click()
             time.sleep(3)
             #print admin page title in output console
             print("Admin page title : ",self.driver.title)
             assert self.driver.title == 'OrangeHRM'
        except NoSuchElementExcetion as error:
             print('validate_admin_page_title',error)

    def test_5_validate_options_adminpage(self):
        wait = WebDriverWait(self.driver, 20)
        try:
             #go to admin
             wait.until(EC.visibility_of_element_located((By.XPATH,locator.web_locators().c_admin))).click()
             time.sleep(3)
             #collect admin page options use via xpath
             Admin_validate=self.driver.find_elements(By.XPATH, locator.web_locators().c_admin_options)
             admin_xpath_count = len(Admin_validate)
             time.sleep(3)
             #suppose visible more option at display, in header list last.  And then first click more option and  count elements 
             more_option_xpath = self.driver.find_elements(By.XPATH, locator.web_locators().c_admin_option_more)
             more_count = len(more_option_xpath)
             if more_count == 1:
                  for element in more_option_xpath:
                       element.click()
                       time.sleep(1)
                       visible_more_options = self.driver.find_elements(By.XPATH, locator.web_locators().c_admin_more_option_visible)
                       visible_more1_options = len(visible_more_options)
             else:
                  visible_more1_options = 0
             print("\nvalidate the options are displaying on this Admin page :")
             count=1
             #use loop highlight and move header admin page options one by one, and print options in output console
             for element in Admin_validate:
                  highlight = ActionChains(self.driver)
                  highlight.move_to_element(element).perform()
                  if visible_more1_options == 0: 
                       print(element.text)
                       time.sleep(1)
                  else:
                       if admin_xpath_count != count:
                            print(element.text)
                            time.sleep(1)
                            #click more option
                       if  admin_xpath_count == count:
                            element.click()
                            time.sleep(2)
                  count=count+1
             #suppose more options display in admin page options at last, already click more option and visible next elements
             #suppose more option not display in admin page options at last, just skip this loop lines automatically
             if more_count == 1:
                  for element in visible_more_options:
                       highlight = ActionChains(self.driver)
                       highlight.move_to_element(element).perform()
                       print(element.text)
                       time.sleep(1)
        #No such element exception from validate_admin_page
        except NosuchElementException as error:
            print("validate_admin_page errors : \n",error)

    def test_6_menu_validate(self):
        #catch menu list and validate of display menu names in output console
        try:
            self.driver.implicitly_wait(10)
            menu_list = self.driver.find_elements(By.XPATH,locator.web_locators().menu_list)
            print("\nvalidate the menu options : ")
            count = 1
            #use for loop
            for element in menu_list:
            #skip claim option , and not mention this, in the project. So I use if condition
                if count !=11:
                    # highlight and move the menu names one by one
                    highlight = ActionChains(self.driver)
                    highlight.move_to_element(element).perform()    
                    print(element.text)
                    time.sleep(2)
                count=count+1
          #No such element exception error from menu_validate
        except NoSuchElementException as error:
            print("menu_validate errors ;\n", error)

    
'''web=Test_orangehrm()
web.test_1_get_url()
web.test_2_forget_password()
web.test_3_login()
web.test_4_validate_title_adminpage()
web.test_5_validate_options_adminpage()
web.test_6_menu_validate()'''
    
