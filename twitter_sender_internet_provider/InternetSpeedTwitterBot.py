import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

SPEED_TEST = "https://www.speedtest.net/"
TWITTER = "https://twitter.com/home"
EMAIL = os.environ['EMAIL']

class InternetSpeedTwitterBot:
    def __init__(self):
        chrome_driver = os.environ['CHROME_DRIVER']
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST)
        consent_button = self.driver.find_element_by_xpath('//*[@id="_evidon-banner-acceptbutton"]')
        consent_button.click()
        go_button = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        go_button.click()
        time.sleep(50)
        self.down = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.up = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span').text
        self.driver.quit()

    def tweet_at_provider(self):
        self.driver.get(TWITTER)
        time.sleep(6)
        login_with_google = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[2]/span[1]')
        login_with_google.click()
        time.sleep(1)
        base_window = self.driver.window_handles[0]
        gmail_login_window = self.driver.window_handles[1]
        self.driver.switch_to.window(gmail_login_window)
        choose_email = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        choose_email.send_keys(EMAIL)
        choose_email.send_keys(Keys.ENTER)
        self.driver.switch_to.window(base_window)

        # tweeting the actual message
        message = f"Hey Internet Provider, why is my internet speed" \
                  f"{self.down}down/{self.up}up when I pay for 150down/10up?"
        tweeter_msgbox = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
        tweeter_msgbox.send_keys(message)
        tweet_btn = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        tweet_btn.click()
        time.sleep(2)
        self.driver.quit()
