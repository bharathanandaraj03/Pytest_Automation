'''
Created on Mar 28, 2020

@author: windowsuser
'''
from cryptography.fernet import Fernet
import logging

privatekey = b'VWp6MDSmQEeW9_DAtnCyt46QCbigQoeTDTRdizcm3xU='

#Method to Encrypt user input
def encrypt(inputStr):
        try:
            f= Fernet(privatekey)
            encryptedString = f.encrypt(inputStr.encode())
            logging.info("Encrypted String: "+str(encryptedString))
            return str(encryptedString)
        except:
            logging.error("Exception while encrypting String")
            raise Exception("Message")
    
#Method to Decrypt the user input
def decryptInputStr(encryptedString):
        try:
            byteencryptedString = bytes(encryptedString,"utf-8")
            f= Fernet(privatekey)
            decryptedString = f.decrypt(byteencryptedString)
            return str(decryptedString.decode())
        except:
            logging.error("Exception while decrypting String")
            raise Exception("Exception while decrypting String")