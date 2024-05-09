from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import wget
import os
from locators import locate
import pytest


class Test_webpage:
    driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    def pytest_configure(config):
        config._metadata = None

    #send web url from webage
    def test_get_url(self):
        self.driver.get(locate.web_locate().url)
        time.sleep(2)
        self.driver.maximize_window()

    #downlaod monthly progress reports and save the reports in pdf_file folder
    def test_download_reports(self):
        wait=WebDriverWait(self.driver,20)
        try:
            doc=wait.until(EC.visibility_of_element_located((By.LINK_TEXT, locate.web_locate().document)))
            action=ActionChains(self.driver)
            action.move_to_element(doc).perform()
            time.sleep(2)
            self.driver.find_element(By.LINK_TEXT,locate.web_locate().monthly_progress_report).click()
            time.sleep(2)
            try:
                path='E:/disk_e/guvi/project_03/result/pdf_file'
                os.mkdir(path)
                print(path,'new folder created')
            except:
                print(path,'folder already created')
            self.driver.get_screenshot_as_file('pdf_file/selenium-get-screenshot-as-file.png')
            pdfs=self.driver.find_elements(By.CSS_SELECTOR, locate.web_locate().reports)
            count=0
            for i in pdfs:
                if count<3:
                    link=i.get_attribute('href')
                    wget.download(link,out=path)
                    print('pdf',count+1,'is downloaded')
                    i.click()
                    time.sleep(1)
                    alert = Alert(self.driver)
                    alert.accept()
                    self.driver.switch_to.window(self.driver.window_handles[1])
                    time.sleep(3)
                    self.driver.close()
                else:
                    break
                self.driver.switch_to.window(self.driver.window_handles[0])
                time.sleep(1)
                count +=1
                
        except NoSuchElementException as selenium_error:
            print('download reports error :\n',selenium_error)
    
    #downlaod images and save the images in images folder
    def test_download_images(self): 
        try:
            wait=WebDriverWait(self.driver,20)
            try:
                path = 'E:/disk_e/guvi/project_03/result/images'
                os.mkdir(path)
                print(path,'new folder created')
            except:
                print(path,'folder already created')
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, locate.web_locate().media))).click()
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, locate.web_locate().click_more))).click()
            time.sleep(2)
            self.driver.find_element(By.LINK_TEXT, locate.web_locate().photo_gallery).click()
            time.sleep(2)
            self.driver.switch_to.window(self.driver.window_handles[1])
            imgd= self.driver.find_elements(By.CSS_SELECTOR, locate.web_locate().photos)
            count=0
            for i in imgd:
                if count<10:
                    link=i.get_attribute('src')
                    wget.download(link,out=path)
                    print('image ',count+1,' is download')
                else:
                    break
                count +=1
            time.sleep(2)
            self.driver.close()
                 
        except NoSuchElementException as selenium_error:
            print('download images error : \n',selenium_error)
