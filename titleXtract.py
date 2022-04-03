import requests
from bs4 import BeautifulSoup

url = input("Enter Project URL: ")
response = requests.get(url)
htmlParsedContent = BeautifulSoup(response.content, 'html.parser')
title = htmlParsedContent.head.title.string.strip().split('-')[2:4]
titleHead = ("-".join(title).strip().replace("- ", " - "))
print(titleHead)




