from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import os

# instantiate options
# opts = Options()
# opts.binary_location = "<path to Chrome executable>"

# set location of webdriver
chrome_driver = os.getcwd() + "/chromedriver"

# instantiate webdriver
driver = webdriver.Chrome( executable_path=chrome_driver)

# load webpage
driver.get('https://newsday.co.tt/2022/06/08/police-hunt-man-shot-by-fellow-bandit-in-petit-valley/')

# parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source)
print(soup.find("article", {"class" : "article-content"}).get_text())