# Pytest_Automation

* Project has been build on python / pytest framework to automate end to end features / test cases. 
* This can be downloaded and used to add automated test cases and execute.
* Added small utility to send what app messages to multiple contacts using whatsapp web which can be used to send bulk messages

Features:
1) Contain boiler plate code to set up driver, etc
2) Logging feature for test execution and reporting
3) Encryption utility to encrypt the passwords
4) Page object Model to strucuture the test cases which will be essential for maintenance
5) Lot of reusable methods for Selenium automation

Pre-requisite:
1)	Python 3.7
2)	Pip
3)	IDE (Eclipse / Pycharm or any IDE of your choice)
4)  Project pyhton packages specified in "requirements.txt" file

Project Details:

* Requirments.txt -> to store python packages required for the Project to run
  Ex: pytest, selenium, etc
* Pytestrun.bat -> Double to click to run the test automatically
* Globalconfig.json -> to store the app URL’s and other Global variables (Ex: User details, etc.) required for the project
* Conftest.py -> to configure set up and tear down steps (Ex: configuring selenium driver and close when test ends)

Folder Details:

1) UTIL - Contains common programs such as to read data from configuration file
2) TestData - to store the test data required for the Project
3) TestCases - Contains test cases created for the project
4) Selenium - Contains common selenium reusable methods such as click, sendkeys
5) Results - All the test execution output would be stored in this folder
6) OTPHandler - Project specific contains http server API’s and to read the OTP file
7) Drivers - Contains selenium browser drivers
8) AppPageObjects – to store application object locators (Ex: xpath, id etc)
9) AppComponents – Contains reusable application methods such as login, logout etc
