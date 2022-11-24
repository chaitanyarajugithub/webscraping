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
    contactpersononename = []
    contactpersononetitle = []
    contactpersononeemail = []
    contactpersontwoname = []
    contactpersontwotitle = []
    contactpersontwoemail = []

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
    for a in range(1, len(country.options)):
        print(a)
        country = Select(driver.find_element('css selector', '#country'))
        time.sleep(2)
        country.select_by_index(a)
        # country.select_by_visible_text("United States of America")
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
                    # text method for selected option text
                    print("Selected City Name: " + cityname.text)
                    time.sleep(2)
                    driver.find_element("css selector", "#btn_search").click()
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
                # text method for selected option text
                print("Selected City Name: " + cityname.text)
                time.sleep(2)
                driver.find_element("css selector", "#btn_search").click()
                time.sleep(4)

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
                        if ("www.wcaworld.com" not in url):
                            print("test")
                            companyname.append(all_hey_elements[x].text)
                            companylink.append(all_hey_elements[x].get_attribute('href'))
                            address.append("Not the same Domine")
                            phone.append("Not the same Domine")
                            emergencycall.append("Not the same Domine")
                            website.append("Not the same Domine")
                            fax.append("Not the same Domine")
                            email.append("Not the same Domine")
                            contactpersononename.append("null")
                            contactpersononetitle.append("null")
                            contactpersononeemail.append("null")
                            contactpersontwoname.append("null")
                            contactpersontwotitle.append("null")
                            contactpersontwoemail.append("null")
                            cityop.append(cityname.text)
                        else:
                            print(all_hey_elements[x].text)
                            companyname.append(all_hey_elements[x].text)
                            print(all_hey_elements[x].get_attribute('href'))
                            companylink.append(all_hey_elements[x].get_attribute('href'))
                            all_hey_elements[x].click()
                            time.sleep(4)
                            # get page source
                            content = driver.page_source
                            soup = BeautifulSoup(content, "html.parser")

                            print(len(soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=2)))
                            canlen = len(soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=2))
                            if (canlen == 2):
                                candcount = 1
                                for a in soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=2):
                                    print(candcount)
                                    if (candcount == 1):
                                        # name = a.findNext('div', attrs={'class': 'profile_label'}, text='Name:').parent
                                        # print(name)
                                        # chai = name.find('div', attrs={'class': 'profile_val'})
                                        # print(chai.text)
                                        print(getdata(a, 'Name:'))
                                        contactpersononename.append(getdata(a, 'Name:').lstrip())
                                        print(getdata(a, 'Title:'))
                                        contactpersononetitle.append(getdata(a, 'Title:'))
                                        print(getdata(a, 'Email'))
                                        contactpersononeemail.append(getdata(a, 'Email'))
                                        print(getdata(a, 'Mobile'))
                                    elif (candcount == 2):
                                        print(getdata(a, 'Name:'))
                                        contactpersontwoname.append(getdata(a, 'Name:').lstrip())
                                        print(getdata(a, 'Title:'))
                                        contactpersontwotitle.append(getdata(a, 'Title:'))
                                        print(getdata(a, 'Email'))
                                        contactpersontwoemail.append(getdata(a, 'Email'))
                                        print(getdata(a, 'Mobile'))
                                    candcount = candcount + 1
                            elif (canlen == 1):
                                for a in soup.find_all('div', attrs={'class': 'contactperson_info'}, limit=1):
                                    print(getdata(a, 'Name:'))
                                    contactpersononename.append(getdata(a, 'Name:'))
                                    print(getdata(a, 'Title:'))
                                    contactpersononetitle.append(getdata(a, 'Title:'))
                                    print(getdata(a, 'Email'))
                                    contactpersononeemail.append(getdata(a, 'Email'))
                                    #Contact person 2 null
                                    contactpersontwoname.append("null")
                                    contactpersontwotitle.append("null")
                                    contactpersontwoemail.append("null")

                            try:
                                # Get address text Code
                                addre = soup.find('div', attrs={'class': 'profile_headline'}, text='Address:').parent
                                addr = addre.find('span')
                                print("Address: ", addr.text)
                                address.append(addr.text)
                                cityop.append(cityname.text)
                                # print("Address: ",soup.find_parent())
                            except AttributeError:
                                address.append("null")

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
                            driver.back()
                            time.sleep(2)

                    # print(len(soup.find_all('a', href=re.compile('directory/members'), text=True)))
                    # for a in soup.find_all('a', href=re.compile('directory/members'), text=True):
                    #     print("Text: ", a.text)




                    time.sleep(5)
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
                           'Contact Person1 Name': contactpersononename, 'Contact Person1 Title': contactpersononetitle,
                           'Contact person1 Email': contactpersononeemail, 'Contact Person2 Name': contactpersontwoname,
                           'Contact Person2 Title': contactpersontwotitle, 'Contact person2 Email': contactpersontwoemail})
        df.to_csv(countryfilename+'.csv', index=False, encoding='utf-8')
        companyname = []
        companylink = []
        cityop = []
        address = []
        phone = []
        fax = []
        emergencycall = []
        website = []
        email = []
        contactpersononename = []
        contactpersononetitle = []
        contactpersononeemail = []
        contactpersontwoname = []
        contactpersontwotitle = []
        contactpersontwoemail = []
# Press the green button in the gutter to run the script.


def getdata(a, text):
    try:
        name = a.findNext('div', attrs={'class': 'profile_label'}, text=text).parent
        chai = name.find('div', attrs={'class': 'profile_val'})
        return chai.text
    except AttributeError:
        return "null"


def urlvalid(url):
    if "wcaworld" in url:
        print("wcaworld")
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


if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
