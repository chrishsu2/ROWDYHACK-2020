from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


def getLocation(locationObject):
    # should return zip code or relevant data.
    return "78059"

def searchWalmartStore(driver, zipcode, query):
    # Selects store
    selectStore1 = driver.find_element_by_xpath('//*[@id="store-list"]/div/ol/li[1]/div/div[2]/span[2]/a[1]/span')
    selectStore1.click()
    selectStore2 = driver.find_element_by_xpath('//*[@id="store-finder-results"]/div/div/div[2]/div[1]/div/div/button')
    selectStore2.click()

    searchField = driver.find_element_by_xpath('//*[@id="store-finder-results"]/div/div/div[4]/form/div/div[1]/span/div/label/input')
    searchField.clear()
    searchField.send_keys(query)
    searchField.submit()

def scrapeWalmartResults(driver, numItemsToScrape):
    grid = driver.find_element_by_xpath('//*[@id="content"]/div[2]/section[2]/div[3]/div/div[2]/div/div[2]/ul')
    items = grid.find_elements_by_xpath(".//div[contains(@class, 'search-result-wrapper')]")
    print("Number of results: " + str(len(items)))
    for i in range(0, min(numItemsToScrape,24)):
        xpath = '//a[@tabindex="0"]'
        link = items[i].find_element_by_xpath(xpath)
        print(i)
        print(link.get_attribute("href"))


def main():
    linksToSearch = ["https://www.walmart.com/browse/ordering/product-availability/","https://www.target.com/b/find-it/-/N-tj7f8"]
    #  driver = webdriver.Chrome("/Users/aaronfanous/Desktop/hackathonStuff/selDataDive/chromedriver") #  add webdriver to PATH instead
    driver = webdriver.Chrome()  # replace with "with webdriver.Chrome() as driver" when ready for production

    driver.get("https://www.walmart.com/store/finder?location="+getLocation("placeholder"))
    time.sleep(1)
    searchWalmartStore(driver, getLocation("PLACEHOLDER"), "bread")
    time.sleep(1)
    scrapeWalmartResults(driver, 10)  # max results from walmart: 24 per page
    input("before quit!")
    driver.quit()



main()


