'''
Created on Apr 18, 2020

@author: windowsuser
'''
import pytest
import logging
from Selenium import SeleniumDriverFactory
from Util import GlobalConfig

#Pytest fixture to set up and tear down
@pytest.fixture(scope="class")
def seleniumFixture(request):
        #Suite Set up
        logging.info("Suite Set up started")
        driver = SeleniumDriverFactory.SeleniumDriverFactory.initSeleniumDriver("","Chrome")
        request.cls.driver = driver
        
        #Suite tear down
        yield
        logging.info("Closing driver")
        driver.close()
        logging.info("Execution complete")
        logging.shutdown()

#Setting up logging for execution
loggingLevel = str(GlobalConfig.getGlobalConfigData("loggingLevel")).upper()

if(loggingLevel=="CRITICAL"):
    logLevel = logging.CRITICAL
elif(loggingLevel=="ERROR"):
    logLevel = logging.ERROR
elif(loggingLevel=="WARNING"):
    logLevel = logging.WARNING
elif(loggingLevel=="INFO"):
    logLevel = logging.INFO
elif(loggingLevel=="DEBUG"):
    logLevel = logging.DEBUG
else:
    logLevel = logging.DEBUG
    
logging.basicConfig(filename="Results/execution.log",filemode='w',level=logLevel,format="%(asctime)s:%(levelname)s:%(message)s")
        