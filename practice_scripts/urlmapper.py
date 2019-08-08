
from bs4 import BeautifulSoup
import requests
import requests.exceptions
from urllib.parse import urlsplit
from urllib.parse import urlparse
from collections import deque

url = 'https://www.bnc.ca/particuliers/comptes.html'

# a queue of urls to be crawled next
#new_urls = deque([url])
# a set of urls that we have already processed
#processed_urls = set()
# a set of domains inside the target website
#local_urls = set()
# a set of domains outside the target website
#foreign_urls = set()
# a set of broken urls
#broken_urls = set()

page = request.urlopen(url)
soup = BeautifulSoup(page, "html5lib")
linksonpage = soup.find_all('a')