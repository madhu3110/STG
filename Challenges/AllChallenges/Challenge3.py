import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge3_forloop(self):
        try:
            self.driver.get("https://www.copart.com/")
            wait = WebDriverWait(self.driver, 10)
            tab_data = "//*[@ng-if='popularSearches']"
            wait.until(EC.presence_of_element_located((By.XPATH, tab_data)))
            tab_data_content = "//*[@ng-if='popularSearches']//a"
            #Looping through the table data content and priting the link text & hrefs
            for a in self.driver.find_elements(By.XPATH, tab_data_content):
                print(a.text +" - " +a.get_attribute('href'))
        except AssertionError:
            raise

if __name__ == '__main__':
    unittest.main()
