#  Include all the common methods, variables in conftest python file
from selenium import webdriver
import pytest

@pytest.fixture()
def setUp(browser):
        if browser == 'chrome':
                driver = webdriver.Chrome(executable_path="C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
                print("Launching chrome browser")
        elif browser == 'firefox':
                driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver-v0.28.0-win64\\geckodriver.exe")
                print("Launching firefox browser")
        else:
                driver=webdriver.Ie(executable_path="C:\\Drivers\\IEDriverServer_Win32_2.39.0\\IEDriverServer.exe")
        return driver

def pytest_addoption(parser):  # This will get the value from CLI/hooks
        parser.addoption("--browser")

@pytest.fixture()
def browser(request):  # This will return the browser value to the setUp method
        return request.config.getoption("--browser")

####  Pytest HTML Report  #####

# hook for adding environment info to HTML Report
def pytest_configure(config):
        config._metadata['Project Name'] = 'Selenium Hybrid Framework'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Sam'

# hook for deleting/modifying environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)

