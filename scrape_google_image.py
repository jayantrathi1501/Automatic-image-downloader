from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

try:
    folder_name = input("Enter Folder Name:- ")   
    os.mkdir(folder_name)
except:
    print("Folder Exist with that name!")
    try:
        folder_name = input("Enter Folder Name:- ")   
        os.mkdir(folder_name)
    except:
        print("Folder Exist with that name!")
        try:
            folder_name = input("Enter Folder Name:- ")   
            os.mkdir(folder_name)
        except:
            print("Folder Exist with that name!")

img =input("who's image do u wanna download: ")
i_max =input("how many image do u wanna download: ")

driver = webdriver.Chrome('C:/Users/Dell/Desktop/jay/python/chromedriver.exe')
driver.get('https://www.google.com/')
box = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
box.send_keys(img)
box.send_keys(Keys.ENTER)
driver.find_element_by_xpath('//*[@id="hdtb-msb"]/div[1]/div/div[2]/a').click()

#Will keep scrolling down the webpage until it cannot scroll no more
last_height = driver.execute_script('return document.body.scrollHeight')
while True:
    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(5)
    new_height = driver.execute_script('return document.body.scrollHeight')
    try:
        driver.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
        time.sleep(5)
    except:
        pass
    if new_height == last_height:
        break
    last_height = new_height

total_pics = int(i_max)+1

for i in range(1,int(total_pics)):
   try:
      driver.find_element_by_xpath('//*[@id="islrg"]/div[1]/div['+ str(i) +']/a[1]/div[1]/img').screenshot('C:/Users/Dell/Desktop/jay/python/'+ folder_name +'/'+ folder_name + '(' + str(i) + ')'+'.png')
   except:
      print("error")





