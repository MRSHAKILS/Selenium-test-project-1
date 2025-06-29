from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
import time
import random

SBR_WEBDRIVER = f'https://brd-customer-hl_8a10678a-zone-tutorial_selenium:sv1v6rjg51wl@brd.superproxy.io:9515'

def main():
    print('Connecting to Scraping Browser ...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    
    # Add more human-like options
    options = ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    
    with Remote(sbr_connection, options=options) as driver:
        # Hide webdriver property
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        print('Connected! Navigating to https://google.com...')
        driver.get('https://google.com')
        
        # Add random delay to mimic human behavior
        time.sleep(random.uniform(2, 5))
        
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        print(html)

if __name__ == '__main__':
    main()