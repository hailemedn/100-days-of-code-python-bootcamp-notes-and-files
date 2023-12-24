from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Haile")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Ramos")

email = driver.find_element(By.NAME, "email")
email.send_keys("haile@gmail.com")

sign_up_button = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up_button.send_keys(Keys.ENTER)




