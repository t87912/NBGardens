# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:03:21 2016

@author: Ameen
"""

import json

class TheWriterClass:
    """ TheWriterClass: This class has one method which takes data as a
        parameter, in the form of a list of lists, and outputs a json file
        in /assets/Files. """
    def writeToFile(self, data): 
        with open('assets/Files/data.json', 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4)
