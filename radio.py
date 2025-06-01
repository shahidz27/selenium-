from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_experimental_option("detach" , True)
driver = webdriver.Chrome(options=options)

driver.get("https://training.qaonlinetraining.com/testPage.php")

radio = driver.find_element(By.XPATH,"/html/body/form/input[5]")
radio.click()

if(radio.is_selected()):
    print("test passed")
else:
    print(("test failed"))