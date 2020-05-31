'''
Created on May 30, 2020

@author: windowsuser
'''
import pytest
from Selenium import SeleniumCommon
from Util import GlobalConfig
from AppComponents import WhatsappWeb
import logging

class SendWhatAppMessages:
    
    @pytest.mark.seltest
    @pytest.mark.usefixtures("seleniumFixture")
    def sendWhatAppMessages(self):
                SeleniumCommon.launchWebApplication(self.driver,GlobalConfig.getGlobalConfigData("whatsAppWebURL") )
                #WhatsappWeb.sendWhatAppMessageToNotSubmitted(self.driver,csvFileName,"Hi, Good Morning Have a nice day")
                #WhatsappWeb.logoutWhatAppMessage(self.driver)