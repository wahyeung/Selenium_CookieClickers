from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



# Set up the ChromeDriver service
service = Service(executable_path="./chromedriver")
driver = webdriver.Chrome(service=service)

# Navigate to the e-commerce website
driver.get("https://workco-qa-assessment.netlify.app")

# Wait until the password input box is present
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.NAME,"password"))
)
input_element = driver.find_element(By.NAME, "password")
input_element.clear()

# Enter the password and submit
input_element.send_keys("w&c0-252!$@2445" + Keys.ENTER)
time.sleep(1)

# Wait for the 'Start Shopping' link to become clickable
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"Splash_productLink__1k_IV"))
)
link = driver.find_element(By.CLASS_NAME,"Splash_productLink__1k_IV")
link.click()

# Wait for the 'Add to Bag' button to become clickable
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"Product_addButton__81Hci"))
)
link = driver.find_element(By.CLASS_NAME,"Product_addButton__81Hci")
link.click()

time.sleep(1)

# Wait for the shopping cart button to become clickable and click it
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"CartButton_button__2zU4G"))
)
link = driver.find_element(By.CLASS_NAME,"CartButton_button__2zU4G")
link.click()

# Wait for the 'Checkout' button to become clickable and click it
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME,"Cart_checkoutBtn__2XCNJ"))
)
link = driver.find_element(By.CLASS_NAME,"Cart_checkoutBtn__2XCNJ")
link.click()

# Wait for the login form to appear, clear any previous inputs, and enter the username and password
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.NAME,"username"))
)
input_element = driver.find_element(By.NAME, "username")
input_element.clear()
input_element.send_keys("admin")
time.sleep(0.5)
input_element = driver.find_element(By.NAME, "password")
input_element.clear()
input_element.send_keys("admin")
time.sleep(1)
# Find and click the 'Log in' button
link = driver.find_element(By.XPATH, "//button[@class='Button_button__2Lf63' and text()='Log in']")
link.click()

# Fill out the payment form with test data
WebDriverWait(driver,5).until(
    EC.presence_of_all_elements_located((By.NAME,"firstName"))
)
input_element = driver.find_element(By.NAME, "firstName")
input_element.clear()
input_element.send_keys("Luna")
time.sleep(0.5)
input_element = driver.find_element(By.NAME, "lastName")
input_element.clear()
input_element.send_keys("Lu")
time.sleep(0.5)
input_element = driver.find_element(By.NAME, "ccNumber")
input_element.clear()
input_element.send_keys("1234567890")
time.sleep(0.5)
input_element = driver.find_element(By.NAME, "expiration")
input_element.clear()
input_element.send_keys("01/01")
time.sleep(0.5)
input_element = driver.find_element(By.NAME, "cvv")
input_element.clear()
input_element.send_keys("987")
time.sleep(0.5)

# Click the 'Place order' button
link = driver.find_element(By.XPATH, "//button[@class='Button_button__2Lf63' and text()='Place order']")
link.click()

# Wait for the order confirmation page to load, then take a screenshot
time.sleep(2)
driver.get_screenshot_as_file("results.png")

# Verify that the order number is displayed exactly once on the confirmation page
html = driver.page_source
C = html.count("Your order number is")
print(C)
assert C == 1, f"Test Failed: {C=}"

# Clean up by closing the browser after a delay
time.sleep(5)
driver.quit()
