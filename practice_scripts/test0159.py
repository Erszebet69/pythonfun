#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from bs4 import BeautifulSoup
import urllib.request
import re





#list of pages to test
testPages = {
    'Pages variation controle':
            {'page accueil': ['https://www.bnc.ca/entreprises.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_1&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_1&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'demarrage': ['https://www.bnc.ca/entreprises/plus-que-bancaire/stades/demarrage.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_1&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/going-further/stages/starting.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_1&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'solutions': ['https://www.bnc.ca/entreprises/solutions-bancaires.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_1&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/banking.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_1&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'comptes': ['https://www.bnc.ca/entreprises/solutions-bancaires/comptes-forfaits/comptes.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_1&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812']},
    'Pages variation B':
            {'page accueil': ['https://www.bnc.ca/entreprises.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'demarrage': ['https://www.bnc.ca/entreprises/plus-que-bancaire/stades/demarrage.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/going-further/stages/starting.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'solutions': ['https://www.bnc.ca/entreprises/solutions-bancaires.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/banking.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'comptes': ['https://www.bnc.ca/entreprises/solutions-bancaires/comptes-forfaits/comptes.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/banking/accounts-packages/accounts.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_2&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812']},
    'Pages variation C':
            {'page accueil': ['https://www.bnc.ca/entreprises.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'demarrage': ['https://www.bnc.ca/entreprises/plus-que-bancaire/stades/demarrage.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/going-further/stages/starting.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'solutions': ['https://www.bnc.ca/entreprises/solutions-bancaires.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/banking.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'comptes': ['https://www.bnc.ca/entreprises/solutions-bancaires/comptes-forfaits/comptes.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/banking/accounts-packages/accounts.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_3&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812']},
    'Pages variation D':
            {'page accueil': ['https://www.bnc.ca/entreprises.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'demarrage': ['https://www.bnc.ca/entreprises/plus-que-bancaire/stades/demarrage.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/going-further/stages/starting.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'solutions': ['https://www.bnc.ca/entreprises/solutions-bancaires.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/banking.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812'],
                'comptes': ['https://www.bnc.ca/entreprises/solutions-bancaires/comptes-forfaits/comptes.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812', 'https://www.nbc.ca/business/banking/accounts-packages/accounts.html?at_preview_token=wFUa7l1vU0%2Bic36AywNjohB5zHRflcauehUk1xPJLvY%3D&at_preview_index=1_4&at_preview_listed_activities_only=true&at_preview_evaluate_as_true_audience_ids=1656812']}
}
#lien vers le formulaire FR et EN challenger et controle
controle = ["Jusqu’à 900 $ de remise en adhérant à un forfait", 'Up to $900 cashback the first year when you sign up for a banking package']
varB = ['Faites-vous rembourser votre première année de frais bancaires sur votre forfait entreprise', 'Get your first year of bank fees on your business package.']
varC = ['Obtenez de 71 $ à 935 $ suite à l’ouverture d’un compte', 'Receive between $71 and $935 cashback after opening an account']
varD = ['On vous aide à démarrer', 'Helping you get started']

#options and desired capabilities
options = Options()
settingsDict = DesiredCapabilities.CHROME

#dictionary composed of the browser name (key) and the associated driver and settings (value)
browserList = {'Chrome': webdriver.Chrome(executable_path=r'C:\Users\eli\AppData\Local\Browser_drivers\chromedriver.exe', options=options), 'Firefox': webdriver.Firefox(executable_path=r'C:\Users\eli\AppData\Local\Browser_drivers\geckodriver.exe'), 'Edge': webdriver.Edge()}

#function checking the H3 text and matching it to one of the variations

def checkText():
    print(name +' sur la page ' + pageTitle)
    if bannerH2.text in controle:
        print('Le texte du H2 "' + bannerH2.text + '" correspond a la variation controle')
    elif bannerH2.text in varB:
        print('Le texte du H2 "' + bannerH2.text + '" correspond a la variation B')
    elif bannerH2.text in varC:
        print('Le texte du H2 "' + bannerH2.text + '" correspond a la variation C')
    elif bannerH2.text in varD:
        print('Le texte du H2 "' + bannerH2.text + '" correspond a la variation D')
    else:
        print('Le texte est errone "' + bannerH2.text + '"')
    return 'Variation text checked'

print("-" * 50)
print('Starting QA for test 0159 - All variations on all browsers for every breakpoints')
print('Opening browser')
for browser, browserDriver in browserList.items():  #loops over the browsers in the browser dict
    driver = browserDriver
    for name, variation in testPages.items():   #loops over the different variations
        for pageTitle, url in variation.items():   #loops over the URLs in the variation dict
            for lang in url:
                if lang == url[0]:
                    print('\n****  Checking ' + pageTitle + ' French URL  ****')
                else:
                    print('\n****  Checking ' + pageTitle + ' English URL  ****')
                driver.get(lang)    #gets current URL
                # cta h2 name to check against variations
                bannerH2 = driver.find_element(By.TAG_NAME, 'h2')
                # dictionary composed of the breakpoint name (key) and the associated window size) in order to run the test on each breakpoints
                breakPoints = {'desktop': driver.set_window_size(1080, 800),
                               'tablet': driver.set_window_size(768, 800),
                               'mobile': driver.set_window_size(320, 800)}
                for device, size in breakPoints.items():
                    changeSize = size
                    browserCheck = checkText()
                    print(str(browserCheck) + ' sur ' + str(browser) + ' en ' + str(device))
print('QA finished')

driver.close()
