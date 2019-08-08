from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import re

# options and desired capabilities
options = Options()
# options.headless = True

url = 'https://comptes.entreprises.bnc.ca/business-chequing-account/start/intro/?new=true'
browserDriver = webdriver.Chrome(executable_path=r'C:\Users\eli\AppData\Local\Browser_drivers\chromedriver.exe', options=options)
settingsDict = DesiredCapabilities.CHROME



print("-" * 50)
print('Starting Form Filler 2000')
print('Opening browser')
driver = browserDriver
driver.get(url)
#if driver.find_element_by_class_name('form'):
formFields = driver.find_elements(By.XPATH, '//input[not(contains(@type, "hidden"))]')
formSelects = driver.find_elements(By.XPATH, '//select[not(contains(@class, "hide"))]')
formRadios = driver.find_elements(By.XPATH, '//div[contains(@class, "checkbox")]/label')

#first page

for fields in formFields:
    if fields.get_attribute('id') == 'perso_phone':
        fields.send_keys('555-555-5555')
    if fields.get_attribute('id') == 'perso_postalcode':
        fields.send_keys('A1A1A1')
    elif fields.get_attribute('type') == 'radio':
        fields.click()
    elif fields.get_attribute('type') == 'text':
        fields.send_keys('aaa')
    elif fields.get_attribute('type') == 'email':
        fields.send_keys('aaa@bnc.ca')
    else:
        continue

for radios in formRadios:
    radios.click()

for selects in formSelects:
    pickone = Select(selects)
    pickone.select_by_index('1')


print('QA finished')
"""
driver.close()


"""