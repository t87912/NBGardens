# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 15:03:21 2016

@author: Ameen
"""

import json
import numpy as np

class TheWriterClass:
    
    #def __init__(self):
        
        #self.data = np.empty((10, 1)).tolist()
        #print (self.data)
    
    
    def writeToFile(self, data): 
        with open('assets/data.json', 'w') as outfile:
            json.dump(data, outfile, sort_keys=True, indent=4)

#writer_obj = TheWriterClass()
#writer_obj.writeToFile()
