from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import requests
from selenium.webdriver.support.select import Select


wDriver = webdriver.Edge(executable_path = "E:\\edgedriver_win64\\msedgedriver.exe")
print(wDriver.title)
print(wDriver.current_url)
wDriver.maximize_window()
wDriver.get("https://documents.worldbank.org/en/publication/documents-reports/documentdetail/925571629439639283/India-SOUTH-ASIA-P173958-Mizoram-Health-Systems-Strengthening-Project-Procurement-Plan/")
time.sleep(5)
print("\nTest Cases")

# wDriver.maximize_window()


continue_link = wDriver.find_element_by_link_text('Official PDF')
type(continue_link)