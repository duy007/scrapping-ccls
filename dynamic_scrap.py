# selenium 4, ChromeDriver with Webdriver Manager
from re import sub
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import Scrappy

urls = ["http://www.corestandards.org/Math/Content/HSF/BF/",
"http://www.corestandards.org/Math/Content/6/NS/",
"http://www.corestandards.org/ELA-Literacy/RF/1/"]

# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver = webdriver.Chrome(executable_path="/opt/homebrew/bin/chromedriver")

# options = Options()
# driver = webdriver.Chrome(options=options)

# driver.get("http://www.corestandards.org/Math/Content/6/RP/")
# substandards = driver.find_element(By.CLASS_NAME, "substandard").text
# print(substandards)
# time.sleep(15)
# driver.quit

scrapper = Scrappy.Scrap(urls, "Crosswalk_with_CA_OR_OH_MA_010722.xlsx - Sheet1.csv", "output.csv")
substandards = scrapper.scrap()
scrapper.writeCSV(substandards)