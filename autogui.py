import pyautogui
import time
import keyboard
import random
import win32api, win32con
import requests
from bs4 import BeautifulSoup

url = "https://documents.worldbank.org/en/publication/documents-reports/documentdetail/131121629282449815/india-south-asia-p162679-west-bengal-major-irrigation-and-flood-management-project-procurement-plan"


def getTitle():

    response = requests.get(url)
    htmlParsedContent = BeautifulSoup(response.content, 'html.parser')
    title = htmlParsedContent.head.title.string.strip().split('-')[2:4]
    print("-".join(title).strip().replace("- ", " - "))

#def rightclick():
    #win32.api(SetCursorPos((x,y))
    #win32api.mouse_event(win32con.MOUSEEVENTIF_LEFTDOWN,0,0)
    #win32api.mouse_event(win32con.MOUSEEVENTIF_LEFTUP,0,0)



# while 1:
#      if pyautogui.locateOnScreen('pdflink.png', grayscale=True, confidence=0.8, region=(815,679,250,150)) != None:
#         print("Official Link located")
#         print("Confidence: 80%")      
#         time.sleep(0.5)

#         while True:
#             location = pyautogui.locateOnScreen('pdflink.png')
#             pyautogui.click(location)
#             time.sleep(2)

#             if pyautogui.locateOnScreen('downButton.png', grayscale=True, confidence=0.8, region=(1782,106,50,50)) != None:
#                 print("Download Button Located")
#                 print("Confidence: 80%")
#                 downButton = pyautogui.locateOnScreen('downButton.png')
#                 pyautogui.click(downButton)
#                 time.sleep(0.2)

#                 if pyautogui.locateOnScreen('downButton.png', grayscale=True, confidence=0.8, region=(1121,298,50,50)) != None:
#                     fileLoc = pyautogui.locateOnScreen('downloadLoc.png')
#                     pyautogui.click(fileLoc)
#                     pyautogui.hotkey('ctrl', 'v')

#                 break
                
        
    
