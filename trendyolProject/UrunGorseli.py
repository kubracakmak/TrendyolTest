from trendyolProject.tabCheck import *
import time
import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .tabCheck import tabControl

class UrunGorseli:

    def __init__(self,driver):

        loginPage.__init__(self, driver)

    def test_CheckImagesInButik(self):
        print("Kadın tab loadsss")
        self.driver.find_element_by_xpath("//a[contains(text(),'KADIN')]").click()
        self.driver.find_element_by_xpath("//div[3]//div[1]//div[1]//article[2]//img[1]").click()

        all_images_in_butik = self.driver.find_elements(By.CLASS_NAME, 'p-card-img')
        self.test_ImageResult(all_images_in_butik)


    def test_DetailsSepet(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//body//div[@class='boutique-detail-app-container']//div//div[2]//a[1]//div[1]//img[1]").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='add-to-bs-tx']").click()