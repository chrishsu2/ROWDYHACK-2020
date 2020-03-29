from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import os
def getLocation(locationObject):
    # should return zip code or relevant data. 
    return "78059"

linksToSearch = ["https://www.walmart.com/browse/ordering/product-availability/","https://www.target.com/b/find-it/-/N-tj7f8"]
driver = webdriver.Chrome("/Users/aaronfanous/Desktop/hackathonStuff/selDataDive/chromedriver")
# include forloop
driver.get(linksToSearch[0])
time.sleep(4) 
## 
driver.find_element_by_xpath("//*[@data-tl-id='nd-zip']").click()

for x in getLocation("placeholder"):
    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[5]/div[1]/div[2]/div[2]/div[1]/div/div[1]/input").send_keys(x)
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/div[5]/div[1]/div[2]/div[2]/div[1]/div/div[2]/button").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@data-tl-id='header-search-input']").send_keys("milk")
driver.find_element_by_xpath("//*[@data-tl-id='GlobalHeaderSearchbar-submit']").click()
time.sleep(3)
#input_field = driver.find_element_by_name("query")
#input_field.send_keys(getLocation("placeholder"))
#input_field.submit()
#  driver.find_element_by_xpath("//*[@data-tl-id='zipcode-form-submit-button']").click()



driver.quit()
#3 need to use xpath for the end portions. 
## vs using css selectors-- use xpath for everything that has attributes, 
# worry about headless after you have built the paths. 

"""dig through all the files and pull relevant information"""



