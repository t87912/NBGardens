# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:32:30 2016

@author: user
"""

def query(db, sql):
        """ query(sql): Query accepts an SQL statement as a parameter and 
            returns the results. """
        cursor = db.cursor() # Creating the cursor to query the database
        
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
            
        results = cursor.fetchall()
        queryResult = []
        for row in results:
            toPrint = []
            queryResult.append([row])
            for i in range(0, len(row)):
                toPrint.append([row[i]])
            print (toPrint)
        return results # was queryResults