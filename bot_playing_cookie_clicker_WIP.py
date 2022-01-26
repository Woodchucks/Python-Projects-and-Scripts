import time
from selenium import webdriver

driver_chrome = r"C:\Users\Sansiowy\PycharmProjects\WebDevelopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_chrome)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

timeout_start = time.time()
timeout = time.time() + 300
time_check = time.time() + 5
cookie = driver.find_element_by_id("cookie")
cookie_money = driver.find_element_by_id("money")
money = int(cookie_money.text)
prices = driver.find_elements_by_css_selector("#store b")[:-1]
prices_formatted = [price.text.strip().split(" - ")[1] for price in prices]
for _ in range(3, 8):
    prices_formatted[_] = prices_formatted[_].replace(",", "")
prices_formatted = [int(price) for price in prices_formatted]
shop = driver.find_elements_by_css_selector("#store div")[:-1]

while True:
    if time.time() >= timeout:
        break
    if time.time() > time_check:
        time_check += 5
        for i in range(len(prices_formatted)):
            if i == 8:
                shop[0].click()
            if money >= prices_formatted[len(prices_formatted)-1-i]:
                shop[7-i].click()
    cookie.click()
driver.quit()
