from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random

# ------------- Browser stays open -------------#
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
# chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
# -----------------------------------------------#

GOOGLE_FORMS_PAGE = 'YOUR FORMS LINK HERE'
ZILLOW_PAGE = 'https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}


driver = webdriver.Chrome(options=chrome_options)

#--------------------- GETTING DATA FROM ZILLOW -----------------------#
driver.get(url=ZILLOW_PAGE)
time.sleep(random.randint(16, 23))

driver.find_element(By.TAG_NAME, 'html').send_keys(Keys.END)
time.sleep(random.randint(4, 7))

resp = driver.page_source

soup = BeautifulSoup(resp, 'html.parser')

prices = soup.find_all('span', {'data-test': 'property-card-price'})
addresses = soup.find_all('address', {'data-test': 'property-card-addr'})
links = soup.find_all('a', {'data-test': 'property-card-link'})

price_list = [price.get_text() for price in prices]
address_list = [address.get_text() for address in addresses]
link_list = list(set([link.get('href') for link in links]))

print(price_list)
print(address_list)
print(link_list)

print()

print(f"length of price_list: {len(price_list)}")
print(f"length of address_list: {len(address_list)}")
print(f"length of link_list: {len(link_list)}")

#--------------------- TRANSFER DATA TO GOOGLE FORMS -----------------------#
# FOR TESTING GOOGLE FORMS
# # Sample data for the 'price' list
# price_list = ["$1,500/mo", "$2,000/mo", "$2,500/mo", "$1,800/mo", "$2,200/mo"]

# # Sample data for the 'address' list
# address_list = [
#     "2623 Martin Luther King Jr Way APT 2, Oakland, CA 94612",
#     "1284-1286 7th Ave #1284, San Francisco, CA 94122",
#     "123 Main St, Los Angeles, CA 90001",
#     "456 Elm St, Chicago, IL 60601",
#     "789 Maple St, New York, NY 10001"
# ]

# # Sample data for the 'link' list
# link_list = [
#     "https://www.zillow.com/homedetails/2623-Martin-Luther-King-Jr-Way-APT-2-Oakland-CA-94612/2058455179_zpid/",
#     "https://www.zillow.com/b/1284-1286-7th-san-francisco-ca-9kpTZX/",
#     "https://www.zillow.com/b/123-Main-St-Los-Angeles-CA-90001/",
#     "https://www.zillow.com/b/456-Elm-St-Chicago-IL-60601/",
#     "https://www.zillow.com/b/789-Maple-St-New-York-NY-10001/"
# ]


for n in range(len(link_list)):

    driver.get(url=GOOGLE_FORMS_PAGE)
    time.sleep(6)

    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address_input.send_keys(address_list[n])
    time.sleep(1)
    price_input.send_keys(price_list[n])
    time.sleep(1)
    link_input.send_keys(link_list[n])
    time.sleep(1)
    submit.click()

