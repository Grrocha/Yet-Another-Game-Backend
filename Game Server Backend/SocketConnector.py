# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 00:04:28 2018

@author: tanasha
"""
import socket
import Settings
import Utility.Logger as Logger

class SocketConnector(object):
    def __init__(self, hostIP, hostPort):
        logMessage = "Initiating socket at " + hostIP +":" + str(hostPort)
        Logger.Log(0, logMessage)
        self.socketConn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.hostIP = hostIP
        self.hostPort = hostPort
        
    def bind(self):
        try:
            Logger.Log(0, "Binding Socket")
            self.socketConn.bind((self.hostIP, self.hostPort))
            Logger.Log(0, "Sucessfuly bind")
        except Exception as ex:
            Logger.Log(1, "Failed to bind:" + str(ex))
            return ex
            
        
    def send(self, message, destination):
        try:
            logMessage = "Sending Message to " + str(destination)
            Logger.Log(0,logMessage)
            data = message
            self.socketConn.sendto(data.encode('utf-8'),destination)
            Logger.Log(0,"Message Sent")
        except Exception as ex:
            Logger.Log(1, "Failed to send message: " + str(ex))
            return ex
        
    def receive(self):
        try:
            received, address = self.socketConn.recvfrom(2048)
            logMessage = "Received message from " + address
            Logger.Log(0, logMessage)
        except Exception as ex:
            Logger.Log(1, "Failed to receive message: " + str(ex))
            return ex
        
socketConn = SocketConnector(Settings.socketHostIp, Settings.socketHostPort)
socketConn.bind()