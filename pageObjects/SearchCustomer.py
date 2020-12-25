# Search Customer Page Object Class
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select

class SearchCustomer:
    # Search Customer Page web elements
    txtEmail_xpath = "//*[@id='SearchEmail']"
    txtFirstName_xpath = "//*[@id='SearchFirstName']"
    txtLastName_xpath = "//*[@id='SearchLastName']"
    btnSearch_xpath = "//button[@id='search-customers']"

    tblSearchResults_xpath = "//table[@role='grid']"
    table_xpath= "//table[@id='customers-grid']"
    tableRows_xpath = "//*[@id='customers-grid']/tbody/tr"
    tableColumns_xpath = "//*[@id='customers-grid']/tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).clear()
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).clear()
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_xpath(self.btnSearch_xpath).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            print(emailid)
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerbyName(self, Name):
        falg = False
        for r in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag = True
        return flag





