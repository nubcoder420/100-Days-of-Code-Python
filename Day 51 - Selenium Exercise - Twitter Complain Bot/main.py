from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#------------- Browser stays open -------------#
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#-----------------------------------------------#


TWITTER_EMAIL = "TWITTER USERNAME"
TWITTER_PASSWORD = "TWITTER PASSWORD"

PROMISED_DOWN = 200
PROMISED_UP = 200

class InternetSpeedTwitterBot:

    def __init__(self):

        self.driver = webdriver.Chrome(options=chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net/")
        time.sleep(5)
        self.driver.find_element(By.CLASS_NAME, "start-text").click()
        time.sleep(45)
        download_speed = bot.driver.find_element(By.CLASS_NAME, "download-speed").text
        upload_speed = bot.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"down: {download_speed}")
        print(f"up: {upload_speed}")
        return download_speed, upload_speed

    def tweet_at_provider(self, download_speed, upload_speed):

        self.driver.get(url="https://twitter.com/")
        time.sleep(5)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span').click()
        time.sleep(3)
        login = self.driver.find_element(By.NAME, "text")
        login.send_keys(TWITTER_EMAIL)
        time.sleep(1)
        login.send_keys(Keys.ENTER)
        time.sleep(2)
        pw = self.driver.find_element(By.NAME, "password")
        time.sleep(2)
        pw.send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        pw.send_keys(Keys.ENTER)
        time.sleep(18)

        self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block").click()
        time.sleep(2)
        tweet = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        time.sleep(1)
        tweet.send_keys(
            f"Internet Download Speed: {download_speed} Mbps\n"
            f"Internet Upload Speed: {upload_speed} Mbps"
        )
        time.sleep(5.2)
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div').click()
        print("Tweet Success")


bot = InternetSpeedTwitterBot()

download_speed, upload_speed = bot.get_internet_speed()
bot.tweet_at_provider(download_speed, upload_speed)

