# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""
import matplotlib.pyplot as plt
from exportToCSV import exportToCSV
from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query
import numpy as np

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
    
    if (len(queryResults) == 1):
        print ("There is no data available for the specified timeframe.")
        if (GUI):
            queryResults = [["There is no data available for the specified timeframe."]]
    else:
        # dates ratings product
        print ("Plotting the data...")
        ids2 = ids[:] # Copy ids into ids2
        # Below is a hacky solution to showing the bars on seperate x axis
        # positions, just take 0.35 off each to offset
        for i in range(0,len(ids2)):
            ids2[i] -= 0.35
        # Force x axis to show every ID, not go up in intervals > 1
        plt.xticks(np.arange(min(ids), max(ids)+1, 1.0))
        plt.bar(ids, amounts,width=0.3,color='g',align='center')
        plt.bar(ids2, totals,width=0.3,color='r',align='center')
        plt.legend(['Stock Available', 'Number of Sales'], loc='upper left')
        plt.xlabel('Product ID')
        plt.ylabel('Number of Stock')
        plt.title('Number of stock available for all products with the number of sales between %s and %s' % (startDate, endDate))
        plt.grid(True)
        plt.savefig("assets\\graph.png")        
        plt.show()
        
    # If GUI return the data
    if (GUI):
        return queryResults
    else:
        exportToCSV(queryResults)