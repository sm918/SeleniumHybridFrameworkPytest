import pytest
import time

from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = "C:\\Users\\gladi\\PycharmProjects\\SeleniumHybridFrameworkPytest\\TestData\\LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setUp):
        self.logger.info("********* Test_002_DDT_Login *****************")
        self.logger.info("********* Verifying Login DDT test **********")
        self.driver = setUp
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of rows in Excel:",self.rows)

        list_status = []  # Empty list variable

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path,'Sheet1',r,1)
            self.psword = XLUtils.readData(self.path, 'Sheet1',r,2)
            self.expected = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.psword)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            print(act_title)
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.expected == "Pass":
                    self.logger.info("********Passed************")
                    self.lp.clickLogout()
                    list_status.append("Pass")

                elif self.expected == "Fail":
                    self.logger.info("*******Failed*******")
                    self.lp.clickLogout()
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.expected == "Pass":
                    self.logger.info("***Failed********")
                    list_status.append("Fail")
                elif self.expected == "Fail":
                    self.logger.info("*************Passed**********")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("****Login DDT test passed*******")
            self.driver.close()
            assert True
        else:
            self.logger.info("*****Login DDT test failed**********")
            self.driver.close()
            assert False

        self.logger.info("***********End of Login DDT Test**********")
        self.logger.info("*********** Completed TC_Login_DDT_002 ***********")





