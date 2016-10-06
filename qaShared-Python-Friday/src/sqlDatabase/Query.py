# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:32:30 2016

@author: user
"""

def query(db, sql):
    """ query(sql): Query accepts an SQL statement and the SQL database
        connection as parameters and returns the results, which includes
        the header (column names) on the first line. Results are printed
        and returned in the format of a list of lists. """            
    # Getting the header:
    cursorHeader = db.cursor() # Creating the cursor to query the database
    try:
        cursorHeader.execute(sql)
        db.commit()
    except:
        db.rollback()
    header = []
    # Add column names to header
    for x in range(0, len(cursorHeader.description)):
        header.append(cursorHeader.description[x][0])
    cursorHeader.close()  
    
    # Getting the query result:
    cursorResults = db.cursor() # Creating the cursor to query the database
    try:
        cursorResults.execute(sql)
        db.commit()
    except:
        db.rollback()
        
    results = cursorResults.fetchall()
    queryResult = []
    print (header) # Print the header first
    # Printing the query results:
    for row in results:
        toPrint = []
        queryResult.append(row) # changed from [row] to row
        for i in range(0, len(row)):
            toPrint.append([row[i]])
        print (toPrint)
    # Putting the header at the start of the results
    queryResult.insert(0, header)
    return queryResult # was queryResults