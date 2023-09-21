from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#------------- Browser stays open -------------#
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
#-----------------------------------------------#

#--------------- LOGIN CREDENTIALS -----------------#
EMAIL = "YOUR EMAIL HERE"
PASSWORD = "YOUR PASSWORD HERE"

#--------------- LINKEDIN LINK -----------------#
URL = "https://www.linkedin.com/jobs/search/?currentJobId=3698138368&f_AL=true&f_BE=&f_C=&f_CM=&f_CR=&f_CT=&f_E=2&f_EA=&f_EL=&f_ES=&f_ET=&f_F=&f_FCE=&f_GC=&f_I=&f_JC=&f_JIYN=&f_JT=&f_LF=&f_PP=&f_SAL=&f_SB=&f_SB2=&f_SB3=&f_T=&f_TP=&f_TPR=&f_WT=2&keywords=python%20developer&latLong=&location=Quezon%20City&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true&sortBy="

driver = webdriver.Chrome(options=chrome_options)

driver.get(url=URL)
time.sleep(5)

sign_in = driver.find_element(By.CLASS_NAME, "cta-modal__primary-btn")
time.sleep(5)
sign_in.click()


username = driver.find_element(By.ID, "username")
username.send_keys(EMAIL)
time.sleep(1)

password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
time.sleep(1)

submit = driver.find_element(By.CLASS_NAME, "btn__primary--large")
submit.click()
time.sleep(10)

save_job = driver.find_element(By.CLASS_NAME, "jobs-save-button")
save_job.click()
time.sleep(10)







