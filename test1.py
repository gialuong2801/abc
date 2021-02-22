#Import the packages
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import time

import requests
from bs4 import BeautifulSoup
import array as arr
import pandas



all_link = []
content = []
name_job = []
name_company = []
name_location = []
salary = []
expiry = []
upload_date = []
position = []
career = []
skill = []
language_of_cv = []
detail_address = []
number_employees = []

#Chrome Webdriver options
chrome_options = Options()
chrome_options.add_argument ('--ignore-certificate-errors')
chrome_options.add_argument ("--igcognito")
chrome_options.add_argument ("--window-size=1920x1080")
chrome_options.add_argument ('--headless')


#Set path to the webdriver
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="C:/webdriver/chromedriver.exe")

#Open log-in url
driver.get("https://secure.vietnamworks.com/login/vi?client_id=3") 
driver.maximize_window()

#Time-wait
time.sleep(10)

#Fill the log-in information
driver.find_element_by_id("email").send_keys("luongdg.bi9159@st.usth.edu.vn") #PUT YOUR EMAIL HERE
driver.find_element_by_id('login__password').send_keys('Conanpro123')         #PUT YOUR PASSWORD HERE
driver.find_element_by_id("button-login").click()

#Open url
url = 'https://www.vietnamworks.com/tim-viec-lam/tat-ca-viec-lam'
driver.get(url)
time.sleep(10)
#Set request to webdriver
page_source = driver.page_source
page = page_source
soup = BeautifulSoup(page_source,"html.parser")

#Get all-link

page_num = 1

while True:

    block_job_list = soup.find_all("div",{"class":"block-job-list"})
    for i in block_job_list:
        link_catalogue = i.find_all("div",{"class":"col-12 col-lg-8 col-xl-8 p-0 wrap-new"})
        for j in link_catalogue:
            link = j.find("a")
            all_link.append("https://www.vietnamworks.com" + link.get("href"))
        salary_catalogue = i.find_all("div",{"class":"col-12 col-lg-4 col-xl-4 p-0 col-salary"})
        for j in salary_catalogue:
            salary = j.find("span")
            all_salary.append(salary.text.replace("\n","").strip())

    #Moving to next page

    a = driver.find_elements_by_class_name('page-link')    #Finds the pages list in the bottom of the page

    if page_num ==1:
        a[2].click()
        page_num +=1

    elif page_num >=2 and page_num <=4:
        a[4].click()
        page_num+=1

    elif page_num >4 and len(a)<7:
        print('End of page')
        break

    else:
        print('yes')
        a[6].click()
        page_num+=1
    time.sleep(3)

driver.quit()

print("\n".join(all_link))
print(len(all_link))
