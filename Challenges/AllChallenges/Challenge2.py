import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        try:
            self.driver.get("https://www.copart.com/")
            self.assertIn("Copart", self.driver.title)
            self.driver.find_element(By.ID,"input-search").send_keys('exotics')
            self.driver.find_element(By.XPATH, "//button[@class='btn btn-lightblue marginleft15']").click()
            # Synchronization with wait
            self.driver.implicitly_wait("10")
            wait = WebDriverWait(self.driver, 10)
            table_xpath = "//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotmake']"
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, table_xpath)))
            table_data = self.driver.find_element(By.XPATH, table_xpath)

            # Assert for the PORSCHE text from make column in result table
            assert table_data.text == "PORSCHE"
            print("\'Challenge-2\' test passed")
            #assert table_data.text == "Madhu"
            #self.assertIn("porsche", self.driver.find_element_by_link_text("porsche"))
        except AssertionError:
            raise

if __name__ == '__main__':
    unittest.main()
