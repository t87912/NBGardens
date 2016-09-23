# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""
import matplotlib.pyplot as plt
from exportToCSV import exportToCSV
from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory13(db, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (not GUI):
            startDate = input("Please enter the start date (YYYY-MM-DD): ")
            endDate = input("Please enter the end date (YYYY-MM-DD): ")    
    
        sqlParse = queries[13] % (startDate, endDate)
          
        sql = sqlParse
        queryResults = query(db, sql)
        
        products = []
        totals = []        
        for r in range(0, len(queryResults)):
            products.append(queryResults[r][0])
            totals.append(queryResults[r][1])
        
        print ("Plotting the data...")
        plt.plot(products, totals, "#993A54")
        plt.xlabel('Product ID')
        plt.ylabel('Amount of sales')
        plt.title('Amount of sales for a particular product over a period of time')
        plt.grid(True)
        plt.savefig("assets\\graph.png")
        plt.show()
        
        header = ("ProductID","NumberOfSales")
        results = []
        results.append(header)
        for x in range(0, len(queryResults)):
            results.append(queryResults[x])
        
        # If GUI return the data
        if (GUI):
            return results
        else:
            exportToCSV(results)
    