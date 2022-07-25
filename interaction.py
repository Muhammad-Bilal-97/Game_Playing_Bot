from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "D:\Development\chromedriver_v103\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.maximize_window()
#driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")

# stats = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#
# all_portals = driver.find_element(By.LINK_TEXT, "Portals")
# all_portals.click()

# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("ABC")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("ABC")

email = driver.find_element(By.NAME, "email")
email.send_keys("XYZ@gmail.com")

sign_up = driver.find_element(By.CSS_SELECTOR, "form button")
sign_up.click()
