from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# ------------- Browser stays open -------------#
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery")
chrome_options.add_argument("--start-maximized")
# -----------------------------------------------#

USERNAME = "YOUR USERNAME HERE"
PASSWORD = "YOUR PASSWORD HERE"

INSTAGRAM_LOGIN_PAGE = "https://www.instagram.com/accounts/login/"
INSTAGRAM_ACCOUNT_FOLLOWERS = "python.hub"

SIMILAR_ACCOUNT = "basics.python"


class InstaFollower:

    def __init__(self):

        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.delete_all_cookies()
        self.driver.set_window_position(0, 0)

    def login(self):

        self.driver.get(url=INSTAGRAM_LOGIN_PAGE)
        time.sleep(12)
        username = self.driver.find_element(By.NAME, "username")
        username.click()
        username.send_keys(USERNAME)
        time.sleep(7)
        password = self.driver.find_element(By.NAME, "password")
        password.click()
        password.send_keys(PASSWORD)
        time.sleep(4)
        password.send_keys(Keys.ENTER)

    def find_followers(self):

        time.sleep(7)
        self.driver.get(url=f"https://www.instagram.com/{SIMILAR_ACCOUNT}/following")
        time.sleep(2)

        follow = self.driver.find_element(By.CSS_SELECTOR, 'div._aano')
        time.sleep(4)
        for i in range(2):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow)
            time.sleep(7)

        self.follow()

    def follow(self):

        follower_buttons = self.driver.find_elements(By.XPATH, "//button[contains(.,'Follow')]")
        for s in follower_buttons:
            if s.text == 'Follow':
                self.driver.execute_script("arguments[0].click();", s)
                time.sleep(1)


bot = InstaFollower()

bot.login()
bot.find_followers()
