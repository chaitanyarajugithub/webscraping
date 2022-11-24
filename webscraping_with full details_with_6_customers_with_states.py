# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import time
import re


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    driver = webdriver.Chrome("/Users/chaitanya/Downloads/Selenium/Installers/Drivers/chromedriver")
    driver.maximize_window()
    companyname = []
    companylink = []
    cityop = []
    address = []
    phone = []
    fax = []
    emergencycall = []
    website = []
    email = []
    contactpersononedetails = []
    contactpersononename = []
    contactpersononetitle = []
    contactpersononeemail = []
    contactpersononemobile = []
    contactpersononedirectline = []
    contactpersontwodetails = []
    contactpersontwoname = []
    contactpersontwotitle = []
    contactpersontwoemail = []
    contactpersontwomobile = []
    contactpersontwodirectline = []
    contactpersonthreedetails = []
    contactpersonthreename = []
    contactpersonthreetitle = []
    contactpersonthreeemail = []
    contactpersonthreemobile = []
    contactpersonthreedirectline = []
    contactpersonfourdetails = []
    contactpersonfourname = []
    contactpersonfourtitle = []
    contactpersonfouremail = []
    contactpersonfourmobile = []
    contactpersonfourdirectline = []
    contactpersonfivedetails = []
    contactpersonfivename = []
    contactpersonfivetitle = []
    contactpersonfiveemail = []
    contactpersonfivemobile = []
    contactpersonfivedirectline = []
    contactpersonsixdetails = []
    contactpersonsixname = []
    contactpersonsixtitle = []
    contactpersonsixemail = []
    contactpersonsixmobile = []
    contactpersonsixdirectline = []

    driver.get("https://www.wcaworld.com/Account/Login")
    driver.find_element("css selector","#username").send_keys("awatacin")
    driver.find_element("css selector","#password").send_keys("AwAtAc$47$")
    driver.find_element("css selector","#login-form [type='submit']").send_keys(Keys.ENTER)
    time.sleep(4)
    driver.find_element("css selector","[href = '/Directory']").click()
    time.sleep(4)
    country = Select(driver.find_element('css selector', '#country'))
    print(len(country.options))
    # select by visible text
    for a in range(14, len(country.options)):
        print(a)
        country = Select(driver.find_element('css selector', '#country'))
        time.sleep(2)
        country.select_by_index(a)
        # country.select_by_visible_text("Angola")
        # get selected item with method first_selected_option
        countryname = country.first_selected_option
        # text method for selected option text
        print("Selected Country Name: " + countryname.text)
        countryfilename = countryname.text
        time.sleep(2)
        # identify element
        statel = driver.find_elements("css selector", "#statecity[disabled='disabled']")
        # get list size with len
        s = len(statel)
        # check condition, if list size > 0, element exists
        if (s == 0):
            state = Select(driver.find_element('css selector', '#statecity'))
            print(len(state.options))
            # select by visible text
            for b in range(1, len(state.options)):
                print(b)
                state = Select(driver.find_element('css selector', '#statecity'))
                time.sleep(2)
                state.select_by_index(b)
                # state.select_by_visible_text("California, CA")
                time.sleep(1)
                # autoload = driver.find_elements("css selector", ".animation_loading[style = 'display:none;']")
                # # get list size with len
                # s = len(autoload)
                # if (autoload == 1):
                #     # object of ActionChains
                #     autol = ActionChains(driver)
                #     # identify element
                #     m = driver.find_element("css selector", ".animation_loading[style = 'display:none;']")
                #     # hover over element
                #     autol.move_to_element(m).click().perform()
                #     time.sleep(4)

                city = Select(driver.find_element('css selector', '#city'))
                print(len(city.options))
                # select by visible text
                for c in range(1, len(city.options) - 1):
                    print(c)
                    city = Select(driver.find_element('css selector', '#city'))
                    time.sleep(2)
                    # country.select_by_index(a)
                    city.select_by_index(c)
                    # get selected item with method first_selected_option
                    cityname = city.first_selected_option
                    citynamea = cityname.text
                    # text method for selected option text
                    print("Selected City Name: " + cityname.text)
                    time.sleep(2)
                    driver.find_element("css selector", "#btn_search").click()
                    # Autoload results
                    autoloadresults(driver)
                    # driver.implicitly_wait(10)  # seconds
                    # content = driver.page_source
                    # soup = BeautifulSoup(content, "html.parser")
                    # print(len(soup.find_all('div', attrs={'class': 'profile_headline'})))
                    # print(len(soup.find_all('div', attrs={'class': 'profile_headline'})))
                    all_hey_elements = driver.find_elements("css selector", "li > a[href*='/directory/members']")
                    print(len(all_hey_elements))
                    if (len(all_hey_elements) > 0):
                        for x in range(0, len(all_hey_elements)):
                            url = all_hey_elements[x].get_attribute('href')
                            urlstate = urlvalid(url)
                            if (urlstate is not True):
                                print("test")
                                companyname.append(all_hey_elements[x].text)
                                companylink.append(all_hey_elements[x].get_attribute('href'))
                                address.append("Not the same Domine")
                                phone.append("Not the same Domine")
                                emergencycall.append("Not the same Domine")
                                website.append("Not the same Domine")
                                fax.append("Not the same Domine")
                                email.append("Not the same Domine")
                                contactpersononedetails.append("null")
                                contactpersontwodetails.append("null")
                                contactpersononename.append("null")
                                contactpersononetitle.append("null")
                                contactpersononeemail.append("null")
                                contactpersononemobile.append("null")
                                contactpersononedirectline.append("null")
                                contactpersontwoname.append("null")
                                contactpersontwotitle.append("null")
                                contactpersontwoemail.append("null")
                                contactpersontwomobile.append("null")
                                contactpersontwodirectline.append("null")
                                contactthreenull(a, contactpersonthreedetails, contactpersonthreename,
                                                 contactpersonthreetitle, contactpersonthreeemail,
                                                 contactpersonthreemobile,
                                                 contactpersonthreedirectline)
                                contactfournull(a, contactpersonfourdetails, contactpersonfourname,
                                                contactpersonfourtitle,
                                                contactpersonfouremail, contactpersonfourmobile,
                                                contactpersonfourdirectline)
                                contactfivenull(a, contactpersonfivedetails, contactpersonfivename,
                                                contactpersonfivetitle,
                                                contactpersonfiveemail, contactpersonfivemobile,
                                                contactpersonfivedirectline)
                                contactsixnull(a, contactpersonsixdetails, contactpersonsixname, contactpersonsixtitle,
                                               contactpersonsixemail, contactpersonsixmobile,
                                               contactpersonsixdirectline)
                                cityop.append(citynamea)
                            else:
                                print(all_hey_elements[x].text)
                                companyname.append(all_hey_elements[x].text)
                                print(all_hey_elements[x].get_attribute('href'))
                                companylink.append(all_hey_elements[x].get_attribute('href'))
                                all_hey_elements[x].click()
                                time.sleep(6)
                                driver_len = len(driver.window_handles)
                                if driver_len > 1:
                                    driver.switch_to.window(driver.window_handles[1])
                                time.sleep(1)
                                # get page source
                                content = driver.page_source
                                soup = BeautifulSoup(content, "html.parser")

                                print(len(soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=6)))
                                canlen = len(soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=6))
                                if (canlen > 0):
                                    candcount = 1
                                    for a in soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=6):
                                        print(candcount)
                                        if (candcount == 1):
                                            contactonepass(a, contactpersononedetails, contactpersononename,
                                                           contactpersononetitle, contactpersononeemail,
                                                           contactpersononemobile, contactpersononedirectline)
                                        elif (candcount == 2):
                                            contacttwopass(a, contactpersontwodetails, contactpersontwoname,
                                                           contactpersontwotitle, contactpersontwoemail,
                                                           contactpersontwomobile, contactpersontwodirectline)
                                        elif (candcount == 3):
                                            contactthreepass(a, contactpersonthreedetails, contactpersonthreename,
                                                             contactpersonthreetitle, contactpersonthreeemail,
                                                             contactpersonthreemobile, contactpersonthreedirectline)
                                        elif (candcount == 4):
                                            contactfourpass(a, contactpersonfourdetails, contactpersonfourname,
                                                            contactpersonfourtitle, contactpersonfouremail,
                                                            contactpersonfourmobile, contactpersonfourdirectline)
                                        elif (candcount == 5):
                                            contactfivepass(a, contactpersonfivedetails, contactpersonfivename,
                                                            contactpersonfivetitle, contactpersonfiveemail,
                                                            contactpersonfivemobile, contactpersonfivedirectline)
                                        elif (candcount == 6):
                                            contactsixpass(a, contactpersonsixdetails, contactpersonsixname,
                                                           contactpersonsixtitle, contactpersonsixemail,
                                                           contactpersonsixmobile, contactpersonsixdirectline)
                                        candcount = candcount + 1

                                    for x in range(canlen + 1, 7):
                                        if (x == 1):
                                            contactonenull(a, contactpersononedetails, contactpersononename,
                                                           contactpersononetitle, contactpersononeemail,
                                                           contactpersononemobile, contactpersononedirectline)
                                        elif (x == 2):
                                            contacttwonull(a, contactpersontwodetails, contactpersontwoname,
                                                           contactpersontwotitle, contactpersontwoemail,
                                                           contactpersontwomobile, contactpersontwodirectline)
                                        elif (x == 3):
                                            contactthreenull(a, contactpersonthreedetails, contactpersonthreename,
                                                             contactpersonthreetitle, contactpersonthreeemail,
                                                             contactpersonthreemobile,
                                                             contactpersonthreedirectline)
                                        elif (x == 4):
                                            contactfournull(a, contactpersonfourdetails, contactpersonfourname,
                                                            contactpersonfourtitle,
                                                            contactpersonfouremail, contactpersonfourmobile,
                                                            contactpersonfourdirectline)
                                        elif (x == 5):
                                            contactfivenull(a, contactpersonfivedetails, contactpersonfivename,
                                                            contactpersonfivetitle,
                                                            contactpersonfiveemail, contactpersonfivemobile,
                                                            contactpersonfivedirectline)
                                        elif (x == 6):
                                            contactsixnull(a, contactpersonsixdetails, contactpersonsixname,
                                                           contactpersonsixtitle,
                                                           contactpersonsixemail, contactpersonsixmobile,
                                                           contactpersonsixdirectline)
                                else:
                                    for x in range(1, 7):
                                        if (x == 1):
                                            contactonenull(a, contactpersononedetails, contactpersononename,
                                                           contactpersononetitle, contactpersononeemail,
                                                           contactpersononemobile, contactpersononedirectline)
                                        elif (x == 2):
                                            contacttwonull(a, contactpersontwodetails, contactpersontwoname,
                                                           contactpersontwotitle, contactpersontwoemail,
                                                           contactpersontwomobile, contactpersontwodirectline)
                                        elif (x == 3):
                                            contactthreenull(a, contactpersonthreedetails, contactpersonthreename,
                                                             contactpersonthreetitle, contactpersonthreeemail,
                                                             contactpersonthreemobile,
                                                             contactpersonthreedirectline)
                                        elif (x == 4):
                                            contactfournull(a, contactpersonfourdetails, contactpersonfourname,
                                                            contactpersonfourtitle,
                                                            contactpersonfouremail, contactpersonfourmobile,
                                                            contactpersonfourdirectline)
                                        elif (x == 5):
                                            contactfivenull(a, contactpersonfivedetails, contactpersonfivename,
                                                            contactpersonfivetitle,
                                                            contactpersonfiveemail, contactpersonfivemobile,
                                                            contactpersonfivedirectline)
                                        elif (x == 6):
                                            contactsixnull(a, contactpersonsixdetails, contactpersonsixname,
                                                           contactpersonsixtitle,
                                                           contactpersonsixemail, contactpersonsixmobile,
                                                           contactpersonsixdirectline)

                                try:
                                    # Get address text Code
                                    addre = soup.find('div', attrs={'class': 'profile_headline'},
                                                      text='Address:').parent
                                    addr = addre.find('span')
                                    print("Address: ", addr.text)
                                    address.append(addr.text)
                                    # print("Address: ",soup.find_parent())
                                except AttributeError:
                                    address.append("null")

                                cityop.append(citynamea)

                                try:
                                    # Get phone text Code
                                    phon = soup.find('div', attrs={'class': 'profile_label'}, text='Phone:').parent
                                    phn = phon.find('div', attrs={'class': 'profile_val'})
                                    print("Phone: ", phn.text)
                                    phone.append(phn.text)
                                except AttributeError:
                                    phone.append("null")

                                try:
                                    # Get emergencycall text Code
                                    emergencyc = soup.find('div', attrs={'class': 'profile_label'},
                                                           text='Emergency Call:').parent
                                    emer = emergencyc.find('div', attrs={'class': 'profile_val'})
                                    print("EMER: ", emer.text)
                                    emergencycall.append(emer.text)
                                except AttributeError:
                                    emergencycall.append("null")

                                try:
                                    # Get website text Code
                                    websi = soup.find('div', attrs={'class': 'profile_label'}, text='Website:').parent
                                    web = websi.find('div', attrs={'class': 'profile_val'})
                                    print("Web: ", web.text)
                                    website.append(web.text)
                                except AttributeError:
                                    website.append("null")

                                try:
                                    # Get fax text
                                    faxw = soup.find('div', attrs={'class': 'profile_label'}, text='Fax:').parent
                                    faxz = faxw.find('div', attrs={'class': 'profile_val'})
                                    print("Fax: ", faxz.text)
                                    fax.append(faxz.text)
                                except AttributeError:
                                    fax.append("null")

                                try:
                                    # Get Email text
                                    email_w = soup.find('div', attrs={'class': 'profile_label'}, text='Email:').parent
                                    email_x = email_w.find('div', attrs={'class': 'profile_val'})
                                    print("Fax: ", email_x.text)
                                    email.append(email_x.text)
                                except AttributeError:
                                    email.append("null")

                                time.sleep(2)
                                if driver_len > 1:
                                    driver.close()
                                    driver.switch_to.window(driver.window_handles[0])
                                else:
                                    driver.back()
                                    time.sleep(4)
                                    autoloadresults(driver)
                                # driver.back()
                                time.sleep(2)

                        # print(len(soup.find_all('a', href=re.compile('directory/members'), text=True)))
                        # for a in soup.find_all('a', href=re.compile('directory/members'), text=True):
                        #     print("Text: ", a.text)

                        time.sleep(2)
                        # for a in soup.find('.profile_headline', text="Address:"):
                        # name = a.find('div', attrs={'class': '_3wU53n'})
                        # price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
                        # rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
                        # products.append(name.text)
                        # prices.append(price.text)
                        # ratings.append(rating.text)
                        # print(soup.title)

                    else:
                        print("No results Found")
        else:
            city = Select(driver.find_element('css selector', '#city'))
            print(len(city.options))
            # select by visible text
            for c in range(1, len(city.options) - 1):
                print(c)
                city = Select(driver.find_element('css selector', '#city'))
                time.sleep(2)
                # country.select_by_index(a)
                city.select_by_index(c)
                # get selected item with method first_selected_option
                cityname = city.first_selected_option
                citynamea = cityname.text
                # text method for selected option text
                print("Selected City Name: " + cityname.text)
                time.sleep(2)
                driver.find_element("css selector", "#btn_search").click()
                time.sleep(5)
                # Autoload results
                autoloadresults(driver)
                # driver.implicitly_wait(10)  # seconds
                # content = driver.page_source
                # soup = BeautifulSoup(content, "html.parser")
                # print(len(soup.find_all('div', attrs={'class': 'profile_headline'})))
                # print(len(soup.find_all('div', attrs={'class': 'profile_headline'})))
                all_hey_elements = driver.find_elements("css selector", "li > a[href*='/directory/members']")
                print(len(all_hey_elements))
                if (len(all_hey_elements) > 0):
                    for x in range(0, len(all_hey_elements)):
                        url = all_hey_elements[x].get_attribute('href')
                        urlstate = urlvalid(url)
                        if (urlstate is not True):
                            print("test")
                            companyname.append(all_hey_elements[x].text)
                            companylink.append(all_hey_elements[x].get_attribute('href'))
                            address.append("Not the same Domine")
                            phone.append("Not the same Domine")
                            emergencycall.append("Not the same Domine")
                            website.append("Not the same Domine")
                            fax.append("Not the same Domine")
                            email.append("Not the same Domine")
                            contactpersononedetails.append("null")
                            contactpersontwodetails.append("null")
                            contactpersononename.append("null")
                            contactpersononetitle.append("null")
                            contactpersononeemail.append("null")
                            contactpersononemobile.append("null")
                            contactpersononedirectline.append("null")
                            contactpersontwoname.append("null")
                            contactpersontwotitle.append("null")
                            contactpersontwoemail.append("null")
                            contactpersontwomobile.append("null")
                            contactpersontwodirectline.append("null")
                            contactthreenull(a, contactpersonthreedetails, contactpersonthreename,
                                             contactpersonthreetitle, contactpersonthreeemail, contactpersonthreemobile,
                                             contactpersonthreedirectline)
                            contactfournull(a, contactpersonfourdetails, contactpersonfourname, contactpersonfourtitle,
                                            contactpersonfouremail, contactpersonfourmobile,
                                            contactpersonfourdirectline)
                            contactfivenull(a, contactpersonfivedetails, contactpersonfivename, contactpersonfivetitle,
                                            contactpersonfiveemail, contactpersonfivemobile,
                                            contactpersonfivedirectline)
                            contactsixnull(a, contactpersonsixdetails, contactpersonsixname, contactpersonsixtitle,
                                           contactpersonsixemail, contactpersonsixmobile, contactpersonsixdirectline)
                            cityop.append(citynamea)
                        else:
                            print(all_hey_elements[x].text)
                            companyname.append(all_hey_elements[x].text)
                            print(all_hey_elements[x].get_attribute('href'))
                            companylink.append(all_hey_elements[x].get_attribute('href'))
                            all_hey_elements[x].click()
                            time.sleep(6)
                            driver_len = len(driver.window_handles)
                            if driver_len > 1:
                                driver.switch_to.window(driver.window_handles[1])
                            time.sleep(1)
                            # get page source
                            content = driver.page_source
                            soup = BeautifulSoup(content, "html.parser")

                            print(len(soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=6)))
                            canlen = len(soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=6))
                            if (canlen > 0):
                                candcount = 1
                                for a in soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=6):
                                    print(candcount)
                                    if (candcount == 1):
                                        contactonepass(a, contactpersononedetails, contactpersononename,
                                                       contactpersononetitle, contactpersononeemail,
                                                       contactpersononemobile, contactpersononedirectline)
                                    elif (candcount == 2):
                                        contacttwopass(a, contactpersontwodetails, contactpersontwoname,
                                                       contactpersontwotitle, contactpersontwoemail,
                                                       contactpersontwomobile, contactpersontwodirectline)
                                    elif (candcount == 3):
                                        contactthreepass(a, contactpersonthreedetails, contactpersonthreename,
                                                         contactpersonthreetitle, contactpersonthreeemail,
                                                         contactpersonthreemobile, contactpersonthreedirectline)
                                    elif (candcount == 4):
                                        contactfourpass(a, contactpersonfourdetails, contactpersonfourname,
                                                        contactpersonfourtitle, contactpersonfouremail,
                                                        contactpersonfourmobile, contactpersonfourdirectline)
                                    elif (candcount == 5):
                                        contactfivepass(a, contactpersonfivedetails, contactpersonfivename,
                                                        contactpersonfivetitle, contactpersonfiveemail,
                                                        contactpersonfivemobile, contactpersonfivedirectline)
                                    elif (candcount == 6):
                                        contactsixpass(a, contactpersonsixdetails, contactpersonsixname,
                                                       contactpersonsixtitle, contactpersonsixemail,
                                                       contactpersonsixmobile, contactpersonsixdirectline)
                                    candcount = candcount + 1

                                for x in range(canlen+1, 7):
                                    if (x == 1):
                                        contactonenull(a, contactpersononedetails, contactpersononename,
                                                       contactpersononetitle, contactpersononeemail,
                                                       contactpersononemobile, contactpersononedirectline)
                                    elif (x == 2):
                                        contacttwonull(a, contactpersontwodetails, contactpersontwoname,
                                                       contactpersontwotitle, contactpersontwoemail,
                                                       contactpersontwomobile, contactpersontwodirectline)
                                    elif (x == 3):
                                        contactthreenull(a, contactpersonthreedetails, contactpersonthreename,
                                                         contactpersonthreetitle, contactpersonthreeemail,
                                                         contactpersonthreemobile,
                                                         contactpersonthreedirectline)
                                    elif (x == 4):
                                        contactfournull(a, contactpersonfourdetails, contactpersonfourname,
                                                        contactpersonfourtitle,
                                                        contactpersonfouremail, contactpersonfourmobile,
                                                        contactpersonfourdirectline)
                                    elif (x == 5):
                                        contactfivenull(a, contactpersonfivedetails, contactpersonfivename,
                                                        contactpersonfivetitle,
                                                        contactpersonfiveemail, contactpersonfivemobile,
                                                        contactpersonfivedirectline)
                                    elif (x == 6):
                                        contactsixnull(a, contactpersonsixdetails, contactpersonsixname,
                                                       contactpersonsixtitle,
                                                       contactpersonsixemail, contactpersonsixmobile,
                                                       contactpersonsixdirectline)
                            else:
                                for x in range(1, 7):
                                    if (x == 1):
                                        contactonenull(a, contactpersononedetails, contactpersononename,
                                                       contactpersononetitle, contactpersononeemail,
                                                       contactpersononemobile, contactpersononedirectline)
                                    elif (x == 2):
                                        contacttwonull(a, contactpersontwodetails, contactpersontwoname,
                                                       contactpersontwotitle, contactpersontwoemail,
                                                       contactpersontwomobile, contactpersontwodirectline)
                                    elif (x == 3):
                                        contactthreenull(a, contactpersonthreedetails, contactpersonthreename,
                                                         contactpersonthreetitle, contactpersonthreeemail,
                                                         contactpersonthreemobile,
                                                         contactpersonthreedirectline)
                                    elif (x == 4):
                                        contactfournull(a, contactpersonfourdetails, contactpersonfourname,
                                                        contactpersonfourtitle,
                                                        contactpersonfouremail, contactpersonfourmobile,
                                                        contactpersonfourdirectline)
                                    elif (x == 5):
                                        contactfivenull(a, contactpersonfivedetails, contactpersonfivename,
                                                        contactpersonfivetitle,
                                                        contactpersonfiveemail, contactpersonfivemobile,
                                                        contactpersonfivedirectline)
                                    elif (x == 6):
                                        contactsixnull(a, contactpersonsixdetails, contactpersonsixname,
                                                       contactpersonsixtitle,
                                                       contactpersonsixemail, contactpersonsixmobile,
                                                       contactpersonsixdirectline)

                            try:
                                # Get address text Code
                                addre = soup.find('div', attrs={'class': 'profile_headline'}, text='Address:').parent
                                addr = addre.find('span')
                                print("Address: ", addr.text)
                                address.append(addr.text)
                                # print("Address: ",soup.find_parent())
                            except AttributeError:
                                address.append("null")

                            cityop.append(citynamea)

                            try:
                                # Get phone text Code
                                phon = soup.find('div', attrs={'class': 'profile_label'}, text='Phone:').parent
                                phn = phon.find('div',attrs={'class': 'profile_val'})
                                print("Phone: ", phn.text)
                                phone.append(phn.text)
                            except AttributeError:
                                phone.append("null")

                            try:
                                # Get emergencycall text Code
                                emergencyc = soup.find('div', attrs={'class': 'profile_label'}, text='Emergency Call:').parent
                                emer = emergencyc.find('div',attrs={'class': 'profile_val'})
                                print("EMER: ", emer.text)
                                emergencycall.append(emer.text)
                            except AttributeError:
                                emergencycall.append("null")

                            try:
                                # Get website text Code
                                websi = soup.find('div', attrs={'class': 'profile_label'}, text='Website:').parent
                                web = websi.find('div',attrs={'class': 'profile_val'})
                                print("Web: ", web.text)
                                website.append(web.text)
                            except AttributeError:
                                website.append("null")

                            try:
                                # Get fax text
                                faxw = soup.find('div', attrs={'class': 'profile_label'}, text='Fax:').parent
                                faxz = faxw.find('div', attrs={'class': 'profile_val'})
                                print("Fax: ", faxz.text)
                                fax.append(faxz.text)
                            except AttributeError:
                                fax.append("null")

                            try:
                                # Get Email text
                                email_w = soup.find('div', attrs={'class': 'profile_label'}, text='Email:').parent
                                email_x = email_w.find('div', attrs={'class': 'profile_val'})
                                print("Fax: ", email_x.text)
                                email.append(email_x.text)
                            except AttributeError:
                                email.append("null")

                            time.sleep(2)
                            if driver_len > 1:
                                driver.close()
                                driver.switch_to.window(driver.window_handles[0])
                            else:
                                driver.back()
                                time.sleep(4)
                                autoloadresults(driver)
                            # driver.back()
                            time.sleep(2)

                    # print(len(soup.find_all('a', href=re.compile('directory/members'), text=True)))
                    # for a in soup.find_all('a', href=re.compile('directory/members'), text=True):
                    #     print("Text: ", a.text)

                    time.sleep(2)
                    # for a in soup.find('.profile_headline', text="Address:"):
                    # name = a.find('div', attrs={'class': '_3wU53n'})
                    # price = a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
                    # rating = a.find('div', attrs={'class': 'hGSR34 _2beYZw'})
                    # products.append(name.text)
                    # prices.append(price.text)
                    # ratings.append(rating.text)
                    # print(soup.title)

                else:
                    print("No results Found")
        df = pd.DataFrame({'Company Name': companyname, 'Company Link': companylink, 'City': cityop, 'Address': address, 'Phone': phone,
                           'Emergency Ph': emergencycall, 'Web Site': website, 'Fax': fax, 'Email': email,
                           'Contact Person1 Full Details': contactpersononedetails, 'Contact Person1 Name': contactpersononename, 'Contact Person1 Title': contactpersononetitle,
                           'Contact person1 Email': contactpersononeemail, 'Contact Person1 Mobile': contactpersononemobile, 'Contact Person1 DirectLine': contactpersononedirectline,'Contact Person2 Full Details': contactpersontwodetails, 'Contact Person2 Name': contactpersontwoname,
                           'Contact Person2 Title': contactpersontwotitle, 'Contact person2 Email': contactpersontwoemail, 'Contact Person2 Mobile': contactpersontwomobile, 'Contact Person2 DirectLine': contactpersontwodirectline,'Contact Person3 Full Details': contactpersonthreedetails, 'Contact Person3 Name': contactpersonthreename, 'Contact Person3 Title': contactpersonthreetitle,
                           'Contact person3 Email': contactpersonthreeemail, 'Contact Person3 Mobile': contactpersonthreemobile, 'Contact Person3 DirectLine': contactpersonthreedirectline, 'Contact Person4 Full Details': contactpersonfourdetails, 'Contact Person4 Name': contactpersonfourname, 'Contact Person4 Title': contactpersonfourtitle,
                           'Contact person4 Email': contactpersonfouremail, 'Contact Person4 Mobile': contactpersonfourmobile, 'Contact Person4 DirectLine': contactpersonfourdirectline,'Contact Person5 Full Details': contactpersonfivedetails, 'Contact Person5 Name': contactpersonfivename, 'Contact Person5 Title': contactpersonfivetitle,
                           'Contact person5 Email': contactpersonfiveemail, 'Contact Person5 Mobile':contactpersonfivemobile, 'Contact Person5 DirectLine': contactpersonfivedirectline,'Contact Person6 Full Details': contactpersonsixdetails, 'Contact Person6 Name': contactpersonsixname, 'Contact Person6 Title': contactpersonsixtitle,
                           'Contact person6 Email': contactpersonsixemail, 'Contact Person6 Mobile':contactpersonsixmobile, 'Contact Person6 DirectLine': contactpersonsixdirectline})
        df.to_csv('files' + '/' +countryfilename+'.csv', index=False, encoding='utf-8')
        companyname = []
        companylink = []
        cityop = []
        address = []
        phone = []
        fax = []
        emergencycall = []
        website = []
        email = []
        contactpersononedetails = []
        contactpersontwodetails = []
        contactpersononename = []
        contactpersononetitle = []
        contactpersononeemail = []
        contactpersononemobile = []
        contactpersononedirectline = []
        contactpersontwoname = []
        contactpersontwotitle = []
        contactpersontwoemail = []
        contactpersontwomobile = []
        contactpersontwodirectline = []
        contactpersonthreedetails = []
        contactpersonthreename = []
        contactpersonthreetitle = []
        contactpersonthreeemail = []
        contactpersonthreemobile = []
        contactpersonthreedirectline = []
        contactpersonfourdetails = []
        contactpersonfourname = []
        contactpersonfourtitle = []
        contactpersonfouremail = []
        contactpersonfourmobile = []
        contactpersonfourdirectline = []
        contactpersonfivedetails = []
        contactpersonfivename = []
        contactpersonfivetitle = []
        contactpersonfiveemail = []
        contactpersonfivemobile = []
        contactpersonfivedirectline = []
        contactpersonsixdetails = []
        contactpersonsixname = []
        contactpersonsixtitle = []
        contactpersonsixemail = []
        contactpersonsixmobile = []
        contactpersonsixdirectline = []
# Press the green button in the gutter to run the script.


def getdata(a, text):
    try:
        name = a.findNext('div', attrs={'class': 'profile_label'}, text=text).parent
        chai = name.find('div', attrs={'class': 'profile_val'})
        return chai.text
    except AttributeError:
        return "null"


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


def urlvalid(url):
    if "wcaworld" in url:
        print("wcaworld")
        return True
    elif "wcaprojects" in url:
        print("wcaprojects")
        return True
    elif "wcaecommerce" in url:
        print("wcaecommerce")
        return True
    elif "elitegln" in url:
        print("elitegln")
        return True
    elif "globalaffinityalliance" in url:
        print("globalaffinityalliance")
        return True
    elif "lognetglobal" in url:
        print("lognetglobal")
        return True
    else:
        print("false")
        return False


def contactonepass(a,contactpersononedetails,contactpersononename,contactpersononetitle,contactpersononeemail,contactpersononemobile,contactpersononedirectline):
    name = a.text
    print(name.strip())
    contactpersononedetails.append(name.strip())
    print(getdata(a, 'Name:'))
    contactpersononename.append(getdata(a, 'Name:').lstrip())
    print(getdata(a, 'Title:'))
    contactpersononetitle.append(getdata(a, 'Title:'))
    print(getdata(a, 'Email'))
    contactpersononeemail.append(getdata(a, 'Email'))
    print(getdata(a, 'Mobile'))
    contactpersononemobile.append(getdata(a, 'Mobile'))
    print(getdata(a, 'Direct Line'))
    contactpersononedirectline.append(getdata(a, 'Direct Line'))


def contactonenull(a,contactpersononedetails,contactpersononename,contactpersononetitle,contactpersononeemail,contactpersononemobile,contactpersononedirectline):
    contactpersononedetails.append("null")
    contactpersononename.append("null")
    contactpersononetitle.append("null")
    contactpersononeemail.append("null")
    contactpersononemobile.append("null")
    contactpersononedirectline.append("null")


def contacttwopass(a,contactpersontwodetails,contactpersontwoname,contactpersontwotitle,contactpersontwoemail,contactpersontwomobile,contactpersontwodirectline):
    name = a.text
    print(name.strip())
    contactpersontwodetails.append(name.strip())
    print(getdata(a, 'Name:'))
    contactpersontwoname.append(getdata(a, 'Name:').lstrip())
    print(getdata(a, 'Title:'))
    contactpersontwotitle.append(getdata(a, 'Title:'))
    print(getdata(a, 'Email'))
    contactpersontwoemail.append(getdata(a, 'Email'))
    print(getdata(a, 'Mobile'))
    contactpersontwomobile.append(getdata(a, 'Mobile'))
    print(getdata(a, 'Direct Line'))
    contactpersontwodirectline.append(getdata(a, 'Direct Line'))


def contacttwonull(a,contactpersontwodetails,contactpersontwoname,contactpersontwotitle,contactpersontwoemail,contactpersontwomobile,contactpersontwodirectline):
    contactpersontwodetails.append("null")
    contactpersontwoname.append("null")
    contactpersontwotitle.append("null")
    contactpersontwoemail.append("null")
    contactpersontwomobile.append("null")
    contactpersontwodirectline.append("null")


def contactthreepass(a,contactpersonthreedetails,contactpersonthreename,contactpersonthreetitle,contactpersonthreeemail,contactpersonthreemobile,contactpersonthreedirectline):
    name = a.text
    print(name.strip())
    contactpersonthreedetails.append(name.strip())
    print(getdata(a, 'Name:'))
    contactpersonthreename.append(getdata(a, 'Name:').lstrip())
    print(getdata(a, 'Title:'))
    contactpersonthreetitle.append(getdata(a, 'Title:'))
    print(getdata(a, 'Email'))
    contactpersonthreeemail.append(getdata(a, 'Email'))
    print(getdata(a, 'Mobile'))
    contactpersonthreemobile.append(getdata(a, 'Mobile'))
    print(getdata(a, 'Direct Line'))
    contactpersonthreedirectline.append(getdata(a, 'Direct Line'))


def contactthreenull(a,contactpersonthreedetails,contactpersonthreename,contactpersonthreetitle,contactpersonthreeemail,contactpersonthreemobile,contactpersonthreedirectline):
    contactpersonthreedetails.append("null")
    contactpersonthreename.append("null")
    contactpersonthreetitle.append("null")
    contactpersonthreeemail.append("null")
    contactpersonthreemobile.append("null")
    contactpersonthreedirectline.append("null")


def contactfourpass(a,contactpersonfourdetails,contactpersonfourname,contactpersonfourtitle,contactpersonfouremail,contactpersonfourmobile,contactpersonfourdirectline):
    name = a.text
    print(name.strip())
    contactpersonfourdetails.append(name.strip())
    print(getdata(a, 'Name:'))
    contactpersonfourname.append(getdata(a, 'Name:').lstrip())
    print(getdata(a, 'Title:'))
    contactpersonfourtitle.append(getdata(a, 'Title:'))
    print(getdata(a, 'Email'))
    contactpersonfouremail.append(getdata(a, 'Email'))
    print(getdata(a, 'Mobile'))
    contactpersonfourmobile.append(getdata(a, 'Mobile'))
    print(getdata(a, 'Direct Line'))
    contactpersonfourdirectline.append(getdata(a, 'Direct Line'))


def contactfournull(a,contactpersonfourdetails,contactpersonfourname,contactpersonfourtitle,contactpersonfouremail,contactpersonfourmobile,contactpersonfourdirectline):
    contactpersonfourdetails.append("null")
    contactpersonfourname.append("null")
    contactpersonfourtitle.append("null")
    contactpersonfouremail.append("null")
    contactpersonfourmobile.append("null")
    contactpersonfourdirectline.append("null")


def contactfivepass(a,contactpersonfivedetails,contactpersonfivename,contactpersonfivetitle,contactpersonfiveemail,contactpersonfivemobile,contactpersonfivedirectline):
    name = a.text
    print(name.strip())
    contactpersonfivedetails.append(name.strip())
    print(getdata(a, 'Name:'))
    contactpersonfivename.append(getdata(a, 'Name:').lstrip())
    print(getdata(a, 'Title:'))
    contactpersonfivetitle.append(getdata(a, 'Title:'))
    print(getdata(a, 'Email'))
    contactpersonfiveemail.append(getdata(a, 'Email'))
    print(getdata(a, 'Mobile'))
    contactpersonfivemobile.append(getdata(a, 'Mobile'))
    print(getdata(a, 'Direct Line'))
    contactpersonfivedirectline.append(getdata(a, 'Direct Line'))


def contactfivenull(a,contactpersonfivedetails,contactpersonfivename,contactpersonfivetitle,contactpersonfiveemail,contactpersonfivemobile,contactpersonfivedirectline):
    contactpersonfivedetails.append("null")
    contactpersonfivename.append("null")
    contactpersonfivetitle.append("null")
    contactpersonfiveemail.append("null")
    contactpersonfivemobile.append("null")
    contactpersonfivedirectline.append("null")


def contactsixpass(a,contactpersonsixdetails,contactpersonsixname,contactpersonsixtitle,contactpersonsixemail,contactpersonsixmobile,contactpersonsixdirectline):
    name = a.text
    print(name.strip())
    contactpersonsixdetails.append(name.strip())
    print(getdata(a, 'Name:'))
    contactpersonsixname.append(getdata(a, 'Name:').lstrip())
    print(getdata(a, 'Title:'))
    contactpersonsixtitle.append(getdata(a, 'Title:'))
    print(getdata(a, 'Email'))
    contactpersonsixemail.append(getdata(a, 'Email'))
    print(getdata(a, 'Mobile'))
    contactpersonsixmobile.append(getdata(a, 'Mobile'))
    print(getdata(a, 'Direct Line'))
    contactpersonsixdirectline.append(getdata(a, 'Direct Line'))


def contactsixnull(a,contactpersonsixdetails,contactpersonsixname,contactpersonsixtitle,contactpersonsixemail,contactpersonsixmobile,contactpersonsixdirectline):
    contactpersonsixdetails.append("null")
    contactpersonsixname.append("null")
    contactpersonsixtitle.append("null")
    contactpersonsixemail.append("null")
    contactpersonsixmobile.append("null")
    contactpersonsixdirectline.append("null")


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
