# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:13:49 2016

@author: Administrator
"""

# Import modules:
import tkinter as tk

# Import other python class files:
from sqlDatabase.MySQLDatabase import MySQLDatabase
from mongoDatabase.MongoDatabase import MongoDatabase

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

# Tkinter fonts:
LARGE_FONT= ("Verdana", 12)
MED_FONT = ("Verdana", 10)

class MainApplication(tk.Frame):
    """ MainApplication: Provides the main logic for the GUI, allows the
        user to log in with user/password, before executing SQL queries. """
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.firstClick = True
        self.userStory = 0
        self.menuLines = ["\nPlease select an option: ",
                          "1. Input a custom SQL query.",
                          "2. Print a list of customers, products and orders",
                          "3. Show Ratings for a product over time",
                          "8. Go back to the main menu"]
        
        self.nbTitle = tk.Label(self.master, text = "\nWelcome to the NB Gardens Accounts and Sales Analytics System (ASAS)", font = LARGE_FONT)
        self.nbTitle.grid(row = 0, columnspan = 16, padx = 300) # Pad to move title to centre
        
        self.mainText = tk.Label(self.master, text = "\nWhat would you like to do?\n\n", font = LARGE_FONT)
        self.mainText.grid(row=1,columnspan=16)
        
        self.sqlLabel = tk.Label(self.master, text = "Query the MySQL database:\n\n\n\n", font = MED_FONT)
        self.sqlLabel.grid(row=2,columnspan=6)
        
        self.usernameLabel = tk.Label(self.master, text = "Username: ").grid(row=2, column=0)

        self.usernameEntry = tk.Entry(self.master)
        self.usernameEntry.grid(row=2,column=1)
        
        self.passwordLabel = tk.Label(self.master, text = "Password: ").grid(row=3,column=0)
        
        self.passwordEntry = tk.Entry(self.master, show="*")
        self.passwordEntry.grid(row=3,column=1)
        
        self.submitButton = tk.Button(self.master, text = "Login", command = self.submit)
        self.submitButton.grid(row=2,column=2, columnspan=2, rowspan=2)
        
        self.logoutButton = tk.Button(self.master, text = "Logout", state = 'disabled', command = self.logout)
        self.logoutButton.grid(row=2,column=3, columnspan=2, rowspan=2)
        
        self.loginStatusLabel = tk.Label(self.master, text = "\nLogin Status: Not logged in\n")
        self.loginStatusLabel.grid(row=4, column=0, columnspan=2)
        
    def submit(self):
        """ submit: Submits the user/password to MySQL database, will update
            the loginStatus text on login or failed login. Once the user is
            logged in, the login buttons are disabled. """
        username = self.usernameEntry.get()
        password = self.passwordEntry.get()
        userLoginDetails = [username, password]
        self.db = MySQLDatabase(userLoginDetails)
        validLogin = self.db.login() # Returns bool True if valid
        self.dbConn = self.db.getDB()
        self.mongoDB = MongoDatabase()
        
        if (validLogin):
            # Change status of buttons/entry widgets on login
            self.loginStatusLabel.config(text = '\nLogin Status: Logged in\n')
            self.submitButton.config(state="disabled")
            self.logoutButton.config(state="active")
            self.passwordEntry.configure(state="disabled")
            self.usernameEntry.configure(state="disabled")
            
            # Show additional GUI options upon login
            self.customQueryLabel = tk.Label(self.master, text = "Enter a custom SQL/Mongo query: ")
            self.customQueryLabel.grid(row=8, column=0, columnspan = 1)

            self.customQueryEntry = tk.Entry(self.master, width = 30)
            self.customQueryEntry.grid(row=8,column=1, columnspan=3)
            self.customQueryEntry.insert(0, 'Enter the custom query...')
            self.customQueryEntry.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customQueryEntry"))
            
            self.customQueryButton = tk.Button(self.master, text = "Submit SQL", command = self.customSQL)
            self.customQueryButton.grid(row=8,column=3, columnspan=2)
            
            self.customQueryButtonMongo = tk.Button(self.master, text = "Submit MongoDB", command = self.customMongo, width=55)
            self.customQueryButtonMongo.grid(row=8,column=5, columnspan=2)
            
            self.options = [
                           "1. (SQL) Top salesperson of a given period, based on total cost of their sales during that time",
                           "2. (SQL) Which customer has highest spending in given period",
                           "3. (SQL) Which customer has spent more than 'x' amount during a given period",
                           "4. (SQL) Total spend vs total cost for given time period",
                           "5. (SQL) Total return on investment for particular product for given time period",
                           "6. (SQL) Average amont of time it takes to fulfill an order during a particular time period",
                           "7. Average rating a particular customer has given NB Gardens",
                           "8. Average rating a group of customers from particular county has given NB Gardens",
                           "9. Average rating a group of customers from particular demographic (age, gender etc.) has given NB Gardens",
                           "10. Compare average rating given to a product through the website against customer order ratings with that same product included",
                           "11. Customer satisfaction in key areas of the business over a given time period",
                           "12. (SQL) Check website details for particular product match that is stored in the physical inventory",
                           "13. (SQL) Create a graph showing the amount of sales for a particular product over a period of time",
                           "14. (SQL) Create a graph showing the amount of sales made by a particular sales person over a period of time",
                           "15. Create a graph showing the levels of customer satisfaction in a range of areas over a period of time",
                           "16. (SQL) Create a graph of the number of stock available for a particular product with the number of sales for that particular product over a particular time period"
                          ]             
                    
            self.spacerLabel0 = tk.Label(self.master, text = "\n\n").grid(row=11, column=0)

            var = tk.StringVar()
            var.set(self.options[0]) # default value
            self.drop = tk.OptionMenu(self.master, var, *self.options, command=self.dropDownInput)
            self.drop.grid(row=11, column = 0, columnspan=8)
            
            self.spacerLabel1 = tk.Label(self.master, text = "\n").grid(row=12, column=0)
            
            self.queryInputBox1 = tk.Entry(self.master)
            self.queryInputBox1.grid(row=12,column=1)
            
            self.queryInputBox2 = tk.Entry(self.master)
            self.queryInputBox2.grid(row=12,column=2)
            
            self.queryInputBox3 = tk.Entry(self.master)
            self.queryInputBox3.grid(row=12,column=3)
            
            self.submitUserStoryInputs = tk.Button(self.master, text = "Submit", command = self.submitUserStory)
            self.submitUserStoryInputs.grid(row=12,column=4)
            
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
           # self.spacerLabel2 = tk.Label(self.master, text = "\n").grid(row=13, column=0)
            
            self.queryResultBox = tk.Text(self.master)
            self.queryResultBox.grid(row = 14, column = 0, columnspan = 8, rowspan = 4)
        else:
            self.loginStatusLabel.config(text = '\nLogin Status: Error, username or password is incorrect\n')
        
    def onEntryClick(self, event, tkWidgetName):
        """ onEntryClick: onFocus event will delete prompt text in entry box """
        stringToEval = "%s.delete(0, \"end\")" % (tkWidgetName)
        eval(stringToEval)
        
    def dropDownInput(self, value):
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
        elif (self.userStory == 15):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            toPrint = userStory16(self.dbConn, True, fromDate, toDate)
        
        self.outputQueryResult(toPrint) 
        
        self.queryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.queryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.queryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        
        self.queryInputBox1.config(state='disabled')                    
        self.queryInputBox2.config(state='disabled')
        self.queryInputBox3.config(state='disabled')
            
    def logout(self):
        """ logout: Destroys GUI features on logout, changes loginStatus label
            text and enable login button and user/password inputs. """
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
        for i in range(0, len(toPrint)):
            textToEval = "self.queryResultBox.insert('%d.0', \"%s\\n\")" % (i+1, toPrint[i])
            eval(textToEval)
        
if __name__ == "__main__":
    root = tk.Tk()
    MainApplication = MainApplication(root)
    root.geometry('1200x800')
    root.wm_title("NB Gardens - ASAS")
    root.mainloop()