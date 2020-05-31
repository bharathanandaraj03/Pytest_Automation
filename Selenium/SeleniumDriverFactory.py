'''
Created on Apr 18, 2020

@author: windowsuser
'''
from selenium import webdriver
import logging
import os
from Util import GlobalConfig
class SeleniumDriverFactory(object):
    '''
    classdocs
    '''
    def initSeleniumDriver(self,Browser):
        Browser = Browser.lower()
        logging.info("***Selenium Driver Set up****")
        rootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        logging.info("rootDir: "+rootDir)
        
        if(Browser == "chrome"):
            driverPath = rootDir+"\\"+GlobalConfig.getGlobalConfigData("chromeDriverPath")
            logging.info("driverPath: "+driverPath)
            driver = webdriver.Chrome(executable_path=driverPath)
            driver.set_page_load_timeout(30)
            logging.info(Browser+" driver instantiated")
            return driver