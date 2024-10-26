from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By

url = "https://www.libraryofshortstories.com/stories"

page = requests.get(url)
driver = webdriver.Safari()
driver.get(url)

elements = driver.find_elements(By.CSS_SELECTOR, ".story_tiles")

for element in elements:
    link = element.find_element("css selector", "a").text
    print(link)
