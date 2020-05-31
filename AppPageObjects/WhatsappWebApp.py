'''
Created on Apr 7, 2020

@author: windowsuser
'''
from selenium.webdriver.common.by import By

StartNewChat = (By.XPATH,"//div[@class='rAUz7']/div[@title='New chat']")
SearchOrStartNewChat = (By.XPATH,"//div[@class='_2S1VP copyable-text selectable-text'][1]")
FirstContactOnList = (By.XPATH,"//*[@id='app']//div[@class='_2EXPL']//div[@class='_3j7s9'][1]")
MessageText = (By.XPATH,"//*[@id='main']/footer//div[@class='_2S1VP copyable-text selectable-text']")
MessageSendButton = (By.XPATH,"//div[@class='weEq5']/button/span")
OptionsMenu = (By.XPATH,"//span[@data-icon='menu']")
Logout = (By.XPATH,"//div[@title='Log out']")
