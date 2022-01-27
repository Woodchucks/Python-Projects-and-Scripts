import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import time

EMAIL = os.environ['GMAIL_USER']
PASSWORD = os.environ['GMAIL_PASSWORD']

driver_chrome = os.environ['CHROME_DRIVER_PATH']
driver = webdriver.Chrome(executable_path=driver_chrome)
driver.get("https://tinder.com/")

log_in = driver.find_element_by_xpath('//*[@id="t-48487324"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span')
log_in.click()
time.sleep(1)

log_in_with_google = driver.find_element_by_xpath('//*[@id="t-1776868400"]/div/div/div[1]/div/div[3]/span/div[1]/div/button/span[2]')
log_in_with_google.click()
time.sleep(1)

base_window = driver.window_handles[0]
gmail_login_window = driver.window_handles[1]
driver.switch_to.window(gmail_login_window)
print(driver.title)

email_field = driver.find_element_by_xpath('//*[@id="yDmH0d"]')
email_field.send_keys(EMAIL)
email_field.send_keys(Keys.ENTER)
time.sleep(5)

password_button = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
password_button.send_keys(PASSWORD)
password_button.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
time.sleep(5)

allow_location_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

notifications_button = driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

cookies = driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):
    time.sleep(1)
    try:
        like_button = driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            back_to_tinder_button = driver.find_element_by_css_selector(".itsAMatch a")
            back_to_tinder_button.click()
        except NoSuchElementException:
            time.sleep(2)

driver.quit()
