# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 02:12:54 2018

@author: tanasha
"""
import datetime

def Log(level, message):
    logLevel = "INFO"
   
    if level == 0:
        logLevel = "INFO"
    elif level == 1:
        logLevel = "WARNING"
    elif level == 2:
        logLevel = "ERROR"
    elif level == 3:
        logLevel = 'CRITICAL'
    else:
        logLevel = "Programmer is stupid and typed wrong log level"
    date = datetime.datetime.now()
    
    print("[" + str(date) + ", " + logLevel + "]: " + message)