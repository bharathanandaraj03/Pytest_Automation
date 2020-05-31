'''
Created on Apr 4, 2020

@author: windowsuser
'''
import csv
import logging

#Method to create CSV file with given File Name and fields
def  createCsvFileWithHeader(csvFileName,fieldnames):
            logging.info("creating/appending CSV File")
            csvFile = open(csvFileName, "a", newline="")       
            writer = csv.DictWriter(csvFile,fieldnames)
            writer.writeheader()
    
#Method to append CSV file with given data row
def appendCsvFileWithHeader(csvFileName,fieldnames,row):
            logging.info("appending CSV File")
            csvFile = open(csvFileName, "a",newline="")
            writer = csv.DictWriter(csvFile,fieldnames)
            writer.writerow(row)
            

    