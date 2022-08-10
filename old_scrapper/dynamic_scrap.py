# selenium 4, ChromeDriver with Webdriver Manager
# from re import sub
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time
import requests
from bs4 import BeautifulSoup
import re
import Scrappy

def find_a(soup, type, urlPattern, result):
    a_arr = soup.find_all('a')
    for link in a_arr:
        if (type in link.get('href')):
            if ("introduction" not in link.get('href')):
                if (re.search(urlPattern, link.get('href'))):
                    result.append(link.get('href'))
# urls = ["http://www.corestandards.org/Math/Content/HSF/BF/",
# "http://www.corestandards.org/Math/Content/6/NS/",
# "http://www.corestandards.org/ELA-Literacy/RF/1/"]
urls = []
ELA_URL= "http://www.corestandards.org/ELA-Literacy/"
MATH_URL = "http://www.corestandards.org/Math/"

ELA_DOC = requests.get(ELA_URL)
MATH_DOC = requests.get(MATH_URL)

ELA_SOUP = BeautifulSoup(ELA_DOC.text, 'html.parser')
MATH_SOUP = BeautifulSoup(MATH_DOC.text, 'html.parser')
find_a(ELA_SOUP, "ELA-Literacy", "http:\/\/www\.corestandards\.org\/ELA-Literacy\/.{1,10}\/.{1,10}$", urls)
find_a(MATH_SOUP, "Math/Content", "http:\/\/www\.corestandards\.org\/Math\/Content\/.{1,10}\/.{1,10}$", urls)
scrapper = Scrappy.Scrap(urls, "Crosswalk_with_CA_OR_OH_MA_010722.xlsx - Sheet1.csv", "output.csv")
# urls1 = ["http://www.corestandards.org/Math/Content/HSA/CED/"]
# scrapper = Scrappy.Scrap(urls, "Crosswalk_with_CA_OR_OH_MA_010722.xlsx - Sheet1 copy.csv", "output.csv")
substandards = scrapper.scrap()
scrapper.writeCSV(substandards)