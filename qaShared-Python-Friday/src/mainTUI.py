# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:11:07 2016

@author: Administrator
"""

# Import modules:
from AutoGenCode import AutoGenCode
from UserStories import AllUserStories
import sys
from Login import Login
from sqlDatabase.MySQLDatabase import MySQLDatabase
from mongoDatabase.MongoDatabase import MongoDatabase
from Logger import Logger

class MainLogic(object):
    """ MainLogic: Holds the logic for running the program in the prompt.  """
    def __init__(self, autoGen):
        self.menuLinesOLD = ["\nPlease select an option: ",
                         "1. Query MySQL Database.",
                         "2. Query MongoDB Database.",
                         "8. Logout.",
                         "9. Quit."]
                         
        self.menuLines = ["\nWhat would you like to do?\n",
                          "Find out about different areas of the business:",
                          "    1. Customer Information",
                          "    2. Order Information",
                          "    3. Product Information",
                          "    4. Employee Information",
                          "    5. NBGardens Information",
                          "Execute a custom query:",
                          "    6. Custom MySQL query",
                          "    7. Custom MongoDB query",
                          "Generate a user story:",
                          "    8. Create a user story",
                          "Execute generated user stories:",
                          "    No generated user stories",
                          "Other options:",
                          "    9. Logout",
                          "    10. Quit"]
        self.autoGen = autoGen
        self.allUserStories = AllUserStories.AllUserStories()
        self.loggedIn = False
        loggerObject = Logger("TUI") # Init the logger object
        self.logger = loggerObject.getLogger() # Get the logger object
        self.fh = loggerObject.getFileHandler() # Get the logger filehandler      
        self.initialLogin = True # used to not display gnome after first login
        self.runProgram()

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
                    self.db = MySQLDatabase(userLoginDetails, self.logger, self.fh, self.autoGen) # Init MySQL db
                    validLogin = self.db.login() # Login to MySQL db
                    if (validLogin):
                        sqlDBForMongo = self.db.getDB()# Get MySQL db object to pass to MongoDB
                        self.dbConn = self.db.getDB()
                        self.mongoDB = MongoDatabase() # Init Mongo db
                        self.mongoDB.setDatabase(sqlDBForMongo) # Pass MySQL db into Mongo
                        self.conn = self.mongoDB.getConnection()
                        self.loggedIn = True
            else:
                if (self.loggedIn):
                    if (not self.initialLogin):
                        print ("Welcome to the NB Gardens Databse Query System!")
                        self.printGnome()
                    while (not valid):
                        self.printMenu()
                        valid = self.getMenuInput()
#                    if (self.menuOption == 1):
#                        db.mainLogic()
#                        valid = False
#                        self.initialLogin = False
#                    elif (self.menuOption == 2):
#                        mongoDB.run()
#                        valid = False
#                        self.initialLogin = False
#                    elif (self.menuOption == 8):
#                        self.loggedIn = False
#                        valid = False
#                    elif (self.menuOption == 9):
#                        print ("Exiting the program...")
#                        self.logger.info('---------- Finished logging TUI -----------')
#                        self.fh.close()
#                        sys.exit(0)
                    if (self.menuOption == 1):
                        self.customerInfo()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 2):
                        self.orderInfo()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 3):
                        self.productInfo()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 4):
                        self.employeeInfo()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 5):
                        self.nbgardensInfo()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 6):
                        self.customSQL()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 7):
                        self.customMongo()
                        valid = False
                        self.initialLogin = False
                    elif (self.menuOption == 9):
                        self.loggedIn = False
                        valid = False
                    elif (self.menuOption == 10):
                        print ("Exiting the program...")
                        self.logger.info('---------- Finished logging TUI -----------')
                        self.fh.close()
                        sys.exit(0)
                        
    def customSQL(self):
        self.db.customQuery(False, 0)
        self.waitForEnter()
        
    def customMongo(self):
        self.mongoDB.customQuery(False, 0)
        self.waitForEnter()
        
    def customerInfo(self):
        menu = ["1. Customer with highest spending in given period", # userStory2 SQL
                "2. Customer who has spent more than 'x' in given period", # userStory3 SQL
                "3. Average rating a particular customer has given NB Gardens", # userStory7 Mongo
                "4. Average rating a group of customers from particular county have given NB Gardens", # userStory8 Mongo
                "5. Average rating a group of customers from particular demographic (age, gender) have given NB Gardens", # userStory9 Mongo
                "9. Back to main menu"]
        validOptions = [1,2,3,4,5,9] # Valid menu options
        
        while (True):
            userChoice = self.getUserMenuChoice(menu, validOptions)
            if (userChoice == 1):
                self.allUserStories.userStorySeries1(self.dbConn, False, 0, 0, 2)
            elif (userChoice == 2):
                self.allUserStories.userStorySeries2(self.dbConn, False, 0, 0, 0, 3)
            elif (userChoice == 3):
                self.allUserStories.mongoStory1(self.dbConn, self.conn, False, 0)
            elif (userChoice == 4):
                self.allUserStories.mongoStory2(self.dbConn, self.conn, False, 0)
            elif (userChoice == 5):
                self.allUserStories.mongoStory3(self.dbConn, self.conn, False, 0, 0, 0)
            else:
                print ("Returning to the main menu...")
                break
            self.waitForEnter()
            
    def orderInfo(self): # 6 10
        menu = ["1. Average amont of time it takes to fulfill an order during a particular time period", # userStory6 SQL
                "2. Compare average online rating for a product against customer order ratings with same product included", # userStory10 Mongo
                "9. Back to main menu"]
        validOptions = [1,2,9] # Valid menu options
        
        while (True):
            userChoice = self.getUserMenuChoice(menu, validOptions)
            if (userChoice == 1):
                self.allUserStories.userStorySeries1(self.dbConn, False, 0, 0, 6)
            elif (userChoice == 2):
                self.allUserStories.mongoStory4(self.dbConn, self.conn, False, 0)
            else:
                print ("Returning to the main menu...")
                break
            self.waitForEnter()
            
    def productInfo(self): # 5 12 13 16
        menu = ["1. Total return on investment for particular product for given time period", # userStory5 SQL
                "2. Check website details for particular product match that is stored in the physical inventory", # userStory12 SQL
                "3. Create a graph showing the amount of sales for a particular product over a period of time", # userStory13 SQL
                "4. Create a graph showing number of stock available for a product against number of sales for product during time period", # userStory16 SQL
                "9. Back to main menu"]
        validOptions = [1,2,3,4,9] # Valid menu options
        
        while (True):
            userChoice = self.getUserMenuChoice(menu, validOptions)
            if (userChoice == 1):
                self.allUserStories.userStorySeries2(self.dbConn, False, 0, 0, 0, 5)
            elif (userChoice == 2):
                self.allUserStories.userStory12(self.dbConn, False, 0)
            elif (userChoice == 3):
                self.allUserStories.userStorySeries1(self.dbConn, False, 0, 0, 13)
            elif (userChoice == 4):
                self.allUserStories.userStorySeries1(self.dbConn, False, 0, 0, 16)
            else:
                print ("Returning to the main menu...")
                break
            self.waitForEnter()
    
    def employeeInfo(self): # 1 14
        menu = ["1. Top salesperson of a given period", # userStory1 SQL
                "2. Create a graph showing the amount of sales made by a particular sales person over a period of time", # userStory14 SQL
                "9. Back to main menu"]
        validOptions = [1,2,9] # Valid menu options
        
        while (True):
            userChoice = self.getUserMenuChoice(menu, validOptions)
            if (userChoice == 1):
                self.allUserStories.userStorySeries1(self.dbConn, False, 0, 0, 1)
            elif (userChoice == 2):
                self.allUserStories.userStorySeries2(self.dbConn, False, 0, 0, 0, 14)
            else:
                print ("Returning to the main menu...")
                break
            self.waitForEnter()
            
    def nbgardensInfo(self): # 4 11 15
        menu = ["1. Total spend vs total cost for given time period", # userStory4 SQL
                "2. Customer satisfaction in key areas of the business over a given time period", # userStory11 Mongo
                "3. Create a graph showing the levels of customer satisfaction in a range of areas over a period of time", # userStory15 Mongo
                "9. Back to main menu"]
        validOptions = [1,2,3,9] # Valid menu options
        
        while (True):
            userChoice = self.getUserMenuChoice(menu, validOptions)
            if (userChoice == 1):
                self.allUserStories.userStorySeries1(self.dbConn, False, 0, 0, 4)
            elif (userChoice == 2):
                self.allUserStories.mongoStory5(self.dbConn, self.conn, False, 0, 0)
            elif (userChoice == 3):
                self.allUserStories.mongoStory6(self.dbConn, self.conn, False, 0, 0)
            else:
                print ("Returning to the main menu...")
                break
            self.waitForEnter()
        
    def getUserMenuChoice(self, menu, validOptions):
        valid = False
        while (not valid):
            self.printAnyMenu(menu)
            userChoice = input("Input option number: ")
            try:
                userChoice = int(userChoice)
                if (userChoice in validOptions):
                    valid = True
                    return userChoice
                else:
                    print ("\nPlease enter a valid menu option...\n")
            except:
                print ("\nPlease enter a valid menu option...\n")
        
    def waitForEnter(self):
        input("Press any key to continue")
        
    def printMenu(self):
        """ printMenu: Prints the main menu. """
        for x in range(0, len(self.menuLines)):
            print (self.menuLines[x])
            
    def printAnyMenu(self, menu):
        for x in range(0, len(menu)):
            print (menu[x])
            
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
        validMenuInput = list(range(1,8)) + [9,10]
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
    autoGenCode = AutoGenCode()
    autoGen = autoGenCode.getAutoGen()
    mainTUI = MainLogic(autoGen)