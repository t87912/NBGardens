# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:06:51 2016

@author: Administrator
"""

# Import modules:
import pymysql
import csv
import sys
from UserStories import AllUserStories

class MySQLDatabase(object):
    """ Database: Holds the database object used for querying, also holds the
        logic for the menus and runs the actual queries. """
    def __init__(self, userLoginDetails, logger, fh, autoGen):
        self.autoGen = autoGen
        self.newMenuOptions = self.autoGen[2]
        self.menuLines = self.autoGen[0]
        self.userStories = self.autoGen[3]
        self.logger = logger
        self.fh = fh # set filehandler, for closing the log file
        self.menuOption = 0
        self.username = userLoginDetails[0]
        self.password = userLoginDetails[1]
        self.backToMain = False
        self.db = None
        self.run_query_obj = AllUserStories.AllUserStories()
#        self.menuLines = ["\nPlease select an option: ",
#                          "User Story Number | Description",
#                          "1. Top salesperson of a given period, based on total cost of their sales during that time",
#                          "2. Which customer has highest spending in given period",
#                          "3. Which customer has spent more than 'x' amount during a given period",
#                          "4. Total spend vs total cost for given time period",
#                          "5. Total return on investment for particular product for given time period",
#                          "6. Average amont of time it takes to fulfill an order during a particular time period",
#                          "12. Check website details for particular product match that is stored in the physical inventory",
#                          "13. Create a graph showing the amount of sales for a particular product over a period of time",
#                          "14. Create a graph showing the amount of sales made by a particular sales person over a period of time",
#                          "16. Create a graph of the number of stock available for a particular product with the number of sales for that particular product over a particular time period",
#                          "\n17. Input a custom SQL query.",
#                          "\n18. Go back to the main menu",
#                          "19. Quit"]

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
            #self.logger.info("Unsuccessful login: %s", self.username)
            return False

    def getDB(self):
        return self.db

    def closeConnection(self):
        self.db.close()

    def methodFinder(self):
        """
        Generates a method to call by using predefined statments with user inputs i.e. <predef mathod tag> + <user menu option number>.
        Constructed string is then used to retrirve an attribute of a class that is identical.
        Inital 'ifs' - inputs uses an instance of obj run_query_obj and runs a user story series if user input matches a list member

        @attention: Previous iteration of this method has been deprecated and since then most methods are called using the combined
        query method named series1 or series2. Only a minority of the superset is used in the intended 'method constructor' form.

        @param:  no params are needed
        @return: a method name to call with appropriate needed params
        """
        self.backToMain = False

        one_param_cases = [12];
        two_param_cases = [1, 2, 4, 6, 13, 16];
        three_param_cases = [3, 5, 14];

        # combined quereies into a method
        if int(self.menuOption) in two_param_cases:
            return self.run_query_obj.userStorySeries1(self.db, False, 0, 0, int(self.menuOption))
        elif int(self.menuOption) in three_param_cases:
            return self.run_query_obj.userStorySeries2(self.db, False, 0, 0, 0, int(self.menuOption))
        elif int(self.menuOption) in self.newMenuOptions:
            print ("In new menu options!")
            print (self.menuOption)
            query_number = 0
            for x in range(0, len(self.newMenuOptions)):
                if (self.menuOption == self.newMenuOptions[x]):
                    query_number = x
            self.run_query_obj.newUserStory(self.db, False, self.autoGen, query_number)
        elif (int(self.menuOption) == self.autoGen[1][0]):
            self.customQuery(False, 0)
        elif (int(self.menuOption) == self.autoGen[1][1]):
            print ("Returning to main menu...")
            self.backToMain = True
        elif (int(self.menuOption) == self.autoGen[1][2]):
            self.exitProgram()
        else:
            method_name = 'userStory' + str(self.menuOption)
            # use string as the method name and call it else return alt method
            find_method = getattr(self.run_query_obj, method_name)
            # ifs to provide additional params should the user cases require them
            if int(self.menuOption) in one_param_cases:
                return find_method(self.db, False, 0)


    def mainLogic(self):
        """ mainLogic: Holds the logic for the main menu. """
        valid = False
        while (not valid):
            self.printMenu()
            valid = self.getMenuInput()
            if (valid):
                self.methodFinder()
                if (self.backToMain):
                    valid = True
                else:
                    valid = False

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
        validInputList = list(range(1, 7)) + list(range(12, 15)) + [16] + self.autoGen[1] + self.autoGen[2]

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
        with open("assets/output.csv", "w") as f:
            # Last 2 parameters below to remove empty line between each line
            writer = csv.writer(f, sys.stdout, lineterminator='\n')
            for z in range(0, len(forCSV)):
                writer.writerow(forCSV[z])

    def customQuery(self, GUI, query):
        """ customeQuery: Executes user custom query. Need validation here. """
        if (not GUI):
            query = input("Input SQL query: ")

        self.logger.info('Custom SQL query: %s', query)
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