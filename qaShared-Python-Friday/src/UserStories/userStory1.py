# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""

from exportToCSV import exportToCSV
from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory1(db, GUI, startDate, endDate):
    """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
    
    print ("USERSTORY1")    
    
    # If called in terminal program, get user to set input:        
    if (not GUI):
        startDate = input("Please enter the start date (YYYY-MM-DD): ")
        endDate = input("Please enter the end date (YYYY-MM-DD): ")    
    
    sqlParse = queries[1] % (startDate, endDate)
    results = []
    sql = sqlParse
    header = ("EmployeeID","Firstname","LastName","SalesTotal")
    queryResults = query(db, sql)
    results.append(header)
    for x in range(0, len(queryResults)):
        results.append(queryResults[x])
    # If GUI return the data
    if (GUI):
        return results
    else:
        exportToCSV(results)