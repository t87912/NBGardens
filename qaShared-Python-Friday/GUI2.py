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

        self.createInitialGUI()

    def createInitialGUI(self):
        """ createInitialGUI: This method is called from __init__ and creates
            the initial GUI, showing just the login/logout buttons and the
            username/password entry boxes. """


        #GUI menu
        menu = tk.Menu(root)
        root.config(menu = menu)

        #GUI submenus
        fileSub = tk.Menu(menu)
        menu.add_cascade(label = "File", menu = fileSub)
        fileSub.add_command(label = "New")
        fileSub.add_command(label = "Save")
        fileSub.add_command(label = "Open")

        editSub = tk.Menu(menu)
        menu.add_cascade(label = "Edit", menu = editSub)
        editSub.add_command(label = "Copy")
        editSub.add_command(label = "Paste")
        editSub.add_command(label = "Select All")

        viewSub = tk.Menu(menu)
        menu.add_cascade(label = "View", menu = viewSub)
        viewSub.add_command(label = "Toggle full screen")

        dataSub = tk.Menu(menu)
        menu.add_cascade(label = "Data", menu = dataSub)
        dataSub.add_command(label = "Export as .csv")

        graphSub = tk.Menu(menu)
        menu.add_cascade(label = "Graph", menu = graphSub)
        graphSub.add_command(label = "Export as .png")

        menu.add_command(label = "Logout")

        outputFrame = tk.Frame(root,height=30,width = 60)
        outputFrame.pack(side = TOP)

        outputBox = tk.Text(outputFrame,width=65,height=20)
        outputBox.pack(side = LEFT)
        outputBox.config(state = DISABLED)

        #input frame
        inputFrame = tk.Frame(root,height=300,width = 600)
        inputFrame.pack(fill = 'both')


        #Tabs
        tabControl = ttk.Notebook(inputFrame)

        tab1 = tk.Frame(tabControl)
        tabControl.add(tab1, text = 'Customer')
        tabControl.pack(expand=1, fill="both")

        tk.Label(tab1, text="Query the database for Customers").grid(column =1, row=0)

        tab2 = tk.Frame(tabControl)
        tabControl.add(tab2, text='Orders')

        tk.Label(tab2, text="Query the database for Orders").grid(column =1, row=0)

        tab3 = tk.Frame(tabControl)
        tabControl.add(tab3, text='Products')

        tk.Label(tab3, text="Query the database for Products").grid(column =1, row=0)

        tab4 = tk.Frame(tabControl)
        tabControl.add(tab4, text='Employee')

        tk.Label(tab4, text="Query the database for Employees").grid(column =1, row=0)

        #Status bar
        status = tk.Label(root, text = "ready", bd = 1, relief = "sunken", anchor = W)
        status.pack(side = BOTTOM, fill = X)


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

    def callCSV(self):
        """ callCSV: This just calls the external method exportToCSV. There is
            a bug preventing it being called directly from the button press,
            so the press goes here before calling the external function. """

    def showGraph(self):
        """ showGraph: This method will open a new top level window and display
            a graph image. It simply shows the image file called graph.png
            which is stored in /assets. This will be the most recent graph
            that has been created. """

    def dropDownInput(self, value):
        """ dropDownInput: This method is called whenever the user selects a
            menu option from the drop down menu. It deletes the contents of the
            input boxes, replaces them with a prompt (e.g. date/prodID).
            Depending on the userStory number, input boxes will be 'unlocked'. """

    def submitUserStory(self):
        """ submitUserStory: This method is called when the submit button is
            pressed. It uses self.userStory (number of drop down menu that
            is currently selected) to decide the values of which input boxes
            it needs to retrieve, before passing them in as parameters to one
            of the user stories. The connection to MySQL or MongoDB is passed
            in as the first parameter. The results are assigned to toPrint,
            which is passed in to the self.outputQueryResult method. """

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

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication = MainApplication(root)
    root.geometry('600x600')
    root.wm_title("NB Gardens - ASAS")
    root.mainloop()
#print ("hello")
#root = tk.Tk()
#login = tk.Tk()
#login.title("NB Gardens")
#login.geometry("600x600")
#root.title("NB Gardens")
#root.geometry("700x600")
