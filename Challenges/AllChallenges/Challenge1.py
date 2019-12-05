import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        try:
            self.driver.get("https://www.google.com")
            self.assertIn("Google", self.driver.title)
            print("\'Challenge-2\' test passed")
        except AssertionError:
            raise


if __name__ == '__main__':
    unittest.main()

