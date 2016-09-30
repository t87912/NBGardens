# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:13:49 2016

@author: Administrator
"""

# Import modules:
from tkinter import *
from tkinter import ttk
import tkinter as tk
import csv
import sys
# Import other python class files:
from sqlDatabase.MySQLDatabase import MySQLDatabase
from mongoDatabase.MongoDatabase import MongoDatabase
from mongoDatabase import MongoQueries
#from exportToCSV import exportToCSV
from Logger import Logger

from AutoGenCode import AutoGenCode

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

    tabControl = None
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.autoGen = args[0]

        self.currentQueryResult = [] # Will hold current query for printing
        self.userStory = 0 # Holds userStory number from drop down menu

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
        loggerObject = Logger("GUI") # Init the logger object
        self.logger = loggerObject.getLogger() # Get the logger object
        self.fh = loggerObject.getFileHandler() # Get the logger filehandler
        self.db = MySQLDatabase(["test","TEST"], self.logger, self.fh, self.autoGen)
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
        self.createInitialGUI()

    def createInitialGUI(self):
        """ createInitialGUI: This method is called from __init__ and creates
            the initial GUI, showing just the login/logout buttons and the
            username/password entry boxes. """

        #GUI menu
        menu = tk.Menu(root)
        root.config(menu = menu)

        #GUI submenus
        fileSub = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = "File", menu = fileSub)
        fileSub.add_command(label = "New")
        fileSub.add_command(label = "Save")
        fileSub.add_command(label = "Open")

        editSub = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = "Edit", menu = editSub)
        editSub.add_command(label = "Copy", command = self.copy)
        editSub.add_command(label = "Paste", command = self.paste)
        editSub.add_command(label = "Select All")

        viewSub = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = "View", menu = viewSub)
        viewSub.add_command(label = "Toggle full screen")

        dataSub = tk.Menu(menu, tearoff = False)
        menu.add_cascade(label = "Data", menu = dataSub)
        dataSub.add_command(label = "Export as .csv")

        menu.add_command(label = "Logout", command = self.logout)

        #Output frame
        self.outputFrame = tk.Frame(root,height=30,width = 60)
        self.outputFrame.pack(side = tk.TOP)

        self.queryResultBox = tk.Text(self.outputFrame,width=65,height=20)
        self.queryResultBox.pack(side = tk.LEFT)
        #self.queryResultBox.config(state = DISABLED)

        #input frame
        inputFrame = tk.Frame(root,height=300,width = 600)
        inputFrame.pack(fill = 'both')


        #Tabs
        tabControl = ttk.Notebook(inputFrame) #Tab control

        # ------------------------------------------------------------------------- TAB 1 -------------------------------------------------------------------------

        tab1 = tk.Frame(tabControl) #Tab 1
        tabControl.add(tab1, text = 'Customer')
        tabControl.pack(expand=1, fill="both")

        #Dropdown list
        var = tk.StringVar()
        var.set(self.options[0])
        self.drop = tk.OptionMenu(tab1, var, *self.options, command=self.customerDropDownInput)
        self.drop.grid(row=1, column = 0, columnspan=3)

        # Query input boxes:
        tk.Label(tab1, text="Date from:").grid(row = 3, column = 0)
        self.customerQueryInputBox1 = tk.Entry(tab1)
        self.customerQueryInputBox1.grid(row=3,column=1)
        tk.Label(tab1, text="Date to:").grid(row = 4, column = 0)
        self.customerQueryInputBox2 = tk.Entry(tab1)
        self.customerQueryInputBox2.grid(row=4,column=1)
        tk.Label(tab1, text="ID:").grid(row = 5, column = 0)
        self.customerQueryInputBox3 = tk.Entry(tab1)
        self.customerQueryInputBox3.grid(row=5,column=1)

        #submit button
        self.submitUserStoryInputs = tk.Button(tab1, text = "Submit", command = self.submitUserStory)
        self.submitUserStoryInputs.grid(row=12,column=3)

        # ------------------------------------------------------------------------- TAB 2 -------------------------------------------------------------------------

        #tab2
        tab2 = tk.Frame(tabControl)
        tabControl.add(tab2, text='Orders')

        #Dropdown list
        var = tk.StringVar()
        var.set(self.options[0])
        self.drop = tk.OptionMenu(tab2, var, *self.options, command=self.orderDropDownInput)
        self.drop.grid(row=1, column = 0, columnspan=3)

        # Query input boxes:
        tk.Label(tab1, text="Date from:").grid(row = 3, column = 0)
        self.orderQueryInputBox1 = tk.Entry(tab2)
        self.orderQueryInputBox1.grid(row=3,column=1)
        tk.Label(tab1, text="Date to:").grid(row = 4, column = 0)
        self.orderQueryInputBox2 = tk.Entry(tab2)
        self.orderQueryInputBox2.grid(row=4,column=1)
        tk.Label(tab1, text="ID:").grid(row = 5, column = 0)
        self.orderQueryInputBox3 = tk.Entry(tab2)
        self.orderQueryInputBox3.grid(row=5,column=1)

        #submit button
        self.submitUserStoryInputs = tk.Button(tab2, text = "Submit", command = self.submitUserStory)
        self.submitUserStoryInputs.grid(row=12,column=3)

        # ------------------------------------------------------------------------- TAB 3 -------------------------------------------------------------------------

        tab3 = tk.Frame(tabControl)
        tabControl.add(tab3, text='Products')

        # ------------------------------------------------------------------------- TAB 4 -------------------------------------------------------------------------

        tab4 = tk.Frame(tabControl)
        tabControl.add(tab4, text='Employee')


        #Status bar
        status = tk.Label(root, text = "ready", bd = 1, relief = "sunken", anchor = W)
        status.pack(side = BOTTOM, fill = X)

        # Set prompt text of input boxes:
        self.customerQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.customerQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.customerQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        self.orderQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.orderQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.orderQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Bind the input boxes, so on focus remove prompt text:
        self.customerQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customerQueryInputBox1"))
        self.customerQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customerQueryInputBox2"))
        self.customerQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customerQueryInputBox3"))

        self.customerQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customerQueryInputBox1"))
        self.customerQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customerQueryInputBox2"))
        self.customerQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.customerQueryInputBox3"))

        # Disable the inputs:
        self.customerQueryInputBox1.configure(state="disabled")
        self.customerQueryInputBox2.configure(state="disabled")
        self.customerQueryInputBox3.configure(state="disabled")

        self.orderQueryInputBox1.configure(state="disabled")
        self.orderQueryInputBox2.configure(state="disabled")
        self.orderQueryInputBox3.configure(state="disabled")

    def copy(self):
        content = self.outputFrame.selection_get()
        root.clipboard_clear()
        root.clipboard_append(content)

    def paste(self):
        t = root.focus_displayof()
        content = root.clipboard_get()
        print(t)


    def createQueryComboBoxOrders(self,tab, row, column, comboValues):
        queryComboBoxFrame = Frame(tab)
        Label(queryComboBoxFrame, text="Choose a query:").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        combobox = ttk.Combobox(queryComboBoxFrame, values = comboValues, width="50")
        combobox.current(0)
        combobox.config(state = 'readonly')
        combobox.grid(row = "0", column = "1")
        B = Button(queryComboBoxFrame,text = "Select Query", command =lambda: self.getEmployeeQueryID(tab,combobox))
        B.grid(row=1)
        queryComboBoxFrame.grid(row=row, column=column)
        queryComboBoxFrame.grid_columnconfigure(0, weight=1)

    def getEmployeeQueryID(self,tab,CB):
        if(CB.current()==0):
            self.us1(tab,0)
        elif(CB.current()==1):
            self.us14(tab,0)


    def submitReq(self,u,fd,td,id,tab):
        self.queryResultBox.delete(1.0,END)
        if(u == 0):
            result = userStory1(self.dbConn, True, fd, td)
            self.outputQueryResult(result)
            self.us1(tab,1)
        if(u == 14):
            result = userStory14(self.dbConn, True, fd, td,id)
            self.outputQueryResult(result)
            self.us14(tab,1)

    def us1(self,tab,delete):
        if (delete == 0):
            userStory = 0
            dateInputFrame = Frame(tab)
            self.startDateEnt = Entry(dateInputFrame)
            self.startDateEnt.grid(row="0", column="1")
            self.startDateEnt.bind('<FocusIn>', lambda event: self.onEntryClick(event,"self.startDateEnt"))
            self.startDateEnt.insert(END, 'From (YYYY-MM-DD)')
            self.endDateEnt = Entry(dateInputFrame)
            self.endDateEnt.insert(END, 'To (YYYY-MM-DD)')
            self.endDateEnt.grid(row="1", column="1")
            self.endDateEnt.bind('<FocusIn>', lambda event: self.onEntryClick(event,"self.endDateEnt"))
            dateInputFrame.grid(row=3)
            fromDate = self.startDateEnt.get()
            toDate = self.endDateEnt.get()
            ok = Button(tab,text = "Perform Query", command =lambda:self.submitReq(userStory,self.startDateEnt.get(),self.endDateEnt.get(),None,tab))
            ok.grid(row="1", column="2")
        else:
            self.startDateEnt.destroy()
            self.endDateEnt.destroy()
    def us14(self,tab,delete):
        if (delete == 0):
            userStory = 14
            dateInputFrame = Frame(tab)
            self.startDateEnt = Entry(dateInputFrame)
            self.startDateEnt.grid(row="0", column="1")
            self.startDateEnt.bind('<FocusIn>', lambda event: self.onEntryClick(event,"self.startDateEnt"))
            self.startDateEnt.insert(END, 'From (YYYY-MM-DD)')
            self.endDateEnt = Entry(dateInputFrame)
            self.endDateEnt.insert(END, 'To (YYYY-MM-DD)')
            self.endDateEnt.grid(row="1", column="1")
            self.endDateEnt.bind('<FocusIn>', lambda event: self.onEntryClick(event,"self.endDateEnt"))
            self.ID = Entry(dateInputFrame)
            self.ID.insert(END, 'Sales ID')
            self.ID.grid(row="2", column="1")
            self.ID.bind('<FocusIn>', lambda event: self.onEntryClick(event,"self.ID"))
            dateInputFrame.grid(row=3)
            fromDate = self.startDateEnt.get()
            toDate = self.endDateEnt.get()
            ok = Button(tab,text = "Perform Query", command =lambda:self.submitReq(userStory,self.startDateEnt.get(),self.endDateEnt.get(),self.ID.get(),tab))
            ok.grid(row="1", column="2")
        else:
            self.startDateEnt.destroy()
            self.endDateEnt.destroy()
            self.ID.destroy()




    def submit(self):
        """ submit: Submits the user/password to MySQL database, will update
            the loginStatus text on login or failed login. If the login is
            successful, the onValidLogin method will be called to create the
            rest of the GUI. """

    def onValidLogin(self):
        """ onValidLogin: This method is called when a successful login is
            made. It creates the rest of the GUI. Login buttons and inputs are
            disabled on login, and the logout button is made active. """

    def onEntryClick(self, event, tkWidgetName):
        """ onEntryClick: onFocus event will delete prompt text in entry box """
        stringToEval = "%s.delete(0, \"end\")" % (tkWidgetName)
        eval(stringToEval)

    def callCSV(self):
        """ callCSV: This just calls the external method exportToCSV. There is
            a bug preventing it being called directly from the button press,
            so the press goes here before calling the external function. """

    def showGraph(self):
        """ showGraph: This method will open a new top level window and display
            a graph image. It simply shows the image file called graph.png
            which is stored in /assets. This will be the most recent graph
            that has been created. """

    def customerDropDownInput(self, value):
        """ dropDownInput: This method is called whenever the user selects a
            menu option from the drop down menu. It deletes the contents of the
            input boxes, replaces them with a prompt (e.g. date/prodID).
            Depending on the userStory number, input boxes will be 'unlocked'. """
        print(value)
        self.customerQueryInputBox1.delete(0, "end")
        self.customerQueryInputBox2.delete(0, "end")
        self.customerQueryInputBox3.delete(0, "end")
        self.customerQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.customerQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.customerQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        self.customerQueryInputBox1.config(state='disabled')
        self.customerQueryInputBox2.config(state='disabled')
        self.customerQueryInputBox3.config(state='disabled')

        if (value == self.options[0]):
            self.userStory = 0
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.options[1]):
            self.userStory = 1
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.options[2]):
            self.userStory = 2
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[3]):
            self.userStory = 3
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.options[4]):
            self.userStory = 4
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[5]):
            self.userStory = 5
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.options[6]): # MONGO - 7
            self.userStory = 6
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[7]): # MONGO - 8
            self.userStory = 7
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[8]): # MONGO - 9
            self.userStory = 8
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[9]): # MONGO - 10
            self.userStory = 9
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[10]): # MONGO - 11
            self.userStory = 10
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.options[11]):
            self.userStory = 11
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[12]):
            self.userStory = 12
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.options[13]):
            self.userStory = 13
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
            self.customerQueryInputBox3.config(state='normal')
        elif (value == self.options[15]):
            self.userStory = 15
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')

    def orderDropDownInput(self, value):
        """ dropDownInput: This method is called whenever the user selects a
            menu option from the drop down menu. It deletes the contents of the
            input boxes, replaces them with a prompt (e.g. date/prodID).
            Depending on the userStory number, input boxes will be 'unlocked'. """
        print(value)
        self.orderQueryInputBox1.delete(0, "end")
        self.orderQueryInputBox2.delete(0, "end")
        self.orderQueryInputBox3.delete(0, "end")
        self.orderQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.orderQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.orderQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        self.orderQueryInputBox1.config(state='disabled')
        self.orderQueryInputBox2.config(state='disabled')
        self.orderQueryInputBox3.config(state='disabled')

        if (value == self.options[0]):
            self.userStory = 0
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
        elif (value == self.options[1]):
            self.userStory = 1
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
        elif (value == self.options[2]):
            self.userStory = 2
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[3]):
            self.userStory = 3
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
        elif (value == self.options[4]):
            self.userStory = 4
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[5]):
            self.userStory = 5
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
        elif (value == self.options[6]): # MONGO - 7
            self.userStory = 6
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[7]): # MONGO - 8
            self.userStory = 7
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[8]): # MONGO - 9
            self.userStory = 8
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[9]): # MONGO - 10
            self.userStory = 9
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[10]): # MONGO - 11
            self.userStory = 10
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
        elif (value == self.options[11]):
            self.userStory = 11
            self.orderQueryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[12]):
            self.userStory = 12
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
        elif (value == self.options[13]):
            self.userStory = 13
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
            self.orderQueryInputBox3.config(state='normal')
        elif (value == self.options[15]):
            self.userStory = 15
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')

    def customerSubmitUserStory(self):
        """ submitUserStory: This method is called when the submit button is
            pressed. It uses self.userStory (number of drop down menu that
            is currently selected) to decide the values of which input boxes
            it needs to retrieve, before passing them in as parameters to one
            of the user stories. The connection to MySQL or MongoDB is passed
            in as the first parameter. The results are assigned to toPrint,
            which is passed in to the self.outputQueryResult method. """
        if (self.userStory == 0):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            toPrint = userStory1(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 1):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            toPrint = userStory2(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 2):
            self.queryResultBox.delete('1.0', tk.END)
            amount = self.customerQueryInputBox3.get()
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            toPrint = userStory3(self.dbConn, True, amount, fromDate, toDate)
        elif (self.userStory == 3):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            toPrint = userStory4(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 4):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            productID = self.customerQueryInputBox3.get()
            toPrint = userStory5(self.dbConn, True, fromDate, toDate, productID)
        elif (self.userStory == 5):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            toPrint = userStory6(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 6): # MONGO - 7
            self.queryResultBox.delete('1.0', tk.END)
            customerID = self.customerQueryInputBox3.get()
            toPrint = userStory7(self.dbConn, self.conn, True, customerID)
        elif (self.userStory == 7): # MONGO - 8
            self.queryResultBox.delete('1.0', tk.END)
            county = self.customerQueryInputBox3.get()
            toPrint = userStory8(self.dbConn, self.conn, True, county)
        elif (self.userStory == 8): # MONGO - 9
            self.queryResultBox.delete('1.0', tk.END)
            gender = self.customerQueryInputBox3.get()
            agemin = self.customerQueryInputBox3.get()
            agemax = self.customerQueryInputBox3.get()
            toPrint = userStory9(self.dbConn, self.conn, True, gender, agemin, agemax)
        elif (self.userStory == 9): # MONGO - 10
            self.queryResultBox.delete('1.0', tk.END)
            productID = self.customerQueryInputBox3.get()
            toPrint = userStory7(self.dbConn, self.conn, True, productID)
        elif (self.userStory == 10): # MONGO - 11
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            toPrint = userStory7(self.dbConn, self.conn, True, fromDate, toDate)
        elif (self.userStory == 11):
            self.queryResultBox.delete('1.0', tk.END)
            productID = self.customerQueryInputBox3.get()
            toPrint = userStory12(self.dbConn, True, productID)
        elif (self.userStory == 12):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            toPrint = userStory13(self.dbConn, True, fromDate, toDate)
        elif (self.userStory == 13):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.queryInputBox1.get()
            toDate = self.queryInputBox2.get()
            employeeID = self.queryInputBox3.get()
            toPrint = userStory14(self.dbConn, True, fromDate, toDate, employeeID)
        elif (self.userStory == 14): # MONGO - 15
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


    def customSQL(self):
        """ customSQL: Allows custom SQL queries to be input, sends user input
            to method in MySQLDatabase, results returned in toPrint. Results
            printed on new lines using eval(). """


    def customMongo(self):
        """ customSQL: Allows custom SQL queries to be input, sends user input
            to method in MySQLDatabase, results returned in toPrint. Results
            printed on new lines using eval(). """


    def outputQueryResult(self, toPrint):
        """ outputQueryResult: Accepts toPrint parameter which is a list of
            lists containing the query results. This iterates over the list
            and creates a textToEval variable which adds that element of the
            list to the queryResultsBox, incrementing the line it inserts onto
            with each new row. This textToEval is then evaluated."""
        self.currentQueryResult = toPrint # For use when writing to CSV
        # queryResultBox
        for i in range(0, len(toPrint)):
            textToEval = "self.queryResultBox.insert('%d.0', \"%s\\n\")" % (i+1, toPrint[i])
            eval(textToEval)

if __name__ == "__main__":
    autoGenCode = AutoGenCode()
    autoGen = autoGenCode.getAutoGen()
    root = tk.Tk()
    MainApplication = MainApplication(root, autoGen)
    root.geometry('600x600')
    root.wm_title("NB Gardens - ASAS")
    root.mainloop()
