from selenium import webdriver


url = input("Enter url: ")
driver = webdriver.Edge(executable_path = 'E:\edgedriver_win64\msedgedriver.exe')
driver.maximize_window()
driver.get(url)



