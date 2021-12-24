from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
import pyperclip
import time

# To set headless
options = Options()
options.headless = False

# to close after execution
# with Firefox(options=options, executable_path=r'C:\DRIVERS\User\geckodriver.exe') as driver:

driver = Firefox(
    options=options, executable_path=r'C:\DRIVERS\User\geckodriver.exe')
# opening the url
driver.get("https://www.guerrillamail.com/")
# waiting for page load
wait = WebDriverWait(driver, 10)
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1

driver.find_element(By.ID, "gm-host-select").click()
driver.find_element_by_xpath(("//option[@value='spam4.me']")).click()

driver.find_element(By.ID, "use-alias").click()
temp_email = driver.find_element(By.ID, "email-widget").text

pyperclip.copy(temp_email)
print("Temporary email address: ", temp_email, "copied to clipboard!")
