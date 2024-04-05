from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# https://sites.google.com/chromium.org/driver/

service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"gLFyf"))
    )
input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
input_element.clear()
input_element.send_keys("Three Billboards" + Keys.ENTER)

WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT,"Three Billboards"))
    )

link = driver.find_element(By.PARTIAL_LINK_TEXT,"Three Billboards")
link.click()
time.sleep(10)
driver.quit()