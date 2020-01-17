import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver.exe")
        self.driver.get("https://www.copart.com")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        popularMakes = self.driver.find_elements(By.XPATH, "//*[@ng-if='popularSearches']//a")
        for e in popularMakes:
            print(e.text + " - " + e.get_attribute("href"))

    # While loop not required for STG certification
    #     listofelements2 = self.driver.find_elements(By.XPATH, '//*[@ng-if="popularSearches"]/../div[3]//a')
    #     count = 0
    #     while count < len(listofelements2):
    #         print (listofelements2[count].text + " : " + listofelements2[count].get_attribute("href"))
    #         count += 1


if __name__ == '__main__':
    unittest.main()
