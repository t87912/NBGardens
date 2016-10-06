# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:23:41 2016

@author: user
"""

# Write to csv function

def writeToCSV(data):
    """ writeToCSV: This function accepts data as a parameter. This data is in
        the following format: [[row 1], [row 2]...[row n]].  """
        
    # BELOW IS MY CODE FROM THE ORIGINAL PROGRAM
    # IT NEEDS TO BE EXTENDED TO ALLOW ANY DATA SET TO BE WRITTEN TO A CSV FILE
    # Convert datetimes to date strings
    dates = []
    ratings = []
    for x in range(0, len(dates)):
        dates[x] = dates[x].strftime('%d-%m-%Y')
        
    for y in range(0, len(ratings)):
        ratings[y] = str(ratings[y])
    
    forCSV = []
    for i in range(0,len(ratings)):
        forCSV.append([dates[i],ratings[i]])
    
    print ("Writing dates and ratings to CSV file: /CSV Files/ratingsOverTime.csv...")
    with open("C:\\Users\\Administrator\\Desktop\\Week 5 - Python\\py files\\CSV Files\\ratingsOverTimeSQL.csv", "w") as f:
        # Last 2 parameters below to remove empty line between each line            
        writer = csv.writer(f, sys.stdout, lineterminator='\n')
        for z in range(0, len(forCSV)):
            writer.writerow(forCSV[z])