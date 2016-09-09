# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:08:40 2016

@author: Administrator
"""

# Import modules:
import csv
import sys
from pprint import pprint
from pymongo import MongoClient
import MongoQueries

from UserStories.userStory7 import userStory7
from UserStories.userStory8 import userStory8
from UserStories.userStory9 import userStory9
from UserStories.userStory10 import userStory10
from UserStories.userStory11 import userStory11
from UserStories.userStory15 import userStory15

#MONGODB_URI = 'mongodb://master:pa$$w0rd@ds019766.mlab.com:19766/nbgardens'
#conn = MongoClient(MONGODB_URI)
#db = conn.get_default_database() 

class MongoDatabase(object):
    """ Database: Holds the database object used for querying. Prints the menu
        for the Mongo options, executes custom query. """
    def __init__(self):
        self.conn = None # Mongo connection set later on
        self.menuLines = ["\nPlease select an option: ",
                          "1. Input a custom MongoDB query.",
                          "2. Average rating a particular customer has given NB Gardens", # mongo
                          "3. Average rating a group of customers from a particular county has given NB Gardens.", # mongo + small sql statement
                          "4. Average rating a group of customers from a particular demographic (age, gender) has given NB Gardens", # mongo + small sql statement (age + gender)
                          "5. Average rating given to a product through the website against customer order ratings with that same product included", # mongo
                          "6. Customer satisfaction in key areas of the business over a given period of time", # mongo + order creation date from order id in SQL
                          "7. Create a graph showing levels of customer satisfaction in a range of areas over a period of time", # mongo
                          "8. Go back to the main menu",
                          "9. Quit"]
        validLogin = self.login()
        
    def run(self):
        validLogin = self.login()
        if (validLogin):
            print ("Connection to MongoDB successful.")
            self.mainLogic()
        elif (not validLogin):
            print ("Please check the MongoDB connection parameters.")
            
    def login(self):
        """ login: Connects to mongoDB using default parameters. """
        try:
            MONGODB_URI = 'mongodb://master:pa$$w0rd@ds019766.mlab.com:19766/nbgardens'
            self.conn = MongoClient(MONGODB_URI)
            print ("Connecting to MongoDB...")
            return True
        except:
            print ("Error: Could not connect to MongoDB.")
            return False
            
    def printMenu(self):
        """ printMenu: Prints the main menu. """
        for x in range(0, len(self.menuLines)):
            print (self.menuLines[x])
            
    def getMenuInput(self):
        """ getMenuInput: Get user input menu choice. """
        userChoice = input("Input option number: ")
        try:
            userChoice = int(userChoice)
        except:
            print ("Error. Please enter a valid number.")
            return False
        validInputList = list(range(1, 10))
        if (int(userChoice) not in validInputList):
            print ("Error. Please enter a valid number.")
            return False
        else:
            self.menuOption = userChoice
            return True
            
    def mainLogic(self):
        """ mainLogic: Provides the logic for the main menu. """
        valid = False
        while (not valid):
            self.printMenu()
            valid = self.getMenuInput()
            if (valid):
                if (self.menuOption == 1):
                    self.customQuery(False, 0)
                    valid = False
                elif (self.menuOption == 2):
                    self.userStory7(False, 0)
                    valid = False
                elif (self.menuOption == 3):
                    self.userStory8(False, 0)
                    valid = False
                elif (self.menuOption == 4):
                    self.userStory9(False)
                    valid = False
                elif (self.menuOption == 5):
                    self.userStory10(False, 0)
                    valid = False
                elif (self.menuOption == 6):
                    self.userStory11(False)
                    valid = False
                elif (self.menuOption == 7):
                    self.userStory15(False)
                    valid = False
                elif (self.menuOption == 8):
                    print ("Going back to the main menu...")
                elif (self.menuOption == 9):
                    print ("Exiting the program...")
                    sys.exit(0)
                    
    def customQuery(self, GUI, userInput):
        """ customQuery: Allows the user to execute a custom query by running
            eval() on the user input. Need validation for drop table etc. """
        db = self.conn.get_default_database() 
        if (not GUI):
            print ("Example: db.CustomerReviews.find({})")
            userInput = input("Enter the MongoDB command: ")
        cursor = eval(userInput)
        results = []
        for document in cursor:
            pprint (document)
            results.append(document)
            
        if (GUI):
            return results;
        
    def toCSV(self, dates, ratings):
        """ toCSV: Writes the dates/ratings to a CSV file. """
        forCSV = []
        for i in range(0,len(ratings)):
            forCSV.append([dates[i],ratings[i]])
        
        print ("Writing dates and ratings to CSV file: /CSV Files/ratingsOverTime.csv...")
        with open("C:\\Users\\Administrator\\Desktop\\Week 5 - Python\\py files\\CSV Files\\ratingsOverTimeMongoDB.csv", "w") as f:
            # Last 2 parameters below to remove empty line between each line            
            writer = csv.writer(f, sys.stdout, lineterminator='\n')
            for z in range(0, len(forCSV)):
                writer.writerow(forCSV[z])

    def userStory7(self, GUI, customerID):
        """ useCase7:  """
        if (GUI):
            return userStory7(MongoQueries, True, customerID)
        else:
            return userStory7(MongoQueries, False, customerID)
        
    def userStory8(self, GUI, gender):
        """ useCase8:  """
        if (GUI):
            return userStory8(MongoQueries, True, gender)
        else:
            return userStory8(MongoQueries, False, gender)
        
    def userStory9(self, GUI):  
        """ useCase9: """
        if (GUI):
            return userStory9(MongoQueries, True)
        else:
            return userStory9(MongoQueries, False)
            
    def userStory10(self, GUI, productID):  
        """ useCase10: """
        if (GUI):
            return userStory10(MongoQueries, True, productID)
        else:
            return userStory10(MongoQueries, False, productID)
            
    def userStory11(self, GUI):  
        """ useCase11: """
        if (GUI):
            return userStory11(MongoQueries, True)
        else:
            return userStory11(MongoQueries, False)
            
    def userStory15(self, GUI):  
        """ useCase10: """
        if (GUI):
            return userStory15(MongoQueries, True)
        else:
            return userStory15(MongoQueries, False)