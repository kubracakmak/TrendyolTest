import requests
import unittest
import base64
from requests.exceptions import InvalidSchema, MissingSchema
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .Login import loginPage
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class tabControl(unittest.TestCase) :

    def __init__(self,driver):
        loginPage.__init__(self,driver)


    def test_ImageControl(self,image):

        try:
            current_link = image.get_attribute("src")

            if 'https://' in current_link:
                r = requests.get(current_link)
                if not (r.status_code // 100) == 2:
                    return False
                else:
                    return True


        except requests.exceptions.RequestException as e:
            print(format(current_link, e))
            return True

    def test_ImageResult(self,all_images):
        for image in all_images:
            if not self.test_ImageControl(image):
                print("problem")
        print("no problem")


    def test_Kadin(self):
       print("Kadın tab loads")
       self.driver.find_element_by_xpath("//a[contains(text(),'KADIN')]").click()

       all_images = self.driver.find_elements(By.TAG_NAME, 'img')
       self.test_ImageResult(all_images)

    def test_Erkek(self):
        print("Erkek tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'ERKEK')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

    def test_Cocuk(self):
        print("Çocuk tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'ÇOCUK')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

    def test_EvYasam(self):
        print("Ev & Yaşam tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'EV & YA')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

    def test_Supermarket(self):
        print("Supermarket tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'SÜPERMARKET')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

    def test_Kozmetik(self):
        print("Kozmetik tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'KOZMET')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

    def test_AyakkabiSapka(self):
        print("Ayakkabı & Çanta tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'AYAKKABI & ÇANTA')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

    def test_SaatAksesuar(self):
        print("Saat & Aksesuar tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'SAAT & AKSESUAR')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

    def test_Elektronik(self):
        print("Elektronik tab loads")
        self.driver.find_element_by_xpath("//a[contains(text(),'ELEKTRON')]").click()
        all_images = self.driver.find_elements(By.TAG_NAME, 'img')
        self.test_ImageResult(all_images)

