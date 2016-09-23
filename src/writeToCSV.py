# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 22:23:41 2016

@author: user
"""

# Write to csv function

def writeToCSV(rows, headers = ""):
    """ writeToCSV: This function accepts data as a parameter. This data is in
        the following format: [[row 1], [row 2]...[row n]].

        Author: Damien Lloyd"""

    path = os.getcwd() + '/'
    filename = path + filename
    print ("Writing CSV to " + filename)

    with open(filename, 'w', newline='') as f:
        a_csv = csv.writer(f)

        if headers != "":
            a_csv.writerow(headers)

        a_csv.writerows(rows)
