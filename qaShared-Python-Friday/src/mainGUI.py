# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:13:49 2016

@author: Administrator
"""

# Import modules:
import tkinter as tk
import csv
import sys

# Import other python class files:
from sqlDatabase.MySQLDatabase import MySQLDatabase
from mongoDatabase.MongoDatabase import MongoDatabase
from mongoDatabase import MongoQueries

# Import user stories:
from UserStories.userStory1 import userStory1
from UserStories.userStory2 import userStory2
from UserStories.userStory3 import userStory3
from UserStories.userStory4 import userStory4
from UserStories.userStory5 import userStory5
from UserStories.userStory6 import userStory6
from UserStories.userStory7 import userStory7
from UserStories.userStory8 import userStory8
from UserStories.userStory9 import userStory9
from UserStories.userStory10 import userStory10
from UserStories.userStory11 import userStory11
from UserStories.userStory12 import userStory12
from UserStories.userStory13 import userStory13
from UserStories.userStory14 import userStory14
from UserStories.userStory16 import userStory16

# Tkinter fonts:
LARGE_FONT= ("Verdana", 12)
MED_FONT = ("Verdana", 10)

class MainApplication(tk.Frame):
    """ MainApplication: Provides the main logic for the GUI, allows the
        user to log in with user/password, before executing SQL and Mongo
        queries using the userStory drop down menu. The user can also execute
        custom SQL/Mongo queries. """
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.currentQueryResult = [] # Will hold current query for printing
        self.userStory = 0 # Holds userStory number from drop down menu
        self.menuLines = ["\nPlease select an option: ",
                          "1. Input a custom SQL query.",
                          "2. Print a list of customers, products and orders",
                          "3. Show Ratings for a product over time",
                          "8. Go back to the main menu"]           
        self.options = [
                           "1.  (SQL) Top salesperson of a given period, based on total cost of their sales during that time",
                           "2.  (SQL) Which customer has highest spending in given period",
                           "3.  (SQL) Which customer has spent more than 'x' amount during a given period",
                           "4.  (SQL) Total spend vs total cost for given time period",
                           "5.  (SQL) Total return on investment for particular product for given time period",
                           "6.  (SQL) Average amont of time it takes to fulfill an order during a particular time period",
                           "7.  (Mongo) Average rating a particular customer has given NB Gardens",
                           "8.  (Mongo) Average rating a group of customers from particular county has given NB Gardens",
                           "9.  (Mongo) Average rating a group of customers from particular demographic (age, gender etc.) has given NB Gardens",
                           "10. (Mongo) Compare average rating given to a product through the website against customer order ratings with that same product included",
                           "11. (Mongo) Customer satisfaction in key areas of the business over a given time period",
                           "12. (SQL) Check website details for particular product match that is stored in the physical inventory",
                           "13. (SQL) Create a graph showing the amount of sales for a particular product over a period of time",
                           "14. (SQL) Create a graph showing the amount of sales made by a particular sales person over a period of time",
                           "15. (Mongo) Create a graph showing the levels of customer satisfaction in a range of areas over a period of time",
                           "16. (SQL) Create a graph of the number of stock available for a particular product with the number of sales for that particular product over a particular time period"
                          ]  
        self.createInitialGUI()
        
    def createInitialGUI(self):
        """ createInitialGUI: This method is called from __init__ and creates
            the initial GUI, showing just the login/logout buttons and the
            username/password entry boxes. """        
        
        # The welcome message and prompt text
        self.nbTitle = tk.Label(self.master, text = "\nWelcome to the NB Gardens Accounts and Sales Analytics System (ASAS)", font = LARGE_FONT)
        self.nbTitle.grid(row = 0, columnspan = 16, padx = 300) # Pad to move title to centre
        self.mainText = tk.Label(self.master, text = "\nWhat would you like to do?\n\n", font = LARGE_FONT)
        self.mainText.grid(row=1,columnspan=16)
        self.sqlLabel = tk.Label(self.master, text = "Query the MySQL database:\n\n\n\n", font = MED_FONT)
        self.sqlLabel.grid(row=2,columnspan=6)

        # User/passwd labels and entry boxes, submit button:        
        self.usernameLabel = tk.Label(self.master, text = "Username: ").grid(row=2, column=0)
        self.usernameEntry = tk.Entry(self.master)
        self.usernameEntry.grid(row=2,column=1)
        self.passwordLabel = tk.Label(self.master, text = "Password: ").grid(row=3,column=0)
        self.passwordEntry = tk.Entry(self.master, show="*")
        self.passwordEntry.grid(row=3,column=1)
        self.submitButton = tk.Button(self.master, text = "Login", command = self.submit)
        self.submitButton.grid(row=2,column=2, columnspan=2, rowspan=2)
        
        # Login button and login status label:
        self.logoutButton = tk.Button(self.master, text = "Logout", state = 'disabled', command = self.logout)
        self.logoutButton.grid(row=2,column=3, columnspan=2, rowspan=2)
        self.loginStatusLabel = tk.Label(self.master, text = "\nLogin Status: Not logged in\n")
        self.loginStatusLabel.grid(row=4, column=0, columnspan=2)
        
    def submit(self):
        """ submit: Submits the user/password to MySQL database, will update
            the loginStatus text on login or failed login. If the login is
            successful, the onValidLogin method will be called to create the
            rest of the GUI. """   
        # Get the username and password from the entry boxes, put in list:
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        userLoginDetails = [username, password]
        
        # Init MySQLDatabase with login details
        self.db = MySQLDatabase(userLoginDetails)
        
        # Attempt to login, returns true/false if valid/invalid
        validLogin = self.db.login()
        
        # If connection to MySQL made, connect to Mongo
        if (validLogin):
            # Get MySQL connection so it can be passed into some of the Mongo
            # queries that require bits of SQL.
            self.dbConn = self.db.getDB()
            self.mongoDB = MongoDatabase() # Init MongoDB
            
            # Get Mongo connection so it can be passed in to Mongo user stories
            self.conn = self.mongoDB.getConnection()
            self.onValidLogin() # On valid login display rest of GUI:
        else:
            # Change login status label if incorrect login
            self.loginStatusLabel.config(text = '\nLogin Status: Error, username or password is incorrect\n')
            
    def onValidLogin(self):
        """ onValidLogin: This method is called when a successful login is
            made. It creates the rest of the GUI. Login buttons and inputs are
            disabled on login, and the logout button is made active. """
        # Change status of buttons/entry widgets on login
        self.loginStatusLabel.config(text = '\nLogin Status: Logged in\n')
        self.submitButton.config(state="disabled")
        self.logoutButton.config(state="active")
        self.passwordEntry.configure(state="disabled")
        self.usernameEntry.configure(state="disabled")
        
        # Custom query label and input box, bound to remove prompt text:
        self.customQueryLabel = tk.Label(self.master, text = "Enter a custom SQL/Mongo query: ")
        self.customQueryLabel.grid(row=8, column=0, columnspan = 1)
        self.customQueryEntry = tk.Entry(self.master, width = 30)
        self.customQueryEntry.grid(row=8,column=1, columnspan=3)
        self.customQueryEntry.insert(0, 'Enter the custom query...')
        self.customQueryEntry.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customQueryEntry"))
        
        # Submit custom query buttons for Mongo/SQL:
        self.customQueryButton = tk.Button(self.master, text = "Submit SQL", command = self.customSQL)
        self.customQueryButton.grid(row=8,column=3, columnspan=2)
        self.customQueryButtonMongo = tk.Button(self.master, text = "Submit MongoDB", command = self.customMongo, width=55)
        self.customQueryButtonMongo.grid(row=8,column=5, columnspan=2)
        
        # A spacer label to help format the way the GUI displays:
        self.spacerLabel0 = tk.Label(self.master, text = "\n\n").grid(row=11, column=0)
        
        # The drop down menu with the user stories, default value is the
        # first user story, onclick call self.dropDownInput()
        var = tk.StringVar()
        var.set(self.options[0]) # default value
        self.drop = tk.OptionMenu(self.master, var, *self.options, command=self.dropDownInput)
        self.drop.grid(row=11, column = 0, columnspan=8)
        
        # A spacer label to help format the way the GUI displays:
        self.spacerLabel1 = tk.Label(self.master, text = "\n").grid(row=12, column=0)
        
        # Query input boxes:
        self.queryInputBox1 = tk.Entry(self.master)
        self.queryInputBox1.grid(row=12,column=1)
        self.queryInputBox2 = tk.Entry(self.master)
        self.queryInputBox2.grid(row=12,column=2)
        self.queryInputBox3 = tk.Entry(self.master)
        self.queryInputBox3.grid(row=12,column=3)
        
        # The submit user story and export to csv buttons:
        self.submitUserStoryInputs = tk.Button(self.master, text = "Submit", command = self.submitUserStory)
        self.submitUserStoryInputs.grid(row=12,column=4)            
        self.writeToCSVButton = tk.Button(self.master, text = "Export to CSV", command = self.exportToCSV)
        self.writeToCSVButton.grid(row=12,column=5)
        
        # Set prompt text of input boxes:
        self.queryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.queryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.queryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        
        # Bind the input boxes, so on focus remove prompt text:
        self.queryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.queryInputBox1"))
        self.queryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.queryInputBox2"))
        self.queryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.queryInputBox3"))
        
        # Disable the inputs:
        self.queryInputBox1.configure(state="disabled")
        self.queryInputBox2.configure(state="disabled")
        self.queryInputBox3.configure(state="disabled")
        
        # The query results box:
        self.queryResultBox = tk.Text(self.master)
        self.queryResultBox.grid(row = 14, column = 0, columnspan = 8, rowspan = 4)
    
    def onEntryClick(self, event, tkWidgetName):
        """ onEntryClick: onFocus event will delete prompt text in entry box """
        stringToEval = "%s.delete(0, \"end\")" % (tkWidgetName)
        eval(stringToEval)
        
    def dropDownInput(self, value):
        """ dropDownInput: This method is called whenever the user selects a
            menu option from the drop down menu. It deletes the contents of the
            input boxes, replaces them with a prompt (e.g. date/prodID).
            Depending on the userStory number, input boxes will be 'unlocked'. """
        print(value)
        self.queryInputBox1.delete(0, "end")
        self.queryInputBox2.delete(0, "end")
        self.queryInputBox3.delete(0, "end")
        self.queryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.queryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.queryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        self.queryInputBox1.config(state='disabled')                    
        self.queryInputBox2.config(state='disabled')
        self.queryInputBox3.config(state='disabled')
        if (value == self.options[0]):
            self.userStory = 0
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')  
        elif (value == self.options[1]):
            self.userStory = 1
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')
        elif (value == self.options[2]):
            self.userStory = 2
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')
            self.queryInputBox3.config(state='normal')
        elif (value == self.options[3]):
            self.userStory = 3
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')
        elif (value == self.options[4]):
            self.userStory = 4
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')
            self.queryInputBox3.config(state='normal')
        elif (value == self.options[5]):
            self.userStory = 5
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')
        elif (value == self.options[6]): # MONGO - 7
            self.userStory = 6
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox3.config(state='normal')
        elif (value == self.options[7]): # MONGO - 8
            self.userStory = 7
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox3.config(state='normal')   
        elif (value == self.options[8]): # MONGO - 9
            self.userStory = 8
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')
            self.queryInputBox2.config(state='normal')
            self.queryInputBox3.config(state='normal')  
        elif (value == self.options[9]): # MONGO - 10
            self.userStory = 9
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox3.config(state='normal') 
        elif (value == self.options[10]): # MONGO - 11
            self.userStory = 10
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal') 
            self.queryInputBox2.config(state='normal')
        elif (value == self.options[11]):
            self.userStory = 11
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox3.config(state='normal')
        elif (value == self.options[12]):
            self.userStory = 12
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')  
        elif (value == self.options[13]):
            self.userStory = 13
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')
            self.queryInputBox3.config(state='normal')   
        elif (value == self.options[15]):
            self.userStory = 15
            self.queryResultBox.delete('1.0', tk.END)
            self.queryInputBox1.config(state='normal')                    
            self.queryInputBox2.config(state='normal')
            
    def submitUserStory(self):
        """ submitUserStory: This method is called when the submit button is
            pressed. It uses self.userStory (number of drop down menu that
            is currently selected) to decide the values of which input boxes
            it needs to retrieve, before passing them in as parameters to one
            of the user stories. The connection to MySQL or MongoDB is passed
            in as the first parameter. The results are assigned to toPrint,
            which is passed in to the self.outputQueryResult method. """
        if (self.userStory == 0):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory1(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 1):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory2(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 2):
            self.queryResultBox.delete('1.0', tk.END)
            amount = self.queryInputBox3.get()
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory3(self.dbConn, True, amount, fromDate, toDate)
        elif (self.userStory == 3):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory4(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 4):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            productID = self.queryInputBox3.get()
            toPrint = userStory5(self.dbConn, True, fromDate, toDate, productID)
        elif (self.userStory == 5):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory6(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 6): # MONGO - 7
            self.queryResultBox.delete('1.0', tk.END)
            customerID = self.queryInputBox3.get()
            toPrint = userStory7(self.dbConn, self.conn, True, customerID)
        elif (self.userStory == 7): # MONGO - 8
            self.queryResultBox.delete('1.0', tk.END)
            county = self.queryInputBox3.get()
            toPrint = userStory8(self.dbConn, self.conn, True, county)
        elif (self.userStory == 8): # MONGO - 9
            self.queryResultBox.delete('1.0', tk.END)
            gender = self.queryInputBox3.get()
            agemin = self.queryInputBox3.get()
            agemax = self.queryInputBox3.get()
            toPrint = userStory9(self.dbConn, self.conn, True, gender, agemin, agemax)
        elif (self.userStory == 9): # MONGO - 10
            self.queryResultBox.delete('1.0', tk.END)
            productID = self.queryInputBox3.get()
            toPrint = userStory7(self.dbConn, self.conn, True, productID)
        elif (self.userStory == 10): # MONGO - 11
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory7(self.dbConn, self.conn, True, fromDate, toDate)
        elif (self.userStory == 11):
            self.queryResultBox.delete('1.0', tk.END)
            productID = self.queryInputBox3.get()
            toPrint = userStory12(self.dbConn, True, productID)
        elif (self.userStory == 12):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory13(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 13):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            employeeID = self.queryInputBox3.get()
            toPrint = userStory14(self.dbConn, True, fromDate, toDate, employeeID)
        elif (self.userStory == 10): # MONGO - 15
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory7(self.dbConn, self.conn, True, fromDate, toDate)
        elif (self.userStory == 15):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory16(self.dbConn, True, fromDate, toDate)
        
        # Put query result in the GUI text box
        self.outputQueryResult(toPrint) 
        
        # Insert default prompt values back into inputs
        self.queryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.queryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.queryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        
        # Disable the inputs
        self.queryInputBox1.config(state='disabled')                    
        self.queryInputBox2.config(state='disabled')
        self.queryInputBox3.config(state='disabled')
            
    def logout(self):
        """ logout: Destroys GUI features on logout, changes loginStatus label
            text and enable login button and user/password inputs. Also closes
            the connections to Mongo and MySQL. """
        self.loginStatusLabel.config(text = '\nLogin Status: Logged out\n')
        self.submitButton.config(state="active")
        self.logoutButton.config(state="disabled")
        self.passwordEntry.configure(state="normal")
        self.passwordEntry.delete(0, 'end')
        self.usernameEntry.configure(state="normal")
        self.usernameEntry.delete(0, 'end')
        self.customQueryLabel.destroy()
        self.customQueryEntry.destroy()
        self.customQueryButton.destroy()
        self.queryResultBox.destroy()
        self.customQueryButtonMongo.destroy()
        self.drop.destroy()
        self.submitUserStoryInputs.destroy()
        self.queryInputBox1.destroy()
        self.queryInputBox2.destroy()
        self.queryInputBox3.destroy()
        
        # On logout, close the database connections
        self.db.closeConnection()
        self.mongoDB.closeConnection()
        
    def customSQL(self):
        """ customSQL: Allows custom SQL queries to be input, sends user input
            to method in MySQLDatabase, results returned in toPrint. Results
            printed on new lines using eval(). """
        self.queryResultBox.delete('1.0', tk.END)
        query = self.customQueryEntry.get()
        toPrint = self.db.customQuery(True, query)
        self.outputQueryResult(toPrint)
        
    def customMongo(self):
        """ customSQL: Allows custom SQL queries to be input, sends user input
            to method in MySQLDatabase, results returned in toPrint. Results
            printed on new lines using eval(). """
        self.queryResultBox.delete('1.0', tk.END)
        query = self.customQueryEntry.get()
        toPrint = self.mongoDB.customQuery(True, query)
        self.outputQueryResult(toPrint)
            
    def outputQueryResult(self, toPrint):
        """ outputQueryResult: Accepts toPrint parameter which is a list of
            lists containing the query results. This iterates over the list
            and creates a textToEval variable which adds that element of the
            list to the queryResultsBox, incrementing the line it inserts onto
            with each new row. This textToEval is then evaluated."""
        self.currentQueryResult = toPrint # For use when writing to CSV
        for i in range(0, len(toPrint)):
            textToEval = "self.queryResultBox.insert('%d.0', \"%s\\n\")" % (i+1, toPrint[i])
            eval(textToEval)
            
    def exportToCSV(self):
        """ exportToCSV: Writes the contents of the query output results box
            to a CSV file in /Assets called CSV_Output.csv. This method can
            write data with any number of rows and columns, assuming the data
            format is a list of lists, e.g. [[1,2],[3,4],[5,6]] """        
        with open("Assets\\CSV_Output.csv", "w") as csvFile:
            # Remove empty line in between every row when writing to CSV
            writer = csv.writer(csvFile, sys.stdout, lineterminator='\n')
            for row in range(0, len(self.currentQueryResult)):
                writer.writerow(self.currentQueryResult[row])
        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication = MainApplication(root)
    root.geometry('1200x1000')
    root.wm_title("NB Gardens - ASAS")
    root.mainloop()