'''
Created on Apr 7, 2020

@author: windowsuser
'''
from AppPageObjects import WhatsappWebApp
import time
from selenium.webdriver.common.by import By
from Selenium import SeleniumCommon
import csv
import logging

#Method to send What app messages
def sendWhatAppMessage(driver,contactNo,MessagetoSend):
    time.sleep(5)
    SeleniumCommon.clickObject(driver,*WhatsappWebApp.StartNewChat)
    SeleniumCommon.sendKeys(driver,contactNo,*WhatsappWebApp.SearchOrStartNewChat)
    time.sleep(1)
    SeleniumCommon.clickObject(driver,*WhatsappWebApp.FirstContactOnList)
    time.sleep(5)
    SeleniumCommon.sendKeys(driver,MessagetoSend,*WhatsappWebApp.MessageText)
    SeleniumCommon.clickObject(driver,*WhatsappWebApp.MessageSendButton)
    
#Method to Logout from Whatapp
def logoutWhatAppMessage(driver):
    SeleniumCommon.clickObject(driver,*WhatsappWebApp.OptionsMenu)
    time.sleep(2)
    SeleniumCommon.clickObject(driver,*WhatsappWebApp.Logout)
    time.sleep(2)
    
#Method to send WhatAPP message to multiple numbers
def sendWhatAppMessageToNotSubmitted(driver,testDataPath,message):
    #Reading data from test data file        
    csvFile = open(testDataPath, "r")
    csvReader = csv.DictReader(csvFile)
    
    #Iterating through all Values in CSV File
    for row in csvReader:
        empWhatAppNo=row["whatsAppno"]
        empStatus=row["Status"]
        #Send Message only if not submitted
        if("NotSubmitted" in empStatus):
            logging.info(empWhatAppNo)
            sendWhatAppMessage(driver, empWhatAppNo, message)