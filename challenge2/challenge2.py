import unittest
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        searchterm = "exotics"
        self.driver.get("https://www.copart.com")
        searchField = self.driver.find_element(By.ID, "input-search")
        searchField.send_keys(searchterm)
        searchField.send_keys(Keys.ENTER)
        # self.driver.implicitly_wait(10)
        wait = WebDriverWait(self.driver, 10)
        # wait.until(EC.visibility_of_element_located(By.XPATH,  "//*[@id=\"serverSideDataTable\"]/tbody/tr[20]"))

        dataelement = self.driver.find_element(By.XPATH, "//*[@id=\"serverSideDataTable\"]//tbody")
        html = dataelement.get_attribute("innerHTML")
        self.assertIn("PORSCHE", html)

if __name__ == '__main__':
    unittest.main()