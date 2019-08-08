from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import scrapy


options = Options()
driver = webdriver.Chrome(executable_path=r'C:\Users\eli\AppData\Local\Browser_drivers\chromedriver.exe', options=options)
settingsDict = DesiredCapabilities.CHROME

#opening and specifying pages
driver.get('https://www.bnc.ca/particuliers/inspiration/professionnel/que-signifie-la-conciliation-travail-famille.html')

# returning spcific values from data layer
'''
data layer value = page, user, name

def datalayerscraping:
    return data layer value

pour dictionnaire, get + la valeur
'''
print(driver.execute_script("return digitalData"))
print("-" * 50)
bncDataLayer = driver.execute_script("return digitalData")
page_name = bncDataLayer.get("event")
print(page_name)
print("-" * 50)
print(driver.execute_script("return digitalData.page.pageInfo.pageName"))
print("-" * 50)
print(driver.execute_script("return digitalData.user.userInfo.language"))
driver.close()