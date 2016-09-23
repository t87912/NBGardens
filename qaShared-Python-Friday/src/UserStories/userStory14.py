# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""

import matplotlib.pyplot as plt

from exportToCSV import exportToCSV
from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory14(db, GUI, startDate, endDate, employeeID):
    """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
    if (not GUI):
        startDate = input("Please enter the start date (YYYY-MM-DD): ")
        endDate = input("Please enter the end date (YYYY-MM-DD): ")  
        employeeID = input("Please enter the employee ID: ")  

    sqlParse = queries[14] % (startDate, endDate, employeeID)
    sql = sqlParse
    queryResults = query(db, sql)
    
    dates = []
    totals = []        
    for r in range(0, len(queryResults)):
        dates.append(queryResults[r][1])
        totals.append(queryResults[r][2])      
    
    if (len(queryResults) == 0):
        print ("There is no sales data available for this employee for the specified timeframe.")
        if (GUI):
            results = ["There is no sales data available for this employee for the specified timeframe."]
    else:
        # dates ratings product
        print ("Plotting the data...")
        plt.plot_date(dates, totals, "#993A54")
        plt.legend(loc=1)
        plt.xlabel('Date (YYYY-MM-DD)')
        plt.xticks(rotation=45)
        plt.ylabel('Number of Sales')
        plt.title('Amount of sales made by a particular salesperson over a period of time')
        plt.grid(True)
        #plt.savefig("C:\\Users\\Administrator\\Desktop\\qaShared-python-20160907T080629Z\\qaShared-python\\qaShared-python\\for git\\Image Files\\userStory14.png")
        plt.savefig("assets\\graph.png")
        plt.show()
        
    header = ("EmployeeID","OrderCreationDate","OrderTotal")
    results = []
    results.append(header)
    for x in range(0, len(queryResults)):
        results.append(queryResults[x])

    # If GUI return the data
    if (GUI):
        return results
    else:
        exportToCSV(results)