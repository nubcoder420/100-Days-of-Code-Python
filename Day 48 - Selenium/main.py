from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#------------- Browser stays open -------------#
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#-----------------------------------------------#


driver = webdriver.Chrome(options=chrome_options)

URL = "https://orteil.dashnet.org/experiments/cookie/"

driver.get(url=URL)

cookie = driver.find_element(By.ID, "cookie")

items = driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in items]

price_list = driver.find_elements(By.CSS_SELECTOR, "#store div b")
price = [price.text for price in price_list]

price_list = [int(text.split('-')[-1].replace(',', '').strip()) for text in price if text]

store = dict(zip(item_ids, price_list))

def check_money():
    money = int(driver.find_element(By.ID, "money").text.replace(',', ''))
    return money


def buy_upgrade(money):
    max_affordable_key = None
    max_affordable_value = 0

    for key, value in store.items():
        if money >= value > max_affordable_value:
            max_affordable_key = key
            max_affordable_value = value

    if max_affordable_key:
        print(f"The key of the highest affordable value with {money} is '{max_affordable_key}' with a value of {max_affordable_value}.")
        driver.find_element(By.ID, f'{max_affordable_key}').click()
        print(f"Bought {max_affordable_key}")
        print(store)
    else:
        print(f"You can't afford any items in the store with {money}.")


timeout = time.time() + 60
duration = 5
start_time = time.time()

while True:
    cookie.click()

    current_time = time.time()
    elapsed_time = current_time - start_time

    if elapsed_time >= duration:

        print(check_money())
        buy_upgrade(check_money())

        start_time = time.time()
