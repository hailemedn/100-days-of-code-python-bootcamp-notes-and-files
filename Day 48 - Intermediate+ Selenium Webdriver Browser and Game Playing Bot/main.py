from selenium import webdriver
from selenium.webdriver.common.by import By

# chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://www.python.org/")
# search_bar = driver.find_element(By.NAME, "q")
# print(search_bar.get_attribute("placeholder"))
#
# logo = driver.find_element(By.CLASS_NAME, "python-logo")
# print(logo.size)
#
# doc_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# print(doc_link.text)
#
# latest_news = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[1]/div/ul/li[1]/a')
# print(latest_news.text)

dates_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li>time")
dates_list_text = [date.text for date in dates_list]
# print(dates_list_text)

events_list = driver.find_elements(By.CSS_SELECTOR, ".event-widget li> time+a")
events_list_text = [event.text for event in events_list]
# print(events_list_text)
print(len(dates_list_text))
print(len(events_list_text))
key = 0
data = {}

for n in range(len(events_list_text)):
    data[n] = {"time": dates_list_text[key], "name": events_list_text[key]}
    key = key + 1

print(data)








# driver.close() # closes a tab.
driver.quit() # closes the browser.


