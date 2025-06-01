from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")
driver.find_element(By.NAME,"q").send_keys("selenium")
driver.find_element(By.CLASS_NAME,"gNO89b").submit()