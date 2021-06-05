# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 23:07:22 2021

@author: Fazil P S
"""


import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By




def usuallogin(email,password):
    cred=driver.find_elements_by_tag_name('input')
    cred[0].send_keys(email)
    cred[1].send_keys(password)
    signin2=driver.find_element_by_xpath('//div[@class="auth__traditional__20x3n"]/button')
    signin2.click()

def withgoogle(email,password):
    signin2=driver.find_element(By.XPATH, '//span[text()="Sign in with Google"]')
    signin2.click()
    driver.implicitly_wait(3)
    email=driver.find_element_by_tag_name('input')
    email.send_keys(email)
    next1=driver.find_element(By.XPATH, '//span[text()="Next"]')
    next1.click()
    driver.implicitly_wait(3)
    passw=driver.find_element_by_xpath('//div[@class="Xb9hP"]/input[@name="password"]')
    passw.send_keys(password)
    passw.send_keys(Keys.RETURN)
    driver.implicitly_wait(3)
      
def blogopen():
    blogs=driver.find_element(By.XPATH, '//span[text()="Blogs"]')
    blogs.click()
    time.sleep(4)
    driver.execute_script("window.scrollTo(0, 700)")
    item=driver.find_elements_by_class_name("item-card__img__2qk2F")
    time.sleep(2)
    item[1].click()
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    usertab=driver.find_element_by_class_name("dashboard__username__O6RIy")
    usertab.click()
    time.sleep(2)
    signout=driver.find_element(By.XPATH, '//span[text()="Sign out"]')
    signout.click()
    time.sleep(2)
    home=driver.find_element_by_class_name("logo__1FDVs")
    home.click()

# Provide the link to your webdriver below
driver=webdriver.Chrome(r"C:\Users\user\Desktop\exam lounge\chromedriver_win32\chromedriver.exe")
driver.get("https://www.examlounge.com/")
driver.implicitly_wait(3)
signin=driver.find_element(By.XPATH, '//span[text()="Sign in"]')
signin.click()
driver.implicitly_wait(3)

email="" # Type your mail ID here
password="" # Type your Password here

# Use any login method by commenting the other one
withgoogle(email,password) 
#usuallogin(email,password)
blogopen()