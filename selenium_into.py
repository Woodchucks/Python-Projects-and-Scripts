from selenium import webdriver

chrome_driver_path = r"C:\Users\Sansiowy\PycharmProjects\WebDevelopment\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")

dates =[]
names = []
for _ in range(1,6):
    dates = driver.find_element_by_css_selector(".event-widget time")
    names = driver.find_element_by_css_selector(".event-widget li a")

events = {}
for _ in range(len(dates)):
    events[_] = {
        "time": dates[_].text,
        "name": names[_].text,
    }
print(events)
driver.close()
