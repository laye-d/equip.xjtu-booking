# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 10:38:50 2020

@author: dl
"""

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui
import time
import getpass
#import eventlet  

#*************INFO****************
url = "http://equip.xjtu.edu.cn/home/"
url_2 = "http://equip.xjtu.edu.cn/lims/!equipments/equipment/index.994.reserv"
username = "username"
#print("Enter the password of username '"+username+"':")
#pwd = getpass.getpass()
pwd = "password"
#position
position_x = 1300
position_y = 665 #615 #570 #525  #675
#position test
#pyautogui.moveTo(position_x,position_y)
#********************************

browser = webdriver.Chrome()
browser.maximize_window()  
browser.get(url)
browser.implicitly_wait(20)
elem=browser.find_element_by_id("top_4")
elem.click()
browser.implicitly_wait(20)
elem=browser.find_element_by_name("username")
elem.send_keys(username)
elem=browser.find_element_by_name("pwd")
elem.send_keys(pwd)
elem=browser.find_element_by_id("account_login")
elem.click()
time.sleep(5)
browser.get(url_2)

class alert_is_present(object):
    """ Expect an alert to be present."""

    """判断当前页面的alert弹窗"""
    def __init__(self):
        pass

    def __call__(self, driver):
        try:
            alert = driver.switch_to.alert
            alert.text
            return alert
        except NoAlertPresentException:
            return False

time.sleep(20)
time.sleep(5)
refresh_success = False;
#eventlet.monkey_patch() 

while True:
        pyautogui.doubleClick(position_x,position_y)
        time.sleep(1)
#        with eventlet.Timeout(1,False):
#            try: 
#                result = browser.find_element_by_name("save")
#            except:
        result_alert = EC.alert_is_present()(browser);
        time.sleep(0.5)
        if not result_alert:
                     try: 
                         browser.implicitly_wait(20)
                         bool_elemFound = False
                         elem = browser.find_element_by_name("extra_fields[1][委托操作]")
                         elem.click()
                         bool_elemFound = True
                         elem = browser.find_element_by_name("extra_fields[2][块体]")
                         elem.click()
                         elem = browser.find_element_by_name("extra_fields[5][否]")
                         elem.click()
                         elem = browser.find_element_by_name("extra_fields[6][其他]")
                         elem.click()
                         elem = browser.find_element_by_name("extra_fields[25][形貌观察]")
                         elem.click()
                         elem = browser.find_element_by_name("description")
                         elem.send_keys("1")
                         elem = browser.find_element_by_name("extra_fields[3]")
                         elem.send_keys("1")
                         elem = browser.find_element_by_name("extra_fields[4]")
                         elem.send_keys("1")
                         elem = browser.find_element_by_name("extra_fields[23]")
                         elem.send_keys("1")
                         elem = browser.find_element_by_name("extra_fields[24]")
                         elem.send_keys("1")
                         elem = browser.find_element_by_name("captcha")
                         elem.send_keys("1")
                         refresh_success = True
                         print("refresh success")
                         break
                     except:
                         if bool_elemFound == False:
                             print("No target element found, retry...")####################################
                         else:
                             print("Target element found, stop...")####################################
                             break########################################################################
        while True:
                result_alert = EC.alert_is_present()(browser)
                if result_alert:
                    print (result_alert.text)
                    result_alert.accept()
                    break
                else: pyautogui.doubleClick(position_x,position_y)
        
print (refresh_success)                

