# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:06:51 2016

@author: Administrator
"""

# Import modules:
import pymysql
import sys
import csv
import logging

# Import the user story py files:
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
    def __init__(self, userLoginDetails):
        self.menuOption = 0
        self.username = userLoginDetails[0]
        self.password = userLoginDetails[1]
        self.db = None
        self.menuLines = ["\nPlease select an option: ",
                          "User Story Number | Description",
                          "1. Top salesperson of a given period, based on total cost of their sales during that time",
                          "2. Which customer has highest spending in given period",
                          "3. Which customer has spent more than 'x' amount during a given period",
                          "4. Total spend vs total cost for given time period",
                          "5. Total return on investment for particular product for given time period",
                          "6. Average amont of time it takes to fulfill an order during a particular time period",
                          "12. Check website details for particular product match that is stored in the physical inventory",
                          "13. Create a graph showing the amount of sales for a particular product over a period of time",
                          "14. Create a graph showing the amount of sales made by a particular sales person over a period of time",
                          "16. Create a graph of the number of stock available for a particular product with the number of sales for that particular product over a particular time period",
                          "\n17. Input a custom SQL query.",
                          "\n18. Go back to the main menu",
                          "19. Quit"]
    
    def login(self):
        """ login: Try/Except to log the user in. """
        try:
            self.db = pymysql.connect("db4free.net", "gemmai95", "raysmithy", "nbgardensqa")
            print ("Login successful.")
            print ("%s, welcome to ASAS!" % (self.username))
            return True
        except:
            print ("Error: username or password incorrect.")
            #self.logger.info("Unsuccessful login: %s", self.username)
            return False
            
    def mainLogic(self):
        """ mainLogic: Holds the logic for the main menu. """
        valid = False
        while (not valid):
            self.printMenu()
            valid = self.getMenuInput() 
            if (valid):
                if (self.menuOption == 1):
                    self.callUserStory1(False, 0, 0)
                    valid = False
                elif (self.menuOption == 2):
                    self.callUserStory2(False, 0, 0)
                    valid = False
                elif (self.menuOption == 3):
                    self.callUserStory3(False, 0, 0, 0)
                    valid = False
                elif (self.menuOption == 4):
                    self.callUserStory4(False, 0, 0)
                    valid = False
                elif (self.menuOption == 5):
                    self.callUserStory5(False, 0, 0)
                    valid = False
                elif (self.menuOption == 6):
                    self.callUserStory6(False, 0, 0)
                    valid = False
                elif (self.menuOption == 12):
                    self.callUserStory12(False, 0)
                    valid = False
                elif (self.menuOption == 13):
                    self.callUserStory13(False, 0, 0)
                    valid = False
                elif (self.menuOption == 14):
                    self.callUserStory14(False, 0, 0, 0)
                    valid = False
                elif (self.menuOption == 16):
                    self.callUserStory16(False, 0, 0)
                    valid = False
                elif (self.menuOption == 17):
                    self.customQuery(False, 0)                    
                    valid = False
                elif (self.menuOption == 18):
                    print ("Returning to main menu...")
                elif (self.menuOption == 19):
                    print ("Exiting the program...")
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
        validInputList = list(range(1, 7)) + list(range(12, 15)) + list(range(16, 20))

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
        except:
            self.db.rollback()

        results = cursor.fetchall()
        for row in results:
            toPrint = []
            for i in range(0, len(row)):
                toPrint.append([row[i]])
            print (toPrint)
        
        if (GUI):
            return results
        
    def callUserStory1(self, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory1(self.db, True, startDate, endDate)
        else:
            return userStory1(self.db, False, startDate, endDate)
        
    def callUserStory2(self, GUI, startDate, endDate):
        """ etc """
        if (GUI):
            return userStory2(self.db, True, startDate, endDate)
        else:
            return userStory2(self.db, False, startDate, endDate)
            
    def callUserStory3(self, GUI, amount, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory3(self.db, True, amount, startDate, endDate)
        else:
            return userStory3(self.db, False, amount, startDate, endDate)
        
    def callUserStory4(self, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory4(self.db, True, startDate, endDate)
        else:
            return userStory4(self.db, False, startDate, endDate)
        
    def callUserStory5(self, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory5(self.db, True, startDate, endDate)
        else:
            return userStory5(self.db, False, startDate, endDate)
        
    def callUserStory6(self, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory6(self.db, True, startDate, endDate)
        else:
            return userStory6(self.db, False, startDate, endDate)
        
    def callUserStory12(self, GUI, productID):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory12(self.db, True, productID)
        else:
            return userStory12(self.db, False, productID)
        
    def callUserStory13(self, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory13(self.db, True, startDate, endDate)
        else:
            return userStory13(self.db, False, startDate, endDate)
        
    def callUserStory14(self, GUI, startDate, endDate, employeeID):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory14(self.db, True, startDate, endDate, employeeID)
        else:
            return userStory14(self.db, False, startDate, endDate, employeeID)
        
    def callUserStory16(self, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (GUI):
            return userStory16(self.db, True, startDate, endDate)
        else:
            return userStory16(self.db, False, startDate, endDate)