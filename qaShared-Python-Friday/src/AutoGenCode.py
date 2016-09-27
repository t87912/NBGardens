# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 22:47:29 2016

@author: user
"""

class AutoGenCode(object):
    """ AutoGenCode: This class will auto-generate the code for the ASAS
        backend based upon the contents of a seperate python file containing
        details of new user stories. """
    def __init__(self):
        self.userStories1 = [["%s. Print a list of all products", "SELECT * FROM Product", [0,0,0]],
                            ["%s. Print a list of all products", "SELECT * FROM Product", [0,0,0]],
                            ["%s. Testing 1","SELECT",[0,0,0]],
                            ["%s. Testing 2","SELECT",[0,0,0]],
                            ["%s. Testing 3","SELECT * FROM Product WHERE productID == '%s'",[0,0,1]]]
        self.userStories = []
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
                  "%s. Input a custom SQL query.",
                  "%s. Go back to the main menu",
                  "%s. Quit"]
        self.generateMenuLines()
        self.autoGen = [self.menuLines,self.last3Options, self.newMenuOptions]
        #MainLogic(autoGen)
        #self.generateMainLogic()
        
    def getAutoGen(self):
        return self.autoGen
                  
    def generateMenuLines(self):
        """ generateMenuLines: This method uses the content of self.menuLines
            and appends the titles of new user stories to the menu, before
            the last position. The menu numbers for the new user stories and
            the last 3 items of the menuLines are generated. """
        #lenMenuLines = len(self.menuLines)
        self.last3Options = []
        self.newMenuOptions = []
        
        if (len(self.userStories) == 0):
            for z in range(3, 0, -1):
                self.menuLines[len(self.menuLines)-z] = self.menuLines[len(self.menuLines)-z] % (len(self.menuLines)-z+5)
                self.last3Options.append(len(self.menuLines)-z+5)
            self.newMenuOptions = []
        else:
            for y in range (0, len(self.userStories)):
                self.userStories[y][0] = self.userStories[y][0] % (len(self.menuLines)+2)
                #print (len(self.menuLines)+2)
                self.newMenuOptions.append(len(self.menuLines)+2)
                self.menuLines.insert(len(self.menuLines)-3, self.userStories[y][0])
                
                            
            for z in range(3, 0, -1):
                self.menuLines[len(self.menuLines)-z] = self.menuLines[len(self.menuLines)-z] % (len(self.menuLines)-z+5)
                self.last3Options.append(len(self.menuLines)-z+5)
                
            #for x in range(0, len(self.menuLines)):
             #   print (self.menuLines[x])
            
        #print (self.last3Options)
        #print (self.newMenuOptions)
        
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


    # things that need to be generated:
        # menu printing in sqldb class
        # menu validation in sqldb class
        # calls to user stories in sqldb class