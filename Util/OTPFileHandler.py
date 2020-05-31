'''
Created on May 9, 2020

@author: windowsuser
'''
from os.path import os
import time

class myOTPFileHandler():
    def removeFileIfExist(self,FileName):
            if os.path.exists(FileName):
                print("OTP File Exist")
                os.remove(FileName)
                print("Removed OTP file")
            else:    
                print("OTP File not Exist")
        
    def writeDataToFile(self,FileName,text):
            if not os.path.exists(FileName):
                print("OTP File Exist")
                file = open(FileName,"w")
                file.write(text)
            else:    
                print("OTP File not Exist")
                
            
    def getDataFromFile(self,FileName):
        data = ""
        if os.path.exists(FileName):
            print("OTP File Exist")
            file = open(FileName,"r")
            data = file.read()
            print(data)
        else:    
            print("OTP File not Exist")
        return data
    
    def returnOTPForTest(self,FileName):
        print("OTP Module:")
        otp=""
                
        for x in range(120):
            time.sleep(1)
            if os.path.exists(FileName):
                print("OTP file exist reading OTP from File")
                otp = myOTPFileHandler.getDataFromFile(self,FileName)
                print(otp)
                break
            else:
                print("OTP not received")
        return otp

#otp = myOTPFileHandler.returnOTPForTest("", "C:/Users/windowsuser/eclipse-workspace/pytestProject/OTPHandler/otp.txt")