'''
Created on May 9, 2020

@author: windowsuser
'''
from http.server import HTTPServer,BaseHTTPRequestHandler
from io import BytesIO
from os.path import os
import ssl

class SimpleHttpRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
        
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(200)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())
        print("Body Received: "+str(body.decode()))
        myOTPFileHandler.writeDataToFile(self,"otp.txt", str(body.decode()))

class myOTPFileHandler():
    def removeFileIfExist(self,FileName):
            if os.path.exists(FileName):
                print("OTP File Exist")
                os.remove(FileName)
                print("Removed OTP file")
            else:    
                print("OTP File not Exist")
        
    def writeDataToFile(self,FileName,text):
                file = open(FileName,"w")
                file.write(text)
                print("OTP updated")
                
            
    def getDataFromFile(self,FileName):
            data = ""
            if os.path.exists(FileName):
                print("OTP File Exist")
                file = open(FileName,"r")
                print(file.read())
            else:    
                print("OTP File not Exist")
            return data
 
myOTPFileHandler.removeFileIfExist("","otp.txt")    
httpd = HTTPServer(("",4443),SimpleHttpRequestHandler)
httpd.socket = ssl.wrap_socket(httpd.socket, 
                               keyfile="F:\Bharath\Enterprise\Learnings\OpenSSLCerts\pmtpkey.pem", 
                               certfile="F:\Bharath\Enterprise\Learnings\OpenSSLCerts\pmtpcrt.pem", 
                               server_side=True) 
httpd.serve_forever (0.2)
