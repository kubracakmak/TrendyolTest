import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

class loginPage:

    def __init__(self, driver):

        if driver == "Chrome":
            self.options = Options()
            self.driver = webdriver.Chrome(options=self.options,
                                           executable_path=r"/Users/kubracakmak/Desktop/PythonTraining/chromedriver")
        elif driver == "Firefox":
            self.options = FirefoxOptions()
            self.driver = webdriver.Firefox(options=self.options,
                                            executable_path=r"/Users/kubracakmak/Desktop/PythonTraining/geckodriver")

        else:
            self.driver = webdriver.Safari()

    def test_openWebPage(self):
        self.driver.get("https://www.trendyol.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_css_selector('body > div.fancybox-overlay.fancybox-overlay-fixed > div > div > a').click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//li[@id='accountBtn']").click()
        time.sleep(5)

    def test_loginInfo(self):
        self.driver.find_element_by_xpath("//input[@id='email']").send_keys("kubracakmak1@hotmail.com")
        self.driver.find_element_by_xpath("//input[@id='password']").send_keys("1105011021.,")
        time.sleep(5)
        self.driver.find_element_by_xpath("//a[@id='loginSubmit']").click()
        time.sleep(5)