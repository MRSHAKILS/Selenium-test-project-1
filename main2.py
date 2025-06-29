from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
# from selenium.webdriver.common.by import By
# AUTH = 'brd-customer-hl_58d62607-zone-tutorial_selenium:hg3mn1se1my3'
SBR_WEBDRIVER = f'https://brd-customer-hl_8a10678a-zone-tutorial_selenium:sv1v6rjg51wl@brd.superproxy.io.9515'
def main():
    print('Connecting to Scraping Browser ...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating to https://google.com...')
        driver.get('https://google.com')
        print('Taking page screenshot to file page.png')
        driver.get_screenshot_as_file('./page.png')
        print('Navigated! Scraping page content...')
        html = driver.page_source
        print(html)
if __name__ == '__main__':
  main()