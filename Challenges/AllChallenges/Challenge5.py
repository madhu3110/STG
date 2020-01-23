import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")

    def tearDown(self):
        self.driver.close()

    def change_ShowEntries(self, entry_value):
        select = Select(self.driver.find_element(By.NAME, "serverSideDataTable_length"))
        select.select_by_value(str(entry_value))

    def search_copart(self,search_text):
        self.driver.get("https://www.copart.com/")
        self.assertIn("Copart", self.driver.title)
        self.driver.find_element(By.ID, "input-search").send_keys(search_text)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-lightblue marginleft15']").click()
        # Synchronization with wait
        self.driver.implicitly_wait("10")

    def test_challenge5(self):
        try:
            # Search for 'Porsche'
            self.search_copart('porsche')
            # Selecting the 'Show Entries' from 20 to 100
            self.change_ShowEntries(100)
            # Verifying page is showing 100 entries
            xpath = "//div[@class='dataTables_info' and contains(text(), 'Showing 1 to 100')]"
            wait = WebDriverWait(self.driver, 10)
            wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
            model_xpath = self.driver.find_elements(By.XPATH, "//table[@id='serverSideDataTable']//span[@data-uname='lotsearchLotmodel']")

            # Fetching the Total Model list
            model_list=[]
            for i in model_xpath:
                model_list.append(i.text)

            # Extracting the Unique models from Total Model list
            unique_model_list =[]
            for a in model_list:
                if a not in unique_model_list:
                    unique_model_list.append(a)
                    print(a)
            print("list of unique models: %s" %unique_model_list)
            print("Total Unique Models: %s" %(len(unique_model_list)))

            # Switch Case for Damages
            def damage_type_1():
                return "REAR END"
            def damage_type_2():
                return "FRONT END"
            def damage_type_3():
                return "MINOR DENT/SCRATCHES"
            def damage_type_4():
                return "UNDERCARRIAGE"
            def default():
                return "MISC"

            switch_damages= {
                "type1": damage_type_1,
                "type2": damage_type_2,
                "type3": damage_type_3,
                "type4": damage_type_4,
               }

            def switch_case(damage):
                return switch_damages.get(damage, default)()

            print("Switch case of type-1 damage: %s" %(switch_case("type1")))
            print("Switch case of type-2 damage: %s" %(switch_case("type2")))
            print("Switch case for other types of damages: %s" % (switch_case("type0")))

        except AssertionError:
            raise


if __name__ == '__main__':
    unittest.main()