# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 09:31:15 2016

@author: Administrator
"""

def writeToTXT(listoflists):
    with open('assets/Files/data.txt', 'w') as f:
        for x in range(0, len(listoflists)):    
            f.write(repr(listoflists[x])+"\n")