# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""
import matplotlib.pyplot as plt

from SQLQueries import queries
from Query import query
import os

def userStory13(db, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (not GUI):
            startDate = input("Please enter the start date (YYYY-MM-DD): ")
            endDate = input("Please enter the end date (YYYY-MM-DD): ")    
    
        sqlParse = queries[13] % (startDate, endDate)
          
        sql = sqlParse
        results = query(db, sql)
        
        products = []
        totals = []        
        for r in range(0, len(results)):
            products.append(results[r][0])
            totals.append(results[r][1])
        
        print ("Plotting the data...")
        plt.plot(products, totals, "#993A54")
        plt.xlabel('Product ID')
        plt.ylabel('Amount of sales')
        plt.title('Amount of sales for a particular product over a period of time')
        plt.grid(True)
        #string = eval(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Image Files'))).replace('\\','\\\\')
        #string = string.replace('\\','\\\\')
        #print (string)
        plt.savefig("graph.png")
        #plt.savefig("\\Image Files\\userStory13.png")
        plt.show()    
        
        # If GUI return the data
        if (GUI):
            return [results]