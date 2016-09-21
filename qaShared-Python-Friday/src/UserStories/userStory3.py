# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""

from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory3(db, GUI, amount, startDate, endDate):
    """ useCase3: Accepts parameter 'period' which is a period, 1-4 """
    
    if (not GUI):
        amount = input("Please enter the amount: ")
        startDate = input("Please enter the start date (YYYY-MM-DD): ")
        endDate = input("Please enter the end date (YYYY-MM-DD): ")
          
    sqlParse = queries[3] % (startDate, endDate, amount)
    sql = sqlParse
    results = query(db, sql)
    
    # If GUI return the data
    if (GUI):
        return results