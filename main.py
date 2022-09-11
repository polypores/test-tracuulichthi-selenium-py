from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time

CHROME_DRIVER_PATH = "./chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('ignore-certificate-errors')

driver = webdriver.Chrome(CHROME_DRIVER_PATH, options=options)

driver.get("https://tracuulichthi.sgu.edu.vn/")

# print(driver.title)

# print(driver.page_source)

# search = driver.find_element_by_id("input-8")

search = WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.ID, "input-8")))

print(search)

# mã số sinh viên ai đó thì tui k biết

search.send_keys("3120560075")
search.send_keys(Keys.RETURN)
time.sleep(4)

label = driver.find_element("xpath", "//*[contains(text(), 'Họ và tên:')]")
label2 = label.find_element("xpath", '..')
label3 = label2.find_element("xpath", '..')
print(label3.text)

time.sleep(14)

# search.clear()
# search.send_keys("3120560074")
# search.send_keys(Keys.RETURN)

# time.sleep(10)

driver.quit()