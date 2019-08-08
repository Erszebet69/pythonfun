from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


'''
debugging options : 
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--remote-debugging-port=9222")

FUCKING HEADLESS MODE WORKS LIKE SHIT WITH EXTENSIONS, DONT DO IT
#options.add_argument("--headless")
#options.headless = True
#assert options.headless  # Operating in headless mode with omnibug and dtm, with js console in terminal

'''

#set options

options = Options()
chrome_exe = r'C:\Users\eli\AppData\Local\Browser_drivers\chromedriver.exe'
#options.binary_location = r'C:\Users\eli\AppData\Local\Browser_drivers\chromedriver.exe'
options.add_argument("--no-sandbox")
options.add_argument("--remote-debugging-port=9222")

options.add_extension(r'C:\Users\eli\PycharmProjects\practice_scripts\chromeext\omnibug_packed\1.8.0_0.crx')#add omni
options.add_extension(r'C:\Users\eli\PycharmProjects\practice_scripts\chromeext\dtm_packed\1.125_0.crx')#add dtm
settingsDict = DesiredCapabilities.CHROME
settingsDict['loggingPrefs'] = {'browser': 'ALL'}
driver = webdriver.Chrome(executable_path=chrome_exe, options=options, desired_capabilities=settingsDict)

driver.get('https://duckduckgo.com')
