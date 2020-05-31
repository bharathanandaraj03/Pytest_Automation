'''
Created on Apr 4, 2020

@author: windowsuser
'''

import time
import random
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import logging

#Launching web application    
def launchWebApplication(driver,appURL):
    driver.get(appURL)
    driver.maximize_window()
    time.sleep(5)
    logging.info("Launched App URL: "+appURL)

def navigateNewWindow(driver,windowID):
    try:
        driver.switch_to.window(driver.window_handles[windowID])
        logging.info("Navigated to new window")
        time.sleep(10)
    except Exception as e:
        logging.error("An error occurred while navigating to new window: "+str(e))
        raise Exception
    
#Switch new window
def switchToFrame(driver,*testobject):
    try:    
        driver.switch_to.frame(driver.find_element(*testobject))
        logging.info("Switched to new frame")
        time.sleep(2)
    except Exception as e:
        logging.error("An error occurred while switching the frame: "+str(e))
        raise Exception   
    
#Method to get text from Object
def getTextFromObject(driver,*testobject):
    try:
        return driver.find_element(*testobject).text
    except Exception as e:
        logging.error("An error occurred while getting text from object: "+str(e))
        raise Exception
    
#Method to Click on any object
def clickObject(driver,*testobject):
    try:
        driver.find_element(*testobject).click()
        time.sleep(1)
        logging.info("Clicked object: "+str(testobject))
    except Exception as e:
        logging.error("An error occurred while clicking: "+str(e))
        raise Exception

#Method to Click on any object
def clickObjectIfExist(driver,*testobject):
    try:
        if(objectExist(driver,*testobject)):
            driver.find_element(*testobject).click()
            logging.info("Clicked object: "+str(testobject))
    except Exception as e:
        logging.error("An error occurred while clicking: "+str(e))
        raise Exception        
            
#Method to check if object exist or not 
def objectExist(driver,*testObject): 
    try:
        driver.find_element(*testObject)
    except NoSuchElementException:
        return  False
    return True

#Method to send keys
def sendKeys(driver,strToEnter,*testObject):
    try:
        driver.find_element(*testObject).clear()
        driver.find_element(*testObject).send_keys(strToEnter)
        logging.info("Entered text: "+str(strToEnter))
    except Exception as e:
        logging.error("An error occurred while sending keys: "+str(e))
        raise Exception    

#Method to send keys password
def sendKeysPassword(driver,strToEnter,*testObject):
    try:
        driver.find_element(*testObject).send_keys(strToEnter)
    except Exception as e:
        logging.error("An error occurred while sending keys: "+str(e))
        raise Exception

#Method to select values by text
def selectByText(driver,valueText,*testObject):
    try:
        selectObject = Select(driver.find_element(*testObject))
        selectObject.select_by_visible_text(valueText)
        time.sleep(1)
        logging.info("Selected Given value: "+valueText)
    except Exception as e:
        logging.error("An error occurred while selecting given value: "+str(e))
        raise Exception
                
#Method to takescreenshot
def takeSelScreenshot(driver,filepath):
    try:
        randnum = random.randint(10000,100000000)
        fileName = filepath+"/Screenshot"+str(randnum)+".png"
        driver.save_screenshot(fileName)
    except Exception as e:
        logging.error("An error occurred while taking screenshot: "+str(e))
        raise Exception    