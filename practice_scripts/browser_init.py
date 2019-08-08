from shutil import which
from selenium import webdriver
import os

FIREFOXPATH = which("firefox")
CHROMEPATH = which("chrome") or which("chromium")



def init_webdriver():
    """Simple Function to initialize and configure Webdriver
    if FIREFOXPATH != None:
        print(FIREFOXPATH)#cm
        from selenium.webdriver.firefox.options import Options
        options = Options()
        options.binary = FIREFOXPATH
        options.add_argument("-headless")
        return webdriver.Firefox(firefox_options=options, log_path="geckodriver.log")
    elif CHROMEPATH != None:

    """
    print(CHROMEPATH)#cm
    from selenium.webdriver.chrome.options import Options
    options = Options()
    options.binary_location = r'C:\Users\eli\AppData\Local\Browser_drivers\chromedriver.exe'
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_extension(r'C:\Users\eli\PycharmProjects\practice_scripts\chromeext\omnibug_packed\1.8.0_0.crx')#add omni
    options.add_extension(r'C:\Users\eli\PycharmProjects\practice_scripts\chromeext\dtm_packed\1.125_0.crx')#add dtm
    return webdriver.Chrome(options=options, service_args=['--verbose'], service_log_path="chromedriver.log")


driver = init_webdriver()
driver.get('https://duckduckgo.com')