from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request

testPages = ['https://www.bnc.ca/entreprises.html', 'https://www.nbc.ca/business.html']
CAOlinkFR = 'https://comptes.entreprises.bnc.ca/start/?questionId_appt_ch=14&questionId_canal=BNC.CA&customType=ENTR&productId=CC-ENT-CA&packageId=&conditionId=&language=FR&exitUrl=entreprises/solutions-bancaires/comptes-forfaits/ouverture.html'
LandinglinkFR = 'https://www.bnc.ca/entreprises/solutions-bancaires/comptes-forfaits/ouverture.html'
CAOlinkEN = 'https://accounts.business.nbc.ca/start/?questionId_appt_ch=14&questionId_canal=NBC.CA&customType=ENTR&productId=CC-ENT-CA&packageId=OFFRE-GEN&conditionId=&language=EN&exitUrl=business/banking/accounts-packages/opening.html'
LandinglinkEN = 'https://www.nbc.ca/business/banking/accounts-packages/opening.html'
browserList = {'Chrome': webdriver.Chrome(executable_path=r'C:\Users\eli\AppData\Local\Browser_drivers\chromedriver.exe'), 'Firefox': webdriver.Firefox(executable_path=r'C:\Users\eli\AppData\Local\Browser_drivers\geckodriver.exe'), 'Edge': webdriver.Edge()}

def checkLink():
    if CTAlink.get_attribute('href') == CAOlinkFR:
        return 'The link is CAO'
    elif CTAlink.get_attribute('href') == LandinglinkFR:
        return 'The link is Landing'
    elif CTAlink.get_attribute('href') == CAOlinkEN:
        return 'The link is CAO'
    elif CTAlink.get_attribute('href') == LandinglinkEN:
        return 'The link is Landing'
    else:
        return 'This shit is not right'

print('Starting QA for test 0171 - Variation B')
for url in testPages:
    page = urllib.request.urlopen(url)
    entrepriseSoup = BeautifulSoup(page, "html5lib")
    for browser, browserDriver in browserList.items():
        driver = browserDriver
        driver.get(url)
       # assert "entrepreneurs" in driver.title
        CTAlink = driver.find_element(By.XPATH, '//p[@class="chapeau3"]/a')
        breakPoints = {'desktop': driver.set_window_size(1020, 800), 'tablet': driver.set_window_size(768, 800),
                       'mobile': driver.set_window_size(320, 800)}
        for device, size in breakPoints.items():
                changeSize = size
                browserCheck = checkLink()
                print(str(browserCheck) + ' sur ' + str(browser) + ' en ' + str(device))
    if url == testPages[0]:
        print('Language switch')
    else:
        print('End of QA')
driver.close()
