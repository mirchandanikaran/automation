from selenium import webdriver
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import requests
from bs4 import BeautifulSoup

#downloadLocation = ("E:\PyautoguiOutput\")

# url = input("Enter url: ")
url = "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/131121629282449815/india-south-asia-p162679-west-bengal-major-irrigation-and-flood-management-project-procurement-plan"
driver = webdriver.Edge(executable_path = 'E:\edgedriver_win64\msedgedriver.exe')
driver.maximize_window()
driver.get(url)

# url = input("Enter Project URL: ")
response = requests.get(url)
htmlParsedContent = BeautifulSoup(response.content, 'html.parser')
title = htmlParsedContent.head.title.string.strip().split('-')[2:4]
titleHead = ("-".join(title).strip().replace("- ", " - "))
print(titleHead)

while 1:
     if pyautogui.locateOnScreen('pdflink.png', grayscale=True, confidence=0.8, region=(861,768,250,150)) != None:
    #  if pyautogui.locateOnScreen('pdflink.png', grayscale=True, confidence=0.8, region=(955,672,250,150)) != None:
        print("Official PDF Link Located")
        print("Confidence: 80%")
        time.sleep(0.5)

        while True:
            location = pyautogui.locateOnScreen('pdflink.png')
            pyautogui.click(location)
            time.sleep(2)

            if pyautogui.locateOnScreen('downButton.png', grayscale=True, confidence=0.8, region=(1782,106,50,50)) != None:
                print("Download Button Located")
                print("Confidence: 80%")
                downButton = pyautogui.locateOnScreen('downButton.png')
                pyautogui.click(downButton)
                time.sleep(0.5)
                break

        
            
     else:
        print("I am unable to see it")
