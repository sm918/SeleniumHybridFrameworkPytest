# Page Object class
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add customer page elements
    # Left Panel elements
    lnkCustomers_menu_xpath = "//a[@href='#']//span[contains(text(), 'Customers')]"
    lnkCustomers_menuitem_xpath = "//span[@class='menu-item-title'][contains(text(), 'Customers')]"
    # web elements
    btnAddNew_xpath = "//a[@class='btn bg-blue']"
    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtDOB_xpath = "//input[@id='DateOfBirth']"
    txtCompany_xpath = "//input[@id='Company']"
    # chkTax_xpath = "//input[@id='IsTaxExempt']"
    # list items
    txtCustomerRoles_xpath = "//*[@id ='customer-info']/div[2]/div[1]/div[10]/div[2]/div/div[1]/div"
    lstitemAdministrators_xpath = "//li[contains(text(), 'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(), 'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(), 'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(), 'Vendors')]"
    lstitemForumModerators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    # Dropdown values
    drpdownManagerOfVendor = "//*[@id='VendorId']"
    txtareaAdminComment_xpath = "//textarea[@id='AdminComment']"
    # chkboxActive_xpath = "//input[@id='Active']"
    btnSave_xpath = "//button[@name='save-continue']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()
        print("Customers Menu clicked")

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()
        print("customers sub menu clicked")
        time.sleep(3)

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setUserEmail(self,useremail):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(useremail)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setDOB(self,dob):
        self.driver.find_element_by_xpath(self.txtDOB_xpath).send_keys(dob)

    def setCompany(self,company):
        self.driver.find_element_by_xpath(self.txtCompany_xpath).send_keys(company)
    #
    # def chkTax(self):
    #     self.driver.find_element_by_xpath(self.chkTax_xpath).click()

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Forum Moderators':
            listitem = self.driver.find_element_by_xpath(self.lstitemForumModerators_xpath)
        elif role == 'Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        listitem.click()

    def selectVendorManager(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpdownManagerOfVendor))
        drp.select_by_visible_text(value)

    # def chkActive(self):
    #     checked = self.driver.find_element_by_xpath(self.chkboxActive_xpath).click()

    def setAdminComment(self,comments):
        self.driver.find_element_by_xpath(self.txtareaAdminComment_xpath).send_keys(comments)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()