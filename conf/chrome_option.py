from selenium import webdriver


option = webdriver.ChromeOption()
option.add_argument('disable-infobars')
option.add_argument('headless')

