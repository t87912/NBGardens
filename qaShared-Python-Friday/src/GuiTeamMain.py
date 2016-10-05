# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 15:13:49 2016

@author: Administrator
"""

# Import modules:
from tkinter import *
from tkinter import ttk
import tkinter as tk

# Import other python class files:
from sqlDatabase.MySQLDatabase import MySQLDatabase
from mongoDatabase.MongoDatabase import MongoDatabase
from mongoDatabase import MongoQueries
from exportToCSV import exportToCSV
from assets.JsonWriterTool import TheWriterClass
from assets.TxtWriterTool import writeToTXT
from Logger import Logger

from AutoGenCode import AutoGenCode

from UserStories import AllUserStories

# Import user stories:
#from UserStories.userStory1 import userStory1
#from UserStories.userStory2 import userStory2
#from UserStories.userStory3 import userStory3
#from UserStories.userStory4 import userStory4
#from UserStories.userStory5 import userStory5
#from UserStories.userStory6 import userStory6
#from UserStories.userStory7 import userStory7
#from UserStories.userStory8 import userStory8
#from UserStories.userStory9 import userStory9
#from UserStories.userStory10 import userStory10
#from UserStories.userStory11 import userStory11
#from UserStories.userStory12 import userStory12
#from UserStories.userStory13 import userStory13
#from UserStories.userStory14 import userStory14
#from UserStories.userStory15 import userStory15
#from UserStories.userStory16 import userStory16


class MainApplication(tk.Frame):
    """ MainApplication: Provides the main logic for the GUI, allows the
        user to log in with user/password, before executing SQL and Mongo
        queries using the userStory drop down menu. The user can also execute
        custom SQL/Mongo queries. """

    tabControl = None
    def __init__(self, master, *args, **kwargs):
        self.master = master
        self.autoGen = args[0]
        self.run_query_obj = AllUserStories.AllUserStories()
        # self.run_query_obj.userStorySeries2(self.db, False, 0, 0, 0, int(self.menuOption)) 3
        # self.run_query_obj.userStorySeries1(self.db, False, 0, 0, int(self.menuOption)) 2
        # self.run_query_obj.userStory12(self.db, False, 0)

        self.currentQueryResult = [] # Will hold current query for printing
        self.userStory = 0 # Holds userStory number from drop down menu

        self.customerOptions = [
                           "Highest spending Customer in a given period",
                           "Which customers have spent more than 'x' amount during a given period",
                           "Total spend vs total cost for given time period",
                           "Average rating a Customer has given NB Gardens",
                           "Average rating Customers from a particular county have given NB Gardens",
                           "Average rating a demographic has given NB Gardens",
                           "Customer satisfaction in key areas of the business over a given time period",
                           "Show the customer satisfaction in a range of areas over a period of time (Graph)",
                          ]

        self.orderOptions = [
                           "Average time taken to fulfill orders during a particular time period",
                           "Compare ratings given to a product through the website and by phone",
                           "Customer satisfaction in key areas of the business over a given time period",
                          ]

        self.productOptions = [
                           "Return on investment for a product over a given time period",
                           "Compare ratings given to a product through the website and by phone",
                           "Customer satisfaction in key areas of the business over a given time period",
                           "Get website details for a product that is stored in the physical inventory",
                           "Get the amount of sales for a product over a period of time (Graph)",
                           "Get customer satisfaction in a range of areas over a period of time (Graph)",
                           "Show the stock available for a product and the number of sales over a particular time period (Graph)"
                          ]

        self.employeeOptions = [
                           "Top salesperson of a given period, based on total value of their sales",
                           "Customer satisfaction in key areas of the business over a given time period",
                           "Show the amount of sales made by a particular sales person over a period of time (Graph)",
                           "Show customer satisfaction in a range of areas over a period of time (Graph)",
                          ]

        self.canLogin = False
        self.login()
        self.canLoginTest = self.getter()
        # If connection to MySQL made, connect to Mongo
#        if (self.canLoginTest):
#            # Get MySQL connection so it can be passed into some of the Mongo
#            # queries that require bits of SQL.
#            self.dbConn = self.db.getDB()
#            self.mongoDB = MongoDatabase() # Init MongoDB
#
#            # Get Mongo connection so it can be passed in to Mongo user stories
#            self.conn = self.mongoDB.getConnection()
#            print ("Working")
#            self.createInitialGUI()

    def login(self):
        top = tk.Toplevel()
        top.title("Login")
        usernameLabel = tk.Label(top,text="Username")
        passwordLabel = tk.Label(top,text="Password")
        usernameEntry = tk.Entry(top)
        passwordEntry = tk.Entry(top,show="*")
#        passwordEntry.pack()
#        usernameLabel.pack()
#        passwordLabel.pack()
#        usernameEntry.pack()
        usernameLabel.grid(row=0, sticky=tk.E)
        passwordLabel.grid(row=1, sticky=tk.E)
        usernameEntry.grid(row=0, column=1)
        passwordEntry.grid(row=1, column=1)


        logbtn = tk.Button(top, text="Login", command = lambda: test())
        logbtn.grid(row=2, column=1,columnspan=2)

        def test():
            username = usernameEntry.get()
            password = passwordEntry.get()
            print (username)
            print (password)
            self._login_btn_clickked(top, username, password)
        #msg.pack()

    def _login_btn_clickked(self,top, username, password):
        loggerObject = Logger("GUI") # Init the logger object
        self.logger = loggerObject.getLogger() # Get the logger object
        self.fh = loggerObject.getFileHandler() # Get the logger filehandler
        self.db = MySQLDatabase([username,password], self.logger, self.fh, self.autoGen)
        # Attempt to login, returns true/false if valid/invalid
        self.loginWindowBool = self.db.login()
        print ("Hello")
        print (username)
        print (password)
        if (self.loginWindowBool):
            self.setter()
            top.destroy()
            # Get MySQL connection so it can be passed into some of the Mongo
            # queries that require bits of SQL.
            self.dbConn = self.db.getDB()
            self.mongoDB = MongoDatabase() # Init MongoDB

            # Get Mongo connection so it can be passed in to Mongo user stories
            self.conn = self.mongoDB.getConnection()
            print ("Working")
            self.createInitialGUI()

    def setter(self):
        self.canLogin = True

    def getter(self):
        return self.canLogin

    def createInitialGUI(self):
        """ createInitialGUI: This method is called from __init__ and creates
            the initial GUI, showing just the login/logout buttons and the
            username/password entry boxes. """

        #GUI menu
        self.menu = tk.Menu(root)
        root.config(menu = self.menu)

        #GUI submenus
        editSub = tk.Menu(self.menu, tearoff = False)
        self.menu.add_cascade(label = "Edit", menu = editSub)
        editSub.add_command(label = "Copy", command = self.copy)
        editSub.add_command(label = "Paste", command = self.paste)
        editSub.add_command(label = "Select All")

        viewSub = tk.Menu(self.menu, tearoff = False)
        self.menu.add_cascade(label = "View", menu = viewSub)
        viewSub.add_command(label = "Toggle full screen")
        viewSub.add_command(label = "Bring the Gnome back", command = self.printGnome)

        dataSub = tk.Menu(self.menu, tearoff = False)
        self.menu.add_cascade(label = "Data", menu = dataSub)
        dataSub.add_command(label = "Export as .txt", command = self.callTXT)
        dataSub.add_command(label = "Export as .csv", command = self.callCSV)
        dataSub.add_command(label = "Export as .json", command = self.callJSON)
        
        self.menu.add_command(label = "Help")

        self.menu.add_command(label = "Logout", command = self.logout)

        #Output frame
        self.outputFrame = tk.Frame(root,height=100,width = 100)
        self.outputFrame.pack(side = tk.TOP)

        self.queryResultBox = tk.Text(self.outputFrame,width=79,height=25)
        self.queryResultBox.pack(side = tk.LEFT)
        #self.queryResultBox.config(state = DISABLED)


        #input frame
        self.inputFrame = tk.Frame(root,height=150,width = 600)
        self.inputFrame.pack(fill = 'both')

        self.printGnome()
        
        #Tabs
        tabControl = ttk.Notebook(self.inputFrame) #Tab control

        # ------------------------------------------------------------------------- TAB 1 -------------------------------------------------------------------------

        tab1 = tk.Frame(tabControl) #Tab 1
        tabControl.add(tab1, text = 'Customer')
        tabControl.pack(expand=1, fill="both")

        #Dropdown list
        var = tk.StringVar()
        var.set(self.customerOptions[0])
        self.customerDrop = tk.OptionMenu(tab1, var, *self.customerOptions, command=self.customerDropDownInput)
        self.customerDrop.grid(row=1, column = 0, columnspan=3)

        # Query input boxes:
        tk.Label(tab1, text="Date from:").grid(row = 3, column = 0)
        self.customerQueryInputBox1 = tk.Entry(tab1)
        self.customerQueryInputBox1.grid(row=3,column=1)
        tk.Label(tab1, text="Date to:").grid(row = 4, column = 0)
        self.customerQueryInputBox2 = tk.Entry(tab1)
        self.customerQueryInputBox2.grid(row=4,column=1)
        self.labelTab1 = tk.Label(tab1, text="ID:")
        self.labelTab1.grid(row = 5, column = 0)
        self.customerQueryInputBox3 = tk.Entry(tab1)
        self.customerQueryInputBox3.grid(row=5,column=1)

        #submit button
        self.customerSubmitUserStoryInputs = tk.Button(tab1, text = "Submit", command = self.customerSubmitUserStory)
        self.customerSubmitUserStoryInputs.grid(row=12,column=3)

        # ------------------------------------------------------------------------- TAB 2 -------------------------------------------------------------------------

        tab2 = tk.Frame(tabControl)
        tabControl.add(tab2, text='Orders')

        #Dropdown list
        var = tk.StringVar()
        var.set(self.orderOptions[0])
        self.orderDrop = tk.OptionMenu(tab2, var, *self.orderOptions, command=self.orderDropDownInput)
        self.orderDrop.grid(row=1, column = 0, columnspan=3)

        # Query input boxes:
        tk.Label(tab2, text="Date from:").grid(row = 3, column = 0)
        self.orderQueryInputBox1 = tk.Entry(tab2)
        self.orderQueryInputBox1.grid(row=3,column=1)
        tk.Label(tab2, text="Date to:").grid(row = 4, column = 0)
        self.orderQueryInputBox2 = tk.Entry(tab2)
        self.orderQueryInputBox2.grid(row=4,column=1)
        self.labelTab2 = tk.Label(tab2, text="ID:")
        self.labelTab2.grid(row = 5, column = 0)
        self.orderQueryInputBox3 = tk.Entry(tab2)
        self.orderQueryInputBox3.grid(row=5,column=1)

        #submit button
        self.orderSubmitUserStoryInputs = tk.Button(tab2, text = "Submit", command = self.orderSubmitUserStory)
        self.orderSubmitUserStoryInputs.grid(row=12,column=3)

        # ------------------------------------------------------------------------- TAB 3 -------------------------------------------------------------------------

        tab3 = tk.Frame(tabControl)
        tabControl.add(tab3, text='Products')

        #Dropdown list
        var = tk.StringVar()
        var.set(self.productOptions[0])
        self.productDrop = tk.OptionMenu(tab3, var, *self.productOptions, command=self.productDropDownInput)
        self.productDrop.grid(row=1, column = 0, columnspan=3)

        # Query input boxes:
        tk.Label(tab3, text="Date from:").grid(row = 3, column = 0)
        self.productQueryInputBox1 = tk.Entry(tab3)
        self.productQueryInputBox1.grid(row=3,column=1)
        tk.Label(tab3, text="Date to:").grid(row = 4, column = 0)
        self.productQueryInputBox2 = tk.Entry(tab3)
        self.productQueryInputBox2.grid(row=4,column=1)
        self.labelTab3 = tk.Label(tab3, text="ID:")
        self.labelTab3.grid(row = 5, column = 0)
        self.productQueryInputBox3 = tk.Entry(tab3)
        self.productQueryInputBox3.grid(row=5,column=1)

        #submit button
        self.productSubmitUserStoryInputs = tk.Button(tab3, text = "Submit", command = self.productSubmitUserStory)
        self.productSubmitUserStoryInputs.grid(row=12,column=3)

        # ------------------------------------------------------------------------- TAB 4 -------------------------------------------------------------------------

        tab4 = tk.Frame(tabControl)
        tabControl.add(tab4, text='Employee')

        #Dropdown list
        var = tk.StringVar()
        var.set(self.employeeOptions[0])
        self.employeeDrop = tk.OptionMenu(tab4, var, *self.employeeOptions, command=self.employeeDropDownInput)
        self.employeeDrop.grid(row=1, column = 0, columnspan=3)

        # Query input boxes:
        tk.Label(tab4, text="Date from:").grid(row = 3, column = 0)
        self.employeeQueryInputBox1 = tk.Entry(tab4)
        self.employeeQueryInputBox1.grid(row=3,column=1)
        tk.Label(tab4, text="Date to:").grid(row = 4, column = 0)
        self.employeeQueryInputBox2 = tk.Entry(tab4)
        self.employeeQueryInputBox2.grid(row=4,column=1)
        self.labelTab4 = tk.Label(tab4, text="ID:")
        self.labelTab4.grid(row = 5, column = 0)
        self.employeeQueryInputBox3 = tk.Entry(tab4)
        self.employeeQueryInputBox3.grid(row=5,column=1)

        #submit button
        self.employeeSubmitUserStoryInputs = tk.Button(tab4, text = "Submit", command = self.employeeSubmitUserStory)
        self.employeeSubmitUserStoryInputs.grid(row=12,column=3)


        #Status bar
        self.status = tk.Label(root, text = "ready", bd = 1, relief = "sunken", anchor = W)
        self.status.pack(side = BOTTOM, fill = X)

        #----------------------------------------------------------------------Customer--------------------------------------------------------

        # Set prompt text of Customer input boxes:
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

        #----------------------------------------------------------------------Order--------------------------------------------------------

        # Set prompt text of order input boxes:
        self.orderQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.orderQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.orderQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        self.orderQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.orderQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.orderQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Bind the input boxes, so on focus remove prompt text:
        self.orderQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.orderQueryInputBox1"))
        self.orderQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.orderQueryInputBox2"))
        self.orderQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.orderQueryInputBox3"))

        self.orderQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.orderQueryInputBox1"))
        self.orderQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.orderQueryInputBox2"))
        self.orderQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.orderQueryInputBox3"))

        # Disable the inputs:
        self.orderQueryInputBox1.configure(state="disabled")
        self.orderQueryInputBox2.configure(state="disabled")
        self.orderQueryInputBox3.configure(state="disabled")

        self.orderQueryInputBox1.configure(state="disabled")
        self.orderQueryInputBox2.configure(state="disabled")
        self.orderQueryInputBox3.configure(state="disabled")

        #----------------------------------------------------------------------Products--------------------------------------------------------

        # Set prompt text of product input boxes:
        self.productQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.productQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.productQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        self.orderQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.orderQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.orderQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Bind the input boxes, so on focus remove prompt text:
        self.productQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.productQueryInputBox1"))
        self.productQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.productQueryInputBox2"))
        self.productQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.productQueryInputBox3"))

        self.productQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.productQueryInputBox1"))
        self.productQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.productQueryInputBox2"))
        self.productQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.productQueryInputBox3"))

        # Disable the inputs:
        self.productQueryInputBox1.configure(state="disabled")
        self.productQueryInputBox2.configure(state="disabled")
        self.productQueryInputBox3.configure(state="disabled")

        self.orderQueryInputBox1.configure(state="disabled")
        self.orderQueryInputBox2.configure(state="disabled")
        self.orderQueryInputBox3.configure(state="disabled")


        #----------------------------------------------------------------------employee--------------------------------------------------------

        # Set prompt text of employee input boxes:
        self.employeeQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.employeeQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.employeeQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        self.orderQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.orderQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.orderQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Bind the input boxes, so on focus remove prompt text:
        self.employeeQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.employeeQueryInputBox1"))
        self.employeeQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.employeeQueryInputBox2"))
        self.employeeQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.employeeQueryInputBox3"))

        self.employeeQueryInputBox1.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.employeeQueryInputBox1"))
        self.employeeQueryInputBox2.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.employeeQueryInputBox2"))
        self.employeeQueryInputBox3.bind('<FocusIn>', lambda event: self.onEntryClick(event, "self.employeeQueryInputBox3"))

        # Disable the inputs:
        self.employeeQueryInputBox1.configure(state="disabled")
        self.employeeQueryInputBox2.configure(state="disabled")
        self.employeeQueryInputBox3.configure(state="disabled")

        self.orderQueryInputBox1.configure(state="disabled")
        self.orderQueryInputBox2.configure(state="disabled")
        self.orderQueryInputBox3.configure(state="disabled")
        
        
    def printGnome(self):
        gnome = [["    /  \        "],
                 ["   /   <\|      "],
                 ["  /      \      "],
                 ["  |_.- o-o      "],
                 ["  / C  -._)\\    "],
                 [" / ,        |   "],
                 ["|   `-,_,__,    "],
                 ["(,,)====[_]=|   "],
                 ["   .   ____/    "],
                 ["   | -|-|_      "],
                 ["   |____)_)     "]]
                 
        self.outputQueryResult(gnome)
        
    def copy(self):
        content = self.outputFrame.selection_get()
        root.clipboard_clear()
        root.clipboard_append(content)
        
    def paste(self):
        content = root.clipboard_get()
        print(content)

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
    
    def callTXT(self):
        """ callTXT: This just calls the external method exportToTXT. There is
            a bug preventing it being called directly from the button press,
            so the press goes here before calling the external function. """
        #writeToTXT().writeToFile(self.currentQueryResult)
        writeToTXT(self.currentQueryResult)
            
        
    def callCSV(self):
        """ callCSV: This just calls the external method exportToCSV. There is
            a bug preventing it being called directly from the button press,
            so the press goes here before calling the external function. """
        exportToCSV(self.currentQueryResult)
        
    def callJSON(self):
        TheWriterClass().writeToFile(self.currentQueryResult)



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

        if (value == self.customerOptions[0]):
            self.userStory = 1
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.customerOptions[1]):
            self.userStory = 2
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
            self.customerQueryInputBox3.config(state='normal')
            self.labelTab1.config(text='Value:')
        elif (value == self.customerOptions[2]):
            self.userStory = 3
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.customerOptions[3]): # MONGO - 7
            self.userStory = 6
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox3.config(state='normal')
            self.labelTab1.config(text='Customer ID:')
        elif (value == self.customerOptions[4]): # MONGO - 8
            self.userStory = 7
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox3.config(state='normal')
            self.labelTab1.config(text='Country:')
        elif (value == self.customerOptions[5]): # MONGO - 9
            self.userStory = 8
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
            self.customerQueryInputBox3.config(state='normal')
            self.labelTab1.config(text='Demographic:')
        elif (value == self.customerOptions[6]): # MONGO - 11
            self.userStory = 10
            self.queryResultBox.delete('1.0', tk.END)
            self.customerQueryInputBox1.config(state='normal')
            self.customerQueryInputBox2.config(state='normal')
        elif (value == self.customerOptions[7]):
            self.userStory = 14
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

        if (value == self.orderOptions[0]):
            self.userStory = 5
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')
        elif (value == self.orderOptions[1]): # MONGO - 10
            self.userStory = 9
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox3.config(state='normal')
            self.labelTab2.config(text='Product ID:')
        elif (value == self.orderOptions[2]): # MONGO - 11
            self.userStory = 10
            self.queryResultBox.delete('1.0', tk.END)
            self.orderQueryInputBox1.config(state='normal')
            self.orderQueryInputBox2.config(state='normal')


    def productDropDownInput(self, value):
        """ dropDownInput: This method is called whenever the user selects a
            menu option from the drop down menu. It deletes the contents of the
            input boxes, replaces them with a prompt (e.g. date/prodID).
            Depending on the userStory number, input boxes will be 'unlocked'. """
        print(value)
        self.productQueryInputBox1.delete(0, "end")
        self.productQueryInputBox2.delete(0, "end")
        self.productQueryInputBox3.delete(0, "end")
        self.productQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.productQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.productQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        self.productQueryInputBox1.config(state='disabled')
        self.productQueryInputBox2.config(state='disabled')
        self.productQueryInputBox3.config(state='disabled')

        if (value == self.productOptions[0]):
            self.userStory = 4
            self.queryResultBox.delete('1.0', tk.END)
            self.productQueryInputBox1.config(state='normal')
            self.productQueryInputBox2.config(state='normal')
            self.productQueryInputBox3.config(state='normal')
            self.labelTab3.config(text='Product ID:')
        elif (value == self.productOptions[1]): # MONGO - 10
            self.userStory = 9
            self.queryResultBox.delete('1.0', tk.END)
            self.productQueryInputBox3.config(state='normal')
            self.labelTab3.config(text='Product ID:')
        elif (value == self.productOptions[2]): # MONGO - 11
            self.userStory = 10
            self.queryResultBox.delete('1.0', tk.END)
            self.productQueryInputBox1.config(state='normal')
            self.productQueryInputBox2.config(state='normal')
        elif (value == self.productOptions[3]):
            self.userStory = 11
            self.queryResultBox.delete('1.0', tk.END)
            self.productQueryInputBox3.config(state='normal')
            self.labelTab3.config(text='Product ID:')
        elif (value == self.productOptions[4]):
            self.userStory = 12
            self.queryResultBox.delete('1.0', tk.END)
            self.productQueryInputBox1.config(state='normal')
            self.productQueryInputBox2.config(state='normal')
        elif (value == self.productOptions[5]):
            self.userStory = 14
            self.queryResultBox.delete('1.0', tk.END)
            self.productQueryInputBox1.config(state='normal')
            self.productQueryInputBox2.config(state='normal')
        elif (value == self.productOptions[6]):
            self.userStory = 15
            self.queryResultBox.delete('1.0', tk.END)
            self.productQueryInputBox1.config(state='normal')
            self.productQueryInputBox2.config(state='normal')

    def employeeDropDownInput(self, value):
        """ dropDownInput: This method is called whenever the user selects a
            menu option from the drop down menu. It deletes the contents of the
            input boxes, replaces them with a prompt (e.g. date/prodID).
            Depending on the userStory number, input boxes will be 'unlocked'. """
        print(value)
        self.employeeQueryInputBox1.delete(0, "end")
        self.employeeQueryInputBox2.delete(0, "end")
        self.employeeQueryInputBox3.delete(0, "end")
        self.employeeQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.employeeQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.employeeQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')
        self.employeeQueryInputBox1.config(state='disabled')
        self.employeeQueryInputBox2.config(state='disabled')
        self.employeeQueryInputBox3.config(state='disabled')

        if (value == self.employeeOptions[0]):
            self.userStory = 0
            self.queryResultBox.delete('1.0', tk.END)
            self.employeeQueryInputBox1.config(state='normal')
            self.employeeQueryInputBox2.config(state='normal')
        elif (value == self.employeeOptions[1]): # MONGO - 11
            self.userStory = 10
            self.queryResultBox.delete('1.0', tk.END)
            self.employeeQueryInputBox1.config(state='normal')
            self.employeeQueryInputBox2.config(state='normal')
        elif (value == self.employeeOptions[2]):
            self.userStory = 13
            self.queryResultBox.delete('1.0', tk.END)
            self.employeeQueryInputBox1.config(state='normal')
            self.employeeQueryInputBox2.config(state='normal')
            self.employeeQueryInputBox3.config(state='normal')
            self.labelTab4.config(text='Employee ID:')
        elif (value == self.employeeOptions[3]):
            self.userStory = 14
            self.queryResultBox.delete('1.0', tk.END)
            self.employeeQueryInputBox1.config(state='normal')
            self.employeeQueryInputBox2.config(state='normal')


    def customerSubmitUserStory(self):
        """ submitUserStory: This method is called when the submit button is
            pressed. It uses self.userStory (number of drop down menu that
            is currently selected) to decide the values of which input boxes
            it needs to retrieve, before passing them in as parameters to one
            of the user stories. The connection to MySQL or MongoDB is passed
            in as the first parameter. The results are assigned to toPrint,
            which is passed in to the self.outputQueryResult method. """
        if (self.userStory == 1):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            #toPrint = userStory2(self.dbConn, True, fromDate, toDate)
            toPrint = self.run_query_obj.userStorySeries1(self.dbConn, True, fromDate, toDate, 2)
        elif (self.userStory == 2):
            self.queryResultBox.delete('1.0', tk.END)
            amount = self.customerQueryInputBox3.get()
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            #toPrint = userStory3(self.dbConn, True, amount, fromDate, toDate)
            toPrint = self.run_query_obj.userStorySeries2(self.dbConn, True, fromDate, toDate, amount, 3)
        elif (self.userStory == 3):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            #toPrint = userStory4(self.dbConn, True, fromDate, toDate)
            toPrint = self.run_query_obj.userStorySeries1(self.dbConn, True, fromDate, toDate, 4)
        elif (self.userStory == 6): # MONGO - 7
            self.queryResultBox.delete('1.0', tk.END)
            customerID = self.customerQueryInputBox3.get()
            toPrint = self.run_query_obj.mongoStory1(self.dbConn, self.conn, True, customerID)
            #toPrint = userStory7(self.dbConn, self.conn, True, customerID)
        elif (self.userStory == 7): # MONGO - 8
            self.queryResultBox.delete('1.0', tk.END)
            county = self.customerQueryInputBox3.get()
            #toPrint = userStory8(self.dbConn, self.conn, True, county)
            toPrint = self.run_query_obj.mongoStory2(self.dbConn, self.conn, True, county)
        elif (self.userStory == 8): # MONGO - 9
            self.queryResultBox.delete('1.0', tk.END)
            gender = self.customerQueryInputBox1.get()
            agemin = self.customerQueryInputBox2.get()
            agemax = self.customerQueryInputBox3.get()
            #toPrint = userStory9(self.dbConn, self.conn, True, gender, agemin, agemax)
            toPrint = self.run_query_obj.mongoStory3(self.dbConn, self.conn, True, gender, agemin, agemax)
        elif (self.userStory == 10): # MONGO - 11
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            #toPrint = userStory11(self.dbConn, self.conn, True, fromDate, toDate)
            toPrint = self.run_query_obj.mongoStory5(self.dbConn, self.conn, True, fromDate, toDate)
        elif (self.userStory == 14): # MONGO - 15
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.customerQueryInputBox1.get()
            toDate = self.customerQueryInputBox2.get()
            #toPrint = userStory15(self.dbConn, self.conn, True, fromDate, toDate)
            toPrint = self.run_query_obj.mongoStory6(self.dbConn, self.conn, True, fromDate, toDate)

        # Put query result in the GUI text box
        self.outputQueryResult(toPrint)

        # Insert default prompt values back into inputs
        self.customerQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.customerQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.customerQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Disable the inputs
        self.customerQueryInputBox1.config(state='disabled')
        self.customerQueryInputBox2.config(state='disabled')
        self.customerQueryInputBox3.config(state='disabled')

    def orderSubmitUserStory(self):
        """ submitUserStory: This method is called when the submit button is
            pressed. It uses self.userStory (number of drop down menu that
            is currently selected) to decide the values of which input boxes
            it needs to retrieve, before passing them in as parameters to one
            of the user stories. The connection to MySQL or MongoDB is passed
            in as the first parameter. The results are assigned to toPrint,
            which is passed in to the self.outputQueryResult method. """

        if (self.userStory == 5):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.orderQueryInputBox1.get()
            toDate = self.orderQueryInputBox2.get()
            #toPrint = userStory6(self.dbConn, True, fromDate, toDate)
            toPrint = self.run_query_obj.userStorySeries1(self.dbConn, True, fromDate, toDate, 6)
        elif (self.userStory == 9): # MONGO - 10
            self.queryResultBox.delete('1.0', tk.END)
            productID = self.orderQueryInputBox3.get()
            #toPrint = userStory10(self.dbConn, self.conn, True, productID)
            toPrint = self.run_query_obj.mongoStory4(self.dbConn, self.conn, True, productID)
        elif (self.userStory == 10): # MONGO - 11
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.orderQueryInputBox1.get()
            toDate = self.orderQueryInputBox2.get()
            #toPrint = userStory11(self.dbConn, self.conn, True, fromDate, toDate)
            toPrint = self.run_query_obj.mongoStory5(self.dbConn, self.conn, True, fromDate, toDate)


        # Put query result in the GUI text box
        self.outputQueryResult(toPrint)

        # Insert default prompt values back into inputs
        self.orderInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.orderQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.orderQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Disable the inputs
        self.orderQueryInputBox1.config(state='disabled')
        self.orderQueryInputBox2.config(state='disabled')
        self.orderQueryInputBox3.config(state='disabled')

    def productSubmitUserStory(self):
        """ submitUserStory: This method is called when the submit button is
            pressed. It uses self.userStory (number of drop down menu that
            is currently selected) to decide the values of which input boxes
            it needs to retrieve, before passing them in as parameters to one
            of the user stories. The connection to MySQL or MongoDB is passed
            in as the first parameter. The results are assigned to toPrint,
            which is passed in to the self.outputQueryResult method. """

        if (self.userStory == 4):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.productQueryInputBox1.get()
            toDate = self.productQueryInputBox2.get()
            productID = self.productQueryInputBox3.get()
            #toPrint = userStory5(self.dbConn, True, fromDate, toDate, productID)
            toPrint = self.run_query_obj.userStorySeries2(self.dbConn, True, fromDate, toDate, productID, 5)
        elif (self.userStory == 9): # MONGO - 10
            self.queryResultBox.delete('1.0', tk.END)
            productID = self.productQueryInputBox3.get()
            #toPrint = userStory10(self.dbConn, self.conn, True, productID)
            toPrint = self.run_query_obj.mongoStory4(self.dbConn, self.conn, True, productID)
        elif (self.userStory == 10): # MONGO - 11
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.productQueryInputBox1.get()
            toDate = self.productQueryInputBox2.get()
            #toPrint = userStory11(self.dbConn, self.conn, True, fromDate, toDate)
            toPrint = self.run_query_obj.mongoStory5(self.dbConn, self.conn, True, fromDate, toDate)
        elif (self.userStory == 11):
            self.queryResultBox.delete('1.0', tk.END)
            productID = self.productQueryInputBox3.get()
            #toPrint = userStory12(self.dbConn, True, productID)
            toPrint = self.run_query_obj.userStory12(self.dbConn, True, productID)
        elif (self.userStory == 12):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.productQueryInputBox1.get()
            toDate = self.productQueryInputBox2.get()
            #toPrint = userStory13(self.dbConn, True, fromDate, toDate)
            toPrint = self.run_query_obj.userStorySeries1(self.dbConn, True, fromDate, toDate, 13)
        elif (self.userStory == 14): # MONGO - 15
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.productQueryInputBox1.get()
            toDate = self.productQueryInputBox2.get()
            #toPrint = userStory15(self.dbConn, self.conn, True, fromDate, toDate)
            toPrint = self.run_query_obj.mongoStory6(self.dbConn, self.conn, True, fromDate, toDate)
        elif (self.userStory == 15):
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.productQueryInputBox1.get()
            toDate = self.productQueryInputBox2.get()
            #toPrint = userStory16(self.dbConn, True, fromDate, toDate)
            toPrint = self.run_query_obj.userStorySeries1(self.dbConn, True, fromDate, toDate, 16)

        # Put query result in the GUI text box
        self.outputQueryResult(toPrint)

        # Insert default prompt values back into inputs
        self.productQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.productQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.productQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Disable the inputs
        self.productQueryInputBox1.config(state='disabled')
        self.productQueryInputBox2.config(state='disabled')
        self.productQueryInputBox3.config(state='disabled')

    def employeeSubmitUserStory(self):
        """ submitUserStory: This method is called when the submit button is
            pressed. It uses self.userStory (number of drop down menu that
            is currently selected) to decide the values of which input boxes
            it needs to retrieve, before passing them in as parameters to one
            of the user stories. The connection to MySQL or MongoDB is passed
            in as the first parameter. The results are assigned to toPrint,
            which is passed in to the self.outputQueryResult method. """
        # 1, 11, 14, 15
        if (self.userStory == 0): # sql 1
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.employeeQueryInputBox1.get()
            toDate = self.employeeQueryInputBox2.get()
            #toPrint = userStory1(self.dbConn, True, fromDate, toDate)
            toPrint = self.run_query_obj.userStorySeries1(self.dbConn, True, fromDate, toDate, 1)

        elif (self.userStory == 10): # MONGO - 11
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.employeeQueryInputBox1.get()
            toDate = self.employeeQueryInputBox2.get()
            #toPrint = userStory11(self.dbConn, self.conn, True, fromDate, toDate)
            toPrint = self.run_query_obj.mongoStory5(self.dbConn, self.conn, True, fromDate, toDate)
        elif (self.userStory == 13): # 14
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.employeeQueryInputBox1.get()
            toDate = self.employeeQueryInputBox2.get()
            employeeID = self.employeeQueryInputBox3.get()
            #toPrint = userStory14(self.dbConn, True, fromDate, toDate, employeeID)
            toPrint = self.run_query_obj.userStorySeries2(self.dbConn, True, fromDate, toDate, employeeID, 14)
        elif (self.userStory == 14): # MONGO - 15
            self.queryResultBox.delete('1.0', tk.END)
            fromDate = self.employeeQueryInputBox1.get()
            toDate = self.employeeQueryInputBox2.get()
            #toPrint = userStory15(self.dbConn, self.conn, True, fromDate, toDate)
            toPrint = self.run_query_obj.mongoStory6(self.dbConn, self.conn, True, fromDate, toDate)


        # Put query result in the GUI text box
        self.outputQueryResult(toPrint)

        # Insert default prompt values back into inputs
        self.employeeQueryInputBox1.insert(0, 'from: YYYY-MM-DD')
        self.employeeQueryInputBox2.insert(0, 'to: YYYY-MM-DD')
        self.employeeQueryInputBox3.insert(0, 'prodID/EmployeeID/Amount')

        # Disable the inputs
        self.employeeQueryInputBox1.config(state='disabled')
        self.employeeQueryInputBox2.config(state='disabled')
        self.employeeQueryInputBox3.config(state='disabled')

    def logout(self):
        """ logout: Destroys GUI features on logout, changes loginStatus label
            text and enable login button and user/password inputs. Also closes
            the connections to Mongo and MySQL. """
        self.canLogin = False
        self.login()
        self.menu.destroy()
        self.outputFrame.destroy()
        self.inputFrame.destroy()
        self.status.destroy()


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
    root.geometry('650x580')
    root.wm_title("NB Gardens - ASAS")
    root.mainloop()
