from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# Add Chrome options for better reliability
chrome_options = Options()
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    driver.get("https://google.com")
    
    # Wait for search input to be present instead of using class name
    wait = WebDriverWait(driver, 10)
    input_element = wait.until(EC.presence_of_element_located((By.NAME, "q")))
    
    input_element.clear()
    input_element.send_keys("sky" + Keys.ENTER)
    
    # Wait for results to load
    wait.until(EC.presence_of_element_located((By.ID, "search")))
    
    time.sleep(20)  # Brief pause to see results
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()