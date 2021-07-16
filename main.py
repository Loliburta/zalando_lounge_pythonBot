from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
import time

site = "https://www.zalando-lounge.pl/campaigns/ZZO1ER5/categories/253250191/articles/IC322S025-Q11"
preferedSize = "M"
timeBetweenSiteRefresh = 2
ChromeUserPath = "user-data-dir=/home/loliburta/.config/google-chrome/Profile 1"

ua = UserAgent()
a = ua.random
user_agent = ua.random
options = Options()
options.add_argument(ChromeUserPath)
options.add_argument("window-size=1100,600")
options.add_argument(f'user-agent={user_agent}')
PATH = "./chromedriver"
driver = webdriver.Chrome(executable_path=PATH, options=options)

driver.get(site)

while True:
    size = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f"//span[text()='{preferedSize}']")))
    buttonToChooseSize = size.find_element_by_xpath('..')
    isDisabled = buttonToChooseSize.get_property("disabled")
    if isDisabled == False:
        break
    print("button size is disabled")
    print(f"refreshing in {timeBetweenSiteRefresh}s")
    time.sleep(timeBetweenSiteRefresh)
    driver.refresh()
    print("site refreshed")
  

    
buttonToChooseSize.click()
cart = driver.find_element_by_xpath(f"//span[text()='Do koszyka']")
cart.click()