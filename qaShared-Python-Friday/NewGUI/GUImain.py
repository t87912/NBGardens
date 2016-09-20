from tkinter import *
from tkinter import ttk



class MainFrame(ttk.Frame):

    queryID = -1
    dates = ['o','o']
    endDateEnt = 0
    startDateEnt = 0
    true = 0
    def __init__(self, master, *args, **kwargs):
        self.test = 1
        self.master = master
        #Setting up main window


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

        editSub = Menu(menu)
        menu.add_cascade(label = "Edit", menu = editSub)
        editSub.add_command(label = "Copy")
        editSub.add_command(label = "Paste")
        editSub.add_command(label = "Select All")

        viewSub = Menu(menu)
        menu.add_cascade(label = "View", menu = viewSub)
        viewSub.add_command(label = "Toggle full screen")

        #Tabs
        tabControl = ttk.Notebook(inputFrame)

        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text = 'Customer')
        tabControl.pack(expand=1, fill="both")
        comboValues = ['Highest spending customer', 'Highest spending customers (limit by min amount)', 'Customers Average rating', 'Average rating by county', 'Average rating by demographic', 'Customer satisfaction by business area', 'Customer satisfaction over areas']
        self.createQueryComboBoxOrders(tab1, 0, 0, comboValues)

        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Orders')
        comboValues = ['Total spend versus total cost', 'Average amount of time taken to fulfil and order']
        self.createQueryComboBoxOrders(tab2, 0, 0, comboValues)

        tab3 = ttk.Frame(tabControl)
        tabControl.add(tab3, text='Products')
        comboValues = ['Total return on investment', 'Average product website rating vs Average product order rating', 'Check if website and physical inventroy details match', 'Amount of Sales', 'Stock available against number of sales for product']
        self.createQueryComboBoxOrders(tab3, 0, 0, comboValues)

        tab4 = ttk.Frame(tabControl)
        tabControl.add(tab4, text='Employee')
        comboValues = ['Top Sales Person', 'Sales by Sales Person']
        self.createQueryComboBoxOrders(tab4, 0, 0, comboValues)

        #Status bar
        status = Label(root, text = "ready", bd = 1, relief = "sunken", anchor = W)
        status.pack(side = BOTTOM, fill = X)

    def getDates(self,a,b):
        start=a.get()
        end=b.get()
        self.dates = [start,end]

    def getQueryID(self,tab,CV):
        queryID = CV[0]
        print(queryID)
        if(queryID=='Top Sales Person'):
            self.dates = self.createDateInputs(tab,5,0)
            ok = Button(tab,text = "Perform Query", command =lambda:self.topSales(tab))
            ok.grid(row="1", column="2")


#Method to insert Start/End Date Entry Inputs
    def createDateInputs(self,tab, row, column):
        dateInputFrame = Frame(tab)
        Label(dateInputFrame, text="Start Date (yyyy-mm-dd)").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        self.startDateEnt = Entry(dateInputFrame)
        self.startDateEnt.grid(row="0", column="1")
        Label(dateInputFrame, text="End Date (yyyy-mm-dd)").grid(row="1", column="0", sticky=W, padx=5)
        self.endDateEnt = Entry(dateInputFrame)
        self.endDateEnt.grid(row="1", column="1")
        dateInputFrame.grid(row=row)


    #Method to take ID
    def createIdInputs(self,frameWindow, row, column):
        idInputFrame = Frame(frameWindow)
        Label(idInputFrame, text="ID").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        idEnt = Entry(idInputFrame)
        idEnt.grid(row="0", column="1")
        idInputFrame.grid(row=row)

    #Method to take country
    def createCountryInputs(self,frameWindow, row, column):
        countryInputFrame = Frame(frameWindow)
        Label(idInputFrame, text="Country").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        countryEnt = Entry(countryInputFrame)
        countryEnt.grid(row="0", column="1")
        countryInputFrame.grid(row=row)

    #Dropdown box for Queries
    def createQueryComboBoxOrders(self,tab, row, column, comboValues):
        queryComboBoxFrame = Frame(tab)
        Label(queryComboBoxFrame, text="Choose a query:").grid(row="0", column="0", sticky=W, padx=5, pady=5)
        combobox = ttk.Combobox(queryComboBoxFrame, values = comboValues, width="50")
        combobox.current(0)
        combobox.config(state = 'readonly')
        combobox.grid(row = "0", column = "1")
        B = Button(queryComboBoxFrame,text = "Select Query", command =lambda: self.getQueryID(tab,comboValues))
        B.grid(row=1)
        queryComboBoxFrame.grid(row=row, column=column)
        queryComboBoxFrame.grid_columnconfigure(0, weight=1)

    #Method to work out the top sales
    def topSales(self,tab):
        self.getDates(self.startDateEnt,self.endDateEnt)
        datefrom = self.dates[0]
        dateto = self.dates[1]
        #MainApplication.userStory1(dateFrom,dateTo)
        print(datefrom,dateto)

root = Tk()
MainFrame = MainFrame(root)
root.title("NB Gardens")
root.geometry("600x600")
root.mainloop()
