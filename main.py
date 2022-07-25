from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "D:\Development\chromedriver_v103\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element(By.CLASS_NAME, "a-price-whole")
# print(price.text)

#upcoming_events = driver.find_element(By.CLASS_NAME, "medium-widget event-widget last")
event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

# driver.close()
driver.quit()
