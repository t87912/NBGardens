# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:06:51 2016

@author: Administrator
"""

# Import modules:
import pymysql
import csv
import logging
import sys

from userStoryInfo import userStories

# Import the user story py files:
from UserStories import AllUserStories
from UserStories.userStory1 import userStory1
from UserStories.userStory2 import userStory2
from UserStories.userStory3 import userStory3
from UserStories.userStory4 import userStory4
from UserStories.userStory5 import userStory5
from UserStories.userStory6 import userStory6
from UserStories.userStory12 import userStory12
from UserStories.userStory13 import userStory13
from UserStories.userStory14 import userStory14
from UserStories.userStory16 import userStory16


# TODO:
# rename local userStoryX to runUserStoryX etc

class MySQLDatabase(object):
    """ Database: Holds the database object used for querying, also holds the
        logic for the menus and runs the actual queries. """
    def __init__(self, userLoginDetails, logger, fh, sqlMenuLines):
        self.logger = logger
        self.fh = fh # set filehandler, for closing the log file        
        self.menuOption = 0
        self.username = userLoginDetails[0]
        self.password = userLoginDetails[1]
        self.backToMain = False
        self.db = None
        self.run_query_obj = AllUserStories.AllUserStories()
        self.menuLines = sqlMenuLines
        self.generateMainLogic()
            
    def generateMainLogic(self):
        self.mainLogicText = \
"""
valid = False
while (not valid):
    self.printMenu()
    valid = self.getMenuInput()
    if (valid):
        if (self.menuOption == 0):
            print ("Exiting the program...")
            sys.exit(0)
        elif (self.menuOption == 1):
            self.customQuery(False, 0)
            valid = False
        elif (self.menuOption == 2):
            print ("Returning to main menu...")
        %s
        if (self.backToMain):
            valid = True
        else:
            valid = False
"""
        self.menuOptionText = """
        elif (self.menuOption == %s):
            %s
            valid = False
"""
        
        menuOptionsList = []
        for x in range(0, len(self.menuLines)-5):
            parametersList = []
            for i in range(0, len(userStories[x][2])):
                if (userStories[x][2][i] == 1):
                    parametersList.append(1)
                else:
                    parametersList.append(0)
            parametersText = ""
            print ("LENGTH param list: %s" % (len(parametersList)))
            for p in range(0, len(parametersList)):
                if (p == len(parametersList)-1):
                    param = " %s" % (parametersList[p])
                    parametersText += param
                else:
                    param = " %s," % (parametersList[p])
                    parametersText += param
            callMethodText = "self.callUserStory%s(False,%s)" % (x, parametersText)
            toAppend = self.menuOptionText % (x+3, callMethodText)
            menuOptionsList.append(toAppend)
        
        menuOptionsString = ""
        for z in range(0, len(menuOptionsList)):
            menuOptionsString += menuOptionsList[z]
        self.mainLogicCode = self.mainLogicText % (menuOptionsString)
        print (self.mainLogicCode)
        

    def login(self):
        """ login: Try/Except to log the user in. """
        try:
            # Ask Tom for the ip/password
            self.db = pymysql.connect("", "", "", "nbgardensds")
            print ("Connecting to MySQL database...")
            print ("Connection to MySQL database was successful.")
            self.logger.info('Successful login to MySQL database, username: %s' % (self.username))
            return True
        except:
            print ("Error: username or password incorrect.")
            self.logger.info("Unsuccessful login: %s", self.username)
            return False

    def getDB(self):
        return self.db
        
    def closeConnection(self):
        self.db.close()

    def mainLogic(self):
        #eval(self.mainLogicCode)
        exec(self.mainLogicCode)
#        """ mainLogic: Holds the logic for the main menu. """
#        valid = False
#        while (not valid):
#            self.printMenu()
#            valid = self.getMenuInput()
#            if (valid):
#                if (self.menuOption == 0):
#                    print ("Exiting the program...")
#                    sys.exit(0)
#                elif (self.menuOption == 1):
#                    self.customQuery(False, 0)
#                    valid = False
#                elif (self.menuOption == 2):
#                    print ("Returning to main menu...")
#                elif (self.menuOption == 3):
#                    self.callUserStory2(False, 0, 0)
#                    valid = False
#                if (self.backToMain):
#                    valid = True
#                else:
#                    valid = False

    def exitProgram(self):
        print ("Exiting the program...")
        self.logger.info('---------- Finished logging -----------')
        self.fh.close()
        sys.exit(0)

    def printMenu(self):
        """ printMenu: Prints the main menu. """
        for x in range(0, len(self.menuLines)):
            print (self.menuLines[x])

    def getMenuInput(self):
        """ getMenuInput: Gets and validates user input of menu choice. """
        userChoice = input("Input option number: ")
        try:
            userChoice = int(userChoice)
        except:
            print ("Error. Please enter a valid number.")
            return False

        # Below is list of all valid input numbers
        validInputList = list(range(0, len(self.menuLines)))

        if (int(userChoice) not in validInputList):
            print ("Error. Please enter a valid number.")
            return False
        else:
            self.menuOption = userChoice
            return True

    def toCSV(self, dates, ratings):
        """ toCSV: Writes dates/ratings to CSV file.  """
        # Convert datetimes to date strings
        for x in range(0, len(dates)):
            dates[x] = dates[x].strftime('%d-%m-%Y')

        for y in range(0, len(ratings)):
            ratings[y] = str(ratings[y])

        forCSV = []
        for i in range(0,len(ratings)):
            forCSV.append([dates[i],ratings[i]])

        print ("Writing dates and ratings to CSV file: /CSV Files/ratingsOverTime.csv...")
        with open("C:\\Users\\Administrator\\Desktop\\Week 5 - Python\\py files\\CSV Files\\ratingsOverTimeSQL.csv", "w") as f:
            # Last 2 parameters below to remove empty line between each line
            writer = csv.writer(f, sys.stdout, lineterminator='\n')
            for z in range(0, len(forCSV)):
                writer.writerow(forCSV[z])

    def customQuery(self, GUI, query):
        """ customeQuery: Executes user custom query. Need validation here. """
        if (not GUI):
            query = input("Input SQL query: ")
        self.logger = logging.info('Custom SQL query: %s', query)
        cursor = self.db.cursor() # Creating the cursor to query the database
        # Executing the query:
        try:
            cursor.execute(query)
            self.db.commit()
            results = cursor.fetchall()
            for row in results:
                toPrint = []
                for i in range(0, len(row)):
                    toPrint.append([row[i]])
                print (toPrint)
            if (GUI):
                return results
        except:
            self.db.rollback()
            print ("Error: SQL query was invalid.")
            
    def callUserStories(self, index):

    def callUserStory1(self, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory1(self.db, True, startDate, endDate)
        else:
            return userStory1(self.db, False, startDate, endDate)
