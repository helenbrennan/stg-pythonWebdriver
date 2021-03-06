import unittest
# from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("porsche")
        searchbtn = self.driver.find_element(By.XPATH, '//*[@id="search-form"]//button')
        searchbtn.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='serverSideDataTable']")))
        dataelement = self.driver.find_element(By.XPATH, "//*[@id='serverSideDataTable']")
        text = dataelement.get_attribute("innerHTML")
        self.assertIn("PORSCHE", text)


if __name__ == '__main__':
    unittest.main()