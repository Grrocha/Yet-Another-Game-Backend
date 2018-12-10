# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 17:40:54 2018

@author: tanasha
"""
import sqlalchemy
import Settings

class SqlConn(object):
    
    def __init__(self, engine):
        try:
            self.engine = sqlalchemy.create_engine(engine)
            self.connection = ""
        except Exception as ex:
            return("Error: " + str(ex))
        
    def Connect(self):
        try:
            self.connection = self.engine.connect()
        except Exception as ex:
            return("Error: " + str(ex))
            
    def Close(self):
        try:
            self.connection.close()
        except Exception as ex:
            return("Error: " + str(ex))
    
    def ExecuteTransaction(self,transaction):
        self.Connect()
        try:
            return self.engine.execute(transaction)
        except Exception as ex:
            return("Error: " + str(ex))
        
conn = SqlConn(Settings.sqlEngine)
