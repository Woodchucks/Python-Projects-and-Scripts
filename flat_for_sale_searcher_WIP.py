IMPORT OS
from bs4 import BeautifulSoup
from selenium import webdriver
import requests

OLX_URL = "https://www.olx.pl/nieruchomosci/mieszkania/sprzedaz/wroclaw/?search%5Bfilter_float_price%3Ato%5D=400000&search%5Bfilter_enum_builttype%5D%5B0%5D=blok&search%5Bfilter_enum_builttype%5D%5B1%5D=apartamentowiec&search%5Bfilter_enum_builttype%5D%5B2%5D=loft&search%5Bfilter_float_m%3Afrom%5D=25&search%5Bfilter_float_m%3Ato%5D=50&search%5Bfilter_enum_rooms%5D%5B0%5D=one&search%5Bdistrict_id%5D=387"
FORM_LINK = os.environ['FORM_LINK']
FORM_RESPONSES_LINK = os.environ['FORM_RESPONSES_LINK']
CHROME_DRIVER_PATH = os.environ['CHROME_DRIVER']

# BeautifulSoup
response = requests.get(OLX_URL)
olx_web_page = response.text

soup = BeautifulSoup(olx_web_page, "html.parser")

titles = []
links = []
cost = []

links_1 = soup.find_all(class_='marginright5 link linkWithHash detailsLinkPromoted', href=True)
links_2 = soup.find_all(class_='marginright5 link linkWithHash detailsLink', href=True)
prices = soup.find_all(name='p',class_='price')
promoted_prices = soup.find(name='table', class_='fixed breakword promoted-list ad_idGvdh2')
promoted_prices = promoted_prices.find_all(name='a', class_='marginright5 link linkWithHash detailsLinkPromoted linkWithHashPromoted')

for item in links_1:
    titles.append(item.getText().split("\n")[1])
    links.append(item['href'])
for item in links_2:
    titles.append(item.getText().split("\n")[1])
    links.append(item['href'])
for price in prices:
    cost.append(price.getText().strip())
for _ in range(len(promoted_prices)):
    cost.pop(_)

# Selenium
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(FORM_LINK)
for j in range(0,4):
    for i in range(0,3):
        question = driver.find_element_by_xpath(f'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[{i+1}]/div/div/div[2]/div/div[1]/div/div[1]/input')
        if i==0:
            question.send_keys(f"{titles[j]}")
        elif i==1:
            question.send_keys(f"{cost[j]}")
        else:
            question.send_keys(f"{links[j]}")
    button = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    button.click()
    insert_details_next_flat = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    insert_details_next_flat.click()
driver.quit()

driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(FORM_RESPONSES_LINK)

create_spreadsheet = driver.find_element_by_xpath('//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span/span/div/div[1]')
create_spreadsheet.click()
confirm_button = driver.find_element_by_xpath('//*[@id="wizViewportRootId"]/div[23]/div/div[2]/div[3]/div[2]/span/span')
confirm_button.click()

driver.quit()
