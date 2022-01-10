# fresh look at how to scrape a website

# install beautifulsoup4
# install requests


# beautifulsoup4 for downloading the data
# requests for assessing the data from an html format

# import both requests and beautifulsoup and start working with it
import requests
from bs4 import BeautifulSoup
football = requests.get('https://fbref.com')

foot = BeautifulSoup(football.text, 'html.parser')

print(foot)
