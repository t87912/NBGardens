# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:18:51 2016

@author: Administrator
"""

import csv
import sys

def exportToCSV(data):
    """ exportToCSV: Writes the contents of the query output results box
        to a CSV file in /Assets called CSV_Output.csv. This method can
        write data with any number of rows and columns, assuming the data
        format is a list of lists, e.g. [[1,2],[3,4],[5,6]] """
    with open("assets/Files/data.csv", "w") as csvFile:
        # Remove empty line in between every row when writing to CSV
        writer = csv.writer(csvFile, sys.stdout, lineterminator='\n')
        for row in range(0, len(data)):
            writer.writerow(data[row])
