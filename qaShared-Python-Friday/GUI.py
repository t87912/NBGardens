from tkinter import *
from tkinter import ttk
import GUIlogin


class main():
    #Setting up main window
    root = Tk()
    login = Tk()
    login.title("NB Gardens")
    login.geometry("600x600")
    root.title("NB Gardens")
    root.geometry("600x600")

    #output frame
    outputFrame = Frame(root,height=30,width = 60)
    outputFrame.pack(side = TOP)

    outputBox = Text(outputFrame,width=40,height=20)
    outputBox.pack(side = LEFT)
    outputBox.config(state = DISABLED)

    graphBox = Text(outputFrame,width=40,height=20)
    graphBox.pack(side = LEFT)

    #input frame
    inputFrame = Frame(root,height=300,width = 600)
    inputFrame.pack(fill = 'both')

    #GUI menu
    menu = Menu(root)
    root.config(menu = menu)

    #GUI submenus
    fileSub = Menu(menu)
    menu.add_cascade(label = "File", menu = fileSub)
    fileSub.add_command(label = "New")
    fileSub.add_command(label = "Save")
    fileSub.add_command(label = "Open")
    fileSub.add_command(label = "Export")

    #Tabs
    tabControl = ttk.Notebook(inputFrame)

    tab1 = ttk.Frame(tabControl)
    tabControl.add(tab1, text = 'Customer')
    tabControl.pack(expand=1, fill="both")

    ttk.Label(tab1, text="Customer query the DB ").grid(column =1, row=0)

    tab2 = ttk.Frame(tabControl)
    tabControl.add(tab2, text='Orders')


    tab3 = ttk.Frame(tabControl)
    tabControl.add(tab3, text='Products')

    tab4 = ttk.Frame(tabControl)
    tabControl.add(tab4, text='Employee')

    #Results frame
    resultsFrame = Frame(root)
    resultsFrame.pack(side = TOP, fill = X)

    #Input frame
    inputFrame = Frame(root)
    inputFrame.pack(side = TOP, fill = X)

    #Status bar
    status = Label(root, text = "ready", bd = 1, relief = "sunken", anchor = W)
    status.pack(side = BOTTOM, fill = X)

    #Method to insert Start/End Date Entry Inputs
    def createDateInputs(frameWindow, row, column):
        dateInputFrame = Frame(frameWindow)
        Label(dateInputFrame, text="Start Date (yyyy-mm-dd)").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        startDateEnt = Entry(dateInputFrame)
        startDateEnt.grid(row="0", column="1")
        Label(dateInputFrame, text="End Date (yyyy-mm-dd)").grid(row="1", column="0", sticky=W, padx=5)
        endDateEnt = Entry(dateInputFrame)
        endDateEnt.grid(row="1", column="1")
        dateInputFrame.grid(row=row)

    #Method to take ID
    def createIdInputs(frameWindow, row, column):
        idInputFrame = Frame(frameWindow)
        Label(idInputFrame, text="ID").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        idEnt = Entry(idInputFrame)
        idEnt.grid(row="0", column="1")
        idInputFrame.grid(row=row)

    #Method to take country
    def createCountryInputs(frameWindow, row, column):
        countryInputFrame = Frame(frameWindow)
        Label(idInputFrame, text="Country").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        countryEnt = Entry(countryInputFrame)
        countryEnt.grid(row="0", column="1")
        countryInputFrame.grid(row=row)
    GUIlogin.LoginFrame(Frame)
    root.mainloop()
