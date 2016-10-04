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
    for r in range(1, len(queryResults)):
        dates.append(queryResults[r][1])
        totals.append(queryResults[r][2])      
    
    if (len(queryResults) == 1):
        print ("There is no data available for the specified timeframe.")
        if (GUI):
            queryResults = [["There is no data available for the specified timeframe."]]
    else:
        # dates ratings product
        print ("Plotting the data...")
        plt.plot_date(dates, totals, "#993A54")
        plt.legend(loc=1)
        plt.xlabel('Date (MMM-YYYY)')
        plt.xticks(rotation=45)
        plt.ylabel('Value of Sales (£)')
        plt.title('Amount of sales made by salespersonID %s between %s and %s' % (employeeID, startDate, endDate))
        plt.grid(True)
        plt.savefig("assets\\graph.png")
        plt.show()
        
    # If GUI return the data
    if (GUI):
        return queryResults
    else:
        exportToCSV(queryResults)