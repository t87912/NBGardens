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
        for r in range(1, len(queryResults)):
            products.append(queryResults[r][0])
            totals.append(queryResults[r][1])
        
        if (len(queryResults) == 1):
            print ("There is no data available for the specified timeframe.")
            if (GUI):
                queryResults = [["There is no data available for the specified timeframe."]]
        else:
            print ("Plotting the data...")
            #plt.plot(products, totals, "#993A54")
            #width = 0.35       # the width of the bars
            products2 = products[:] # Copy ids into ids2
            # Below is a hacky solution to showing the bars on seperate x axis
            # positions, just take 0.2 off each to offset
            # Bascially aligns prodID bar directly over prodID x tick
            for i in range(0,len(products2)):
                products2[i] -= 0.2
            plt.bar(products2, totals, width=0.4)
            plt.xticks(np.arange(min(products), max(products)+1, 1.0))
            plt.xlabel('Product ID')
            plt.ylabel('Amount of sales')
            plt.title('Amount of sales for all products between %s and %s' % (startDate, endDate))
            plt.grid(True)
            plt.savefig("assets\\graph.png")
            plt.show()
        
        # If GUI return the data
        if (GUI):
            return queryResults
        else:
            exportToCSV(queryResults)
    