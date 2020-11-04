# Login with LinkedIn using selenium

from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://www.linkedin.com/login")    # open link in firefox

auth = driver.find_element_by_id('username')
auth.send_keys("atulpunde970@gmail.com")

auth = driver.find_element_by_id('password')
auth.send_keys('atulpunde1997')

# Pass username and password
auth.submit()

# Wait for some time
time.sleep(14)
driver.close()

# Just exploring selenium for project study.
