from encodings import utf_8
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re
from bs4 import BeautifulSoup
from PyPDF2 import PdfFileReader
import wget
def load(driver):
    presence = len(driver.find_elements(By.LINK_TEXT, "Load more"))
    while( presence > 0):
        try:
            load_link = WebDriverWait(driver, 50000).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Load more"))
            )
        finally:
            load_link.click()
            presence = len(driver.find_elements(By.LINK_TEXT, "Load more"))

# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.implicitly_wait(30)
# driver.get("https://www.oercommons.org/curated-collections/1111?__hub_id=1")
# # counter = driver.find_element(By.CLASS_NAME, "counter").text
# # load(driver)
# html = driver.page_source
# soup = BeautifulSoup(html, "html.parser")
# print(soup.find(class_="counter").text)
# items = soup.find(class_="js-index-item")
# print(items.find(class_="item-link").text)
# info = items.find(class_="item-info")
# tmp = []
# info_dict = {}
#python generator need to be conver to a list to be reverse
#the info section likely to be reserved for the description box
# for tag in reversed(list(info.children)):
#     if(tag.name == 'dd'):
#         tmp.append(tag.text)
#     if(tag.name == 'dt'):
#         info_dict[tag.text] = tmp.copy()
#         tmp.clear()
# lics = items[1].find(class_="cou-bucket").find("span").text
# print(lics)
# print(info_dict)
# driver.quit()
# html = requests.get("https://www.oercommons.org/authoring/47217-3-md-c-7b-finding-area_madison-s-garden?__hub_id=1")
# soup = BeautifulSoup(html.text, "html.parser")
# tmp = []
# info_dict = {}
# overview = soup.find("dd", {"itemprop":"description"}).text
# subject = []
# for item in soup.find_all("span", {"itemprop":"about"}):
#     subject.append(item.text)
# mat_type = []
# for item in soup.find_all("span", {"itemprop":"learningResourceType"}):
#     mat_type.append(item.text)
# authors = {}
# for item in soup.find_all("span", {"itemprop":"author"}):
#     author = item.find("a", {"itemprop":"name"})
#     authors[author.text] = author.get('href')
# license = soup.find("a", {"rel":"license"}).text.strip()
# language = []
# for item in soup.find_all("span", {"itemprop":"inLanguage"}):
#     language.append(item.text)
# media_format = []
# for item in soup.find_all("span", {"itemprop":"genre"}):
#     media_format.append(item.text)

# level = list(soup.find("dt", string="Level:").next_siblings)[1].text.strip().split(", ")
# grades = list(soup.find("dt", string="Grades:").next_siblings)[1].text.strip().split(", ")

# remix_check = soup.find("dt", string="Remix of:")
# remix = {}
# if remix_check is not None:
#     original = list(remix_check.next_siblings)[1]
#     remix['title'] = original.text.strip()
#     remix['link'] = original.find("a").get('href')

# tags = []
# for tag in soup.find_all("li", class_="tag-instance"):
#     tags.append(tag.text.strip())

# vist = list(soup.find(class_='fa-eye').next_siblings)[3].text
# save = list(soup.find(class_='fa-save').next_siblings)[3].text
# comment_count = list(soup.find(class_='fa-comment').next_siblings)[3].text

# rating = soup.find(class_='stars').get('data-rating-value')
# rater_count = 0
# if len(list(soup.find(class_='stars').next_siblings)) > 0:
#     rater_count = re.sub(r"[()]","",list(soup.find(class_='stars').next_siblings)[1].text)
# print(rater_count)

# test = "Grade 3, Measurement and Data"
# if re.match(r"(Grade \d)",test):
#     if "," in test:
#         print(re.sub(r".*(Grade \d).*", r"\1", test).strip())
# PDF = PdfFileReader('3.MD.C.7b - Finding Area_Madison\'s Garden.pdf')

# pages = PDF.getNumPages()
# key = '/Annots'
# uri = '/URI'
# ank = '/A'
# pattern = r"(related-resource)\/.*\/(download)"
# pattern2 = r"(editor)\/(documents)\/.*$"
# for page in range(pages):
#     print("Current Page: {}".format(page))
#     pageSliced = PDF.getPage(page)
#     pageObject = pageSliced.getObject()
#     # if /Annots is a key in the page 
#     if key in pageObject.keys():
#         # give me the annotation object from the page
#         ann = pageObject[key]
#         # for every annoation in the annotation object
#         for a in ann:
#             # give the python oject of the annotation
#             u = a.getObject()
#             # check if the /URI is in the object annotation[/A]
#             if uri in u[ank].keys():
#                 if re.search(pattern, u[ank][uri]) or re.search(pattern2, u[ank][uri]):
#                     wget.download(u[ank][uri])

def scroll_down(elem, num):
    for _ in range(num):
        time.sleep(.01)
        elem.send_keys(Keys.PAGE_DOWN)

url = "https://store.steampowered.com/search/?category1=998&supportedlang=english"
options = Options()
options.add_argument("--headless")
options.add_argument("window-size=1400,1500")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("start-maximized")
options.add_argument("enable-automation")
options.add_argument("--disable-infobars")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(30)
SCROLL_PAUSE_TIME = 10
elem = driver.find_element_by_tag_name("body")
prev_height = elem.get_attribute("scrollHeight")
driver.get("https://store.steampowered.com/search/?category1=998&supportedlang=english")
for i in range(0, 500):
    scroll_down()

