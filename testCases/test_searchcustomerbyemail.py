import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomer import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.AddCustomer import AddCustomer

class Test_004_SearchcustomerbyEmail:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchcustomerbyemail(self, setUp):
        self.logger.info("SearchCustomer")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successful")

        self.logger.info("Search Customer by Email")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail("james_pan@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByEmail("james_pan@nopCommerce.com")
        assert True == status

        self.logger.info("End of search customer by email test case ")
        self.driver.close()


