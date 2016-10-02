# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:11:07 2016

@author: Administrator
"""

# TODO
# 2. finish off mongo queries that use SQL
# 8. on github readme, have proper dependencies eg. need pysql/pymongo

# Import modules:
from AutoGenCode import AutoGenCode

import sys

# Import other python class files:
from Login import Login
from sqlDatabase.MySQLDatabase import MySQLDatabase
from mongoDatabase.MongoDatabase import MongoDatabase
from Logger import Logger

class MainLogic(object):
    """ MainLogic: Holds the logic for running the program in the prompt.  """
    def __init__(self, autoGen):
        self.menuLines = ["\nPlease select an option: ",
                         "1. Query MySQL Database.",
                         "2. Query MongoDB Database.",
                         "8. Logout.",
                         "9. Quit."]
        self.autoGen = autoGen
        self.loggedIn = False
        loggerObject = Logger("TUI") # Init the logger object
        self.logger = loggerObject.getLogger() # Get the logger object
        self.fh = loggerObject.getFileHandler() # Get the logger filehandler      
        self.initialLogin = True # used to not display gnome after first login
        self.runProgram()

#    def runProgram(self):  
#        """ runProgram: Holds logic for the menu choices. """
#        valid = False
#        while (not valid):
#            print ("Welcome to the NB Gardens Databse Query System!")
#            self.printGnome()
#            self.printMenu()
#            valid = self.getMenuInput()
#            if (valid):
#                if (self.menuOption == 1):
#                    validLogin = False
#                    while (not validLogin):
#                        userLogin = Login()
#                        userLoginDetails = userLogin.getLoginDetails()
#                        db = MySQLDatabase(userLoginDetails)
#                        validLogin = db.login()
#                    db.mainLogic()
#                    valid = False
#                elif (self.menuOption == 2):
#                    mongoDB = MongoDatabase()
#                    mongoDB.run()
#                    valid = False
#                elif (self.menuOption == 9):
#                    print ("Exiting the program...")
#                    sys.exit(0)

    def runProgram(self):  
        """ runProgram: Holds logic for the menu choices. """
        valid = False
        while (not valid):
            if (not self.loggedIn):
                print ("Welcome to the NB Gardens Databse Query System!")
                self.printGnome()
                validLogin = False
                while (not validLogin):
                    userLogin = Login()
                    userLoginDetails = userLogin.getLoginDetails()
                    db = MySQLDatabase(userLoginDetails, self.logger, self.fh, self.autoGen) # Init MySQL db
                    validLogin = db.login() # Login to MySQL db
                    if (validLogin):
                        sqlDBForMongo = db.getDB()# Get MySQL db object to pass to MongoDB
                        mongoDB = MongoDatabase() # Init Mongo db
                        mongoDB.setDatabase(sqlDBForMongo) # Pass MySQL db into Mongo
                        self.loggedIn = True
            else:
                if (self.loggedIn):
                    if (not self.initialLogin):
                        print ("Welcome to the NB Gardens Databse Query System!")
                        self.printGnome()
                    while (not valid):
                        self.printMenu()
                        valid = self.getMenuInput()
                    if (self.menuOption == 1):
                        db.mainLogic()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 2):
                        mongoDB.run()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 8):
                        self.loggedIn = False
                        valid = False
                    elif (self.menuOption == 9):
                        print ("Exiting the program...")
                        self.logger.info('---------- Finished logging TUI -----------')
                        self.fh.close()
                        sys.exit(0)
        
    def printMenu(self):
        """ printMenu: Prints the main menu. """
        for x in range(0, len(self.menuLines)):
            print (self.menuLines[x])
            
    def printGnome(self):
        """ printGnome: Reads text file containing gnome in ASCII text and
            prints it out, stripping out newline characters. """
        with open('assets\\gnome.txt') as f:            
            for line in f: 
                line = line.rstrip('\n')
                print (line)
    
    def getMenuInput(self):
        """ getMenuInput: Gets user input for the menu, returns True/False. """
        userChoice = input("Input option number: ")
        validMenuInput = [1,2,8,9]
        try:
            userChoice = int(userChoice)
        except:
            print ("Error. Please enter a valid number.")
            return False
        if (int(userChoice) not in validMenuInput):
            print ("Error. Please enter a valid number.")
            return False
        else:
            self.menuOption = userChoice
            return True
            
    

        
if __name__ == "__main__":
    #app = MainLogic()
    autoGenCode = AutoGenCode()
    autoGen = autoGenCode.getAutoGen()
    mainTUI = MainLogic(autoGen)