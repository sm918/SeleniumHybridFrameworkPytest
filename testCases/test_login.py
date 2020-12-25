import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setUp):

        self.logger.info("********* Test_001_Login **********")
        self.logger.info("********* Verifying Home Page Title **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********* Home Page Title test is passed **********")
        else:
            self.driver.save_screenshot("C:\\Users\\gladi\\PycharmProjects\\SeleniumHybridFrameworkPytest\\Screenshots\\" + "test_homePageTitle.png")
            self.driver.close()
            self.logger.info("********* Home Page Title test is failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setUp):
        self.logger.info("********* Verifying Login test **********")
        self.driver = setUp
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********* Login test is passed **********")
            self.driver.close()
        else:
            self.driver.save_screenshot("C:\\Users\\gladi\\PycharmProjects\\SeleniumHybridFrameworkPytest\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error("********* Login test is failed **********")
            assert False







