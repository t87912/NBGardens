# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:38:50 2016

@author: user
"""

from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory2(db, GUI, startDate, endDate):
    """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
    # If called in terminal program, get user to set input 
    if (not GUI):
        startDate = input("Please enter the start date (YYYY-MM-DD): ") 
        endDate = input("Please enter the end date (YYYY-MM-DD): ")
        
    sqlParse = queries[2] % (startDate, endDate)
    header = ("CustomerID","Firstname","LastName","SpendingTotal")
    results = []
    sql = sqlParse
    queryResults = query(db, sql) 
    results.append(header)
    for x in range(0, len(queryResults)):
        results.append(queryResults[x])
    if (GUI):  # If GUI return the data
        return results