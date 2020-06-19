import unittest
# from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class challenge5(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.send_keys("porsche")
        searchbtn = self.driver.find_element(By.XPATH, '//*[@id="search-form"]//button')
        searchbtn.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='serverSideDataTable']")))
        dataelement = self.driver.find_element(By.XPATH, "//*[@id='serverSideDataTable']")
        text = dataelement.get_attribute("innerHTML")
        self.assertIn("PORSCHE", text)

    def maxResults(self, locator, value):
        selectOption = Select(self.driver.find_element(*locator))
        option_selected = selectOption.select_by_value(value)





    rear = 0
    front = 0
    minor = 0
    misc = 0
    under = 0

    def rearEnd(self):
        self.rear = self.rear + 1
        return "rearEnd"

    def frontEnd(self):
        self.front = self.front + 1
        return "frontEnd"

    def minor(self):
        self.minor = self.minor + 1
        return "minor"

    def undercarriage(self):
        self.under = self.under + 1
        return "undercarriage"

    def default(self):
        self.misc = self.m
        return "MISC"

    switcher = {

        "REAR END": rearEnd,
        "FRONT END": frontEnd,
        "MINOR DENT/SCRATCHES": minor,
        "UNDERCARRIAGE": undercarriage,
    }


def switch(self, damage):
    return switch.get(damage, self.default)()


if __name__ == '__main__':
    unittest.main()
