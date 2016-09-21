# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""

from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query

def userStory12(db, GUI, productID):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        
        if (not GUI):
            productID = input("Please enter the productID: ") 
        
        sqlParse = queries[12] % (productID)
        sql = sqlParse
        results = query(db, sql)
        
        # If GUI return the data
        if (GUI):
            return results