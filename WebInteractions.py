import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.com/")
searchbar = driver.find_element_by_name("q")
searchbar.sendkeys("selenium")
time.sleep(5)
driver.quit()