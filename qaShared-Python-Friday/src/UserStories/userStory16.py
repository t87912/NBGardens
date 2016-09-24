# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""
import matplotlib.pyplot as plt
from exportToCSV import exportToCSV
from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory16(db, GUI, startDate, endDate):
    """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
    if (not GUI):
        startDate = input("Please enter the start date (YYYY-MM-DD): ")
        endDate = input("Please enter the end date (YYYY-MM-DD): ")    

    sqlParse = queries[16] % (startDate, endDate)
      
    sql = sqlParse
    queryResults = query(db, sql)
    
    ids = []
    totals = [] 
    amounts = []
    
    for r in range(1, len(queryResults)):
        ids.append(queryResults[r][0])
        totals.append(queryResults[r][1])
        amounts.append(queryResults[r][2])
    
    print (len(ids))    
    print (len(totals))
    print (len(amounts))    
    
    # dates ratings product
    print ("Plotting the data...")
    width = 0.35       # the width of the bars
    plt.bar(ids, totals, width, color='r')
    plt.bar(ids, amounts, width, color='b')
    #plt.plot(ids, totals)
    #plt.plot(ids, amounts)
    plt.legend(['Number of Sales', 'Stock Available'], loc='upper left')
    plt.xlabel('Product ID')
    plt.ylabel('Number of Sales')
    plt.title('Amount of sales made by a particular salesperson over a period of time')
    plt.grid(True)
    plt.savefig("assets\\graph.png")        
    plt.show()
        
    # If GUI return the data
    if (GUI):
        return queryResults
    else:
        exportToCSV(queryResults)