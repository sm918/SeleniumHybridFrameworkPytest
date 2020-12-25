import random
import string
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomer import AddCustomer
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addcustomer(self, setUp):
        self.logger.info("Test_003_AddCustomer")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.driver.maximize_window()


        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("Login successful")

        self.logger.info("starting add customer page")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddNew()

        self.logger.info("providing customer info")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setUserEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("Divya")
        self.addcust.setLastName("Khosla")
        self.addcust.setDOB("09/03/1988")
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setCompany("QABee")
        self.addcust.setGender("Female")
        self.addcust.selectVendorManager("Vendor 2")
        self.addcust.setAdminComment("this is for testing add customer module")
        self.addcust.clickOnSave()

        self.logger.info("Save customer info")

        self.logger.info("Validating the data")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("Customer test passed")
        else:
            self.driver.save_screenshot("C:\\Users\\gladi\\PycharmProjects\\SeleniumHybridFrameworkPytest\\Screenshots\\" + "test_addCustomer_scr.png")
            self.logger.info("add customer test failed")
            assert True == False

        self.driver.close()
        self.logger.info("End of add customer page")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))






