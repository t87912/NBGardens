# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 16:49:43 2016

@author: Administrator
"""

# Test Adapter Class
import unittest
import pymysql
from UserStories import AllUserStories
from mongoDatabase.MongoDatabase import MongoDatabase

class UnitTestAdapter(unittest.TestCase):
    
    def setupEnvironment(self):
        # Setup allUserStories()
        self.run_query_obj = AllUserStories.AllUserStories()
        
        # Setup mySQL
        self.db = pymysql.connect("", "", "", "nbgardensds")
        
        # Setup MongoDB
        self.mongoDB = MongoDatabase() # Init Mongo db
        self.mongoDB.setDatabase(self.db) # Pass MySQL db into Mongo
        self.conn = self.mongoDB.getConnection()

    def test_date(self):
        valid = self.run_query_obj.validateDateInput("2000-01-01")
        self.assertEqual(True, valid)
            
    def test_userStory7(self):
        self.setupEnvironment()
        queryResults = self.run_query_obj.mongoStory1(self.db, self.conn, True, 1)
        correctResults = [['averageProductScore', 'averageDeliveryScore', 'averageServiceScore'],
                          [7.4, 8.75, 8.75]]
        self.assertEqual(queryResults, correctResults)

if __name__ == '__main__':
    unittest.main()