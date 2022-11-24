# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import time

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    driver = webdriver.Chrome("/Users/chaitanya/Downloads/Selenium/Installers/Drivers/chromedriver")
    driver.maximize_window()
    products = []  # List to store name of the product
    prices = []  # List to store price of the product
    ratings = []  # List to store rating of the product
    driver.get("https://www.wcaworld.com/Account/Login")
    driver.find_element("css selector","#username").send_keys("awatacin")
    driver.find_element("css selector","#password").send_keys("AwAtAc$47$")
    driver.find_element("css selector","#login-form [type='submit']").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element("css selector","[href = '/Directory']").click()
    time.sleep(4)
    select = Select(driver.find_element('css selector','#country'))
    # select by visible text
    select.select_by_visible_text('United Kingdom')
    time.sleep(4)
    driver.find_element("css selector","#btn_search").click()
    time.sleep(4)
    autoloadresults(driver)
    # # get list size with len
    # autole = driver.find_elements("css selector", ".loadmore[href='#']")
    # s = len(autole)
    # # check condition, if list size > 0, element exists
    # if (s > 0):
    #     autol = ActionChains(driver)
    #     # identify element
    #     autolea = driver.find_elements("css selector", ".loadmore[href = '#'][style = 'display: none;']")
    #     t = len(autolea)
    #     print(t)
    #     print("Entried If")
    #     while (len(driver.find_elements("css selector", ".loadmore[href='#']")) != len(driver.find_elements("css selector", ".loadmore[href = '#'][style = 'display: none;']"))):
    #         print("Entried while")
    #         autolew = driver.find_elements("css selector", ".loadmore[href='#']")
    #         h = len(autolew)
    #         m = autolew[h-1]
    #         # hover over element
    #         autol.move_to_element(m).click().perform()
    #         time.sleep(5)
    # else:
    #     print("Element does not exist")
    time.sleep(5)
    driver.implicitly_wait(10)  # seconds
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    print(soup.title)
# Press the green button in the gutter to run the script.


def autoloadresults(driver):
    # get list size with len
    autole = driver.find_elements("css selector", ".loadmore[href='#']")
    s = len(autole)
    # check condition, if list size > 0, element exists
    if (s > 0):
        autol = ActionChains(driver)
        # identify element
        autolea = driver.find_elements("css selector", ".loadmore[href = '#'][style = 'display: none;']")
        t = len(autolea)
        print(t)
        print("Entried If")
        while (len(driver.find_elements("css selector", ".loadmore[href='#']")) != len(
                driver.find_elements("css selector", ".loadmore[href = '#'][style = 'display: none;']"))):
            print("Entried while")
            autolew = driver.find_elements("css selector", ".loadmore[href='#']")
            h = len(autolew)
            m = autolew[h - 1]
            # hover over element
            autol.move_to_element(m).click().perform()
            time.sleep(5)


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
