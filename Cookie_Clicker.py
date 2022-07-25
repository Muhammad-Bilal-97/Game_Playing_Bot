from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = "D:\Development\chromedriver_v103\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element(By.ID, "cookie")

# Get upgrade item ids.
items = driver.find_element(By.CSS_SELECTOR, "#store div")
item_ids = [items.get_attribute("id" for item in items)]

timeout = time.time() + 5
five_min = time.time() + 60*5 # 5 minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:
        # get all upgrade <b> tags
        all_prices = driver.find_element(By.CSS_SELECTOR, "#store b")
        item_prices = []

        # convert <b> text into an integer price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)
        # create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # get current cookie count
        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(By.ID, "to_purchase_id").click()

        # add another 5 seconds until the next check
        timeout = time.time() + 5

    # after 5 minutes stop the bot and check the cookies per second count
    if time.time() > five_min:
        cookie_per_sec = driver.find_element(By.ID, "cps").text
        print(cookie_per_sec)
        break





