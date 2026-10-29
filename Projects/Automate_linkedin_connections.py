#Install Required Libraries->  pip install selenium webdriver-manager

#Import Necessary Libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Log in to LinkedIn
# setup the browser
driver = webdiriver.Chrome(service = Service(ChromeDriverManager.install()))
driver.get("https://www.linkedin.com/login")

#Enter login credentials
username = driver.find_element(By.ID, "username")
password = driver.find_element(By.ID, "password")
username.send_keys("morepranali0007@gmail.com")
password.send_keys("pranali@2531")

# Click login button
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

time.sleep(3)  #wait for the page to load
