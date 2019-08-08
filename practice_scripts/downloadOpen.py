'''

Tasks
1. set up driver
2. get url
3. find download link
4. download file
5. open file when download finished

'''



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import urllib.request
from selenium.webdriver.chrome.options import Options

#main variables
pagesToCrawl = ['https://www.bnc.ca/entreprises.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjoin9M6yvbBbENaHowWYOb%2BI%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjoin9M6yvbBbENaHowWYOb%2BI%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812']
downloadLink = 'https://comptes.entreprises.bnc.ca/start/?questionId_appt_ch=14&questionId_canal=BNC.CA&customType=ENTR&productId=CC-ENT-CA&packageId=&conditionId=&language=FR&exitUrl=entreprises/solutions-bancaires/comptes-forfaits/ouverture.html'

#driver options set-up
options = Options()
options.headless = True


def downloadopen():
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


print('Starting file extraction')
for url in pagesToCrawl:
    driver = webdriver.Chrome(executable_path=chrome_exe, options=options)
    page = urllib.request.urlopen(url)
    driver.get(url)

    if url == pagesToCrawl[0]:
        print('Language switch')
    else:
        print('End of QA')
driver.close()