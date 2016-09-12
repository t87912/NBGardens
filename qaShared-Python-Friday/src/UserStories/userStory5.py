# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""

from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory5(db, GUI, startDate, endDate):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        
        if (not GUI):
            startDate = input("Please enter the start date (YYYY-MM-DD): ")
            endDate = input("Please enter the end date (YYYY-MM-DD): ") 
            productID = input("Please enter the productID: ") 
        
        sqlParse = queries[5] % (startDate, endDate, productID)
        sql = sqlParse
        results = query(db, sql)
        
        # If GUI return the data
        if (GUI):
            return [results]