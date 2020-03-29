from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


def getLocation(locationObject):
    # should return zip code or relevant data.
    return "78059"

def searchStore(driver, storeType, zipcode, query):
    if storeType == "Walmart":
        # Selects store
        selectStore1 = driver.find_element_by_xpath('//*[@id="store-list"]/div/ol/li[1]/div/div[2]/span[2]/a[1]/span')
        print(selectStore1.location)
        selectStore1.click()
        selectStore2 = driver.find_element_by_xpath('//*[@id="store-finder-results"]/div/div/div[2]/div[1]/div/div/button')
        selectStore2.click()

        searchField = driver.find_element_by_xpath('//*[@id="store-finder-results"]/div/div/div[4]/form/div/div[1]/span/div/label/input')
        searchField.clear()
        searchField.send_keys(query)
        input("0 search store")
        searchField.submit()


def main():
    linksToSearch = ["https://www.walmart.com/browse/ordering/product-availability/","https://www.target.com/b/find-it/-/N-tj7f8"]
    #  driver = webdriver.Chrome("/Users/aaronfanous/Desktop/hackathonStuff/selDataDive/chromedriver") #  add webdriver to PATH instead
    driver = webdriver.Chrome()  # replace with "with webdriver.Chrome() as driver" when ready for production

    driver.get("https://www.walmart.com/store/finder?location="+getLocation("placeholder"))
    time.sleep(1)
    searchStore(driver, "Walmart", getLocation("PLACEHOLDER"), "bread")
    time.sleep(1)
    input("before quit!")
    driver.quit()



main()


