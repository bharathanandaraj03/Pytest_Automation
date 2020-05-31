'''
Created on Mar 30, 2020

@author: windowsuser
'''
import json
import logging

#Method to Load required data from GlobalConfig File
def getGlobalConfigData(getGlobalConfigKey): 
        try:
            globalConfigFile = open("GlobalConfig.json", "r")
            globalConfigData = json.load(globalConfigFile)
            getGlobalValue=globalConfigData[getGlobalConfigKey]
            return str(getGlobalValue)
        except FileNotFoundError:
            logging.error("globalConfig not exist in the location"+globalConfigFile)
            raise Exception
        except KeyError:
            logging.error("Give key not exist in GlobalConfig: "+getGlobalConfigKey)
        except:
            logging.error("Exception while reading from globalConfig.json file")
            raise Exception
        return None
    
