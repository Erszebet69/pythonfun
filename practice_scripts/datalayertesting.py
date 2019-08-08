from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os


def chromeDriver():
    if os.path.exists('.env'):
        for line in open('.env'):
            var = line.strip().split('=')
            if len(var) == 2:
                os.environ[var[0]] = var[1]

    # Enable JS console Output in terminal
    settingsDict = DesiredCapabilities.CHROME
    settingsDict['loggingPrefs'] = {'browser': 'ALL'}

    # Add dtm debug and omnibug
    chrome_options = Options()
    chrome_options.add_extension(os.environ.get('CHROME_DTM_PATH'))
    chrome_options.add_extension(os.environ.get('CHROME_OMNIBUG_PATH'))

    # Build the driver object
    driver = webdriver.Chrome(os.environ['CHROME_DRIVER_PATH'], chrome_options=chrome_options,
                              desired_capabilities=settingsDict)

    return driver

import unittest
from driver import chromeDriver

def digital_data(driver):
    """Return the javascript digitalData object"""
    return driver.execute_script(''' return digitalData; ''')

def return_satellite_var(driver, var):
    """Returns the output of _satellite.getVar()"""
    return driver.execute_script(''' return _satellite.getVar("{}"); '''.format(var))

class TestBasic(unittest.TestCase):

    def setUp(self):
        self.driver = chromeDriver()

    def test_driver(self):
        self.driver.get("https://www.ticketmaster.com")
        assert "ticket" in self.driver.current_url

    def test_page_name(self):
        self.driver.get("https://www.ticketmaster.com")
        page_name = digital_data(self.driver)['page']['pageInfo']['pageName']
        prop1 = return_satellite_var(self.driver, "page.pageInfo.pageName")
        assert page_name == "TM_US: Home"
        assert prop1 == "TM_US: Home"

    def test_search_page(self):
        search_term = "detroit red wings"
        self.driver.get("https://www.ticketmaster.com")

        # Go to homepage and perform a search
        search_box = self.driver.find_element_by_id('search_input')
        search_box.send_keys(search_term)
        search_button = self.driver.find_element_by_id('search')
        search_button.click()

        # Now on the search page
        on_site_search_term = digital_data(self.driver)['page']['pageInfo']['onsiteSearchTerm']
        evar7_prop5 = return_satellite_var(self.driver, "page.pageInfo.onsiteSearchTerm")
        assert self.driver.current_url.startswith('http://www.ticketmaster.com/search?')
        assert on_site_search_term == search_term
        assert  evar7_prop5 == search_term

    def tearDown(self):
        self.driver.close()