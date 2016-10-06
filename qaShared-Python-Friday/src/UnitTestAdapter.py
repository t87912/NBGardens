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
    """ UnitTestAdapter: This class is used for testing the NBGardens ASAS
        system. Methods test various userStories and validation methods
        within allUserStories. assertEqual is used to assert that the returned
        data (for a user story) or boolean (for validation) is correct. """
        
    def setupEnvironment(self):
        """ setupEnvironment: This method sets up the environment to allow
            the unit tests on userStories to work with the correct database
            connections to mongoDB/mySQL. """
        # Setup allUserStories()
        self.run_query_obj = AllUserStories.AllUserStories()
        # Setup mySQL
        self.db = pymysql.connect("", "", "", "nbgardensds")
        # Setup MongoDB
        self.mongoDB = MongoDatabase() # Init Mongo db
        self.mongoDB.setDatabase(self.db) # Pass MySQL db into Mongo
        self.conn = self.mongoDB.getConnection()

    def test_date_valid(self):
        """ test_date_valid: This method tests that a date is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateDateInput("2000-01-01")
        self.assertEqual(True, valid)
        
    def test_date_invalid(self):
        """ test_date_invalid: This method tests that a date is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateDateInput("1st May 2011")
        self.assertEqual(False, valid)
        
    def test_productID_valid(self):
        """ test_productID_valid: This method tests that a productID is 
            validated correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateProductIDInput(1)
        self.assertEqual(True, valid)
        
    def test_productID_invalid(self):
        """ test_productID_invalid: This method tests that a productID is 
            validated correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateProductIDInput("one")
        self.assertEqual(False, valid)
        
    def test_age_valid(self):
        """ test_age_valid: This method tests that an age is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateAgeInput(18)
        self.assertEqual(True, valid)
        
    def test_age_invalid(self):
        """ test_age_invalid: This method tests that an age is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateAgeInput("eighteen")
        self.assertEqual(False, valid)
        
    def test_amount_valid(self):
        """ test_amount_valid: This method tests that an amount is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateAmountInput(50)
        self.assertEqual(True, valid)
        
    def test_amount_invalid(self):
        """ test_amount_invalid: This method tests that an amount is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateAmountInput("fifty")
        self.assertEqual(False, valid)
        
    def test_county_valid(self):
        """ test_county_valid: This method tests that a county is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateCountyInput("London")
        self.assertEqual(True, valid)
        
    def test_county_invalid(self):
        """ test_county_invalid: This method tests that a county is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateCountyInput("United Kingdom")
        self.assertEqual(False, valid)
        
    def test_gender_valid(self):
        """ test_gender_valid: This method tests that a gender is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateGenderInput("Male")
        self.assertEqual(True, valid)
        
    def test_gender_invalid(self):
        """ test_gender_invalid: This method tests that a gender is validated 
            correctly. """
        self.run_query_obj = AllUserStories.AllUserStories()
        valid = self.run_query_obj.validateGenderInput("Apache Attack Helicopter")
        self.assertEqual(False, valid)
        
    def test_userStor7(self):
        """ test_userStory7: This method validates asserts that the data
            returned for userStory3 is correct. """
        self.setupEnvironment()
        queryResults = self.run_query_obj.mongoStory1(self.db, self.conn, True, 1)
        correctResults = [7.4, 8.75, 8.75]
        self.assertEqual(queryResults[1], correctResults)
            
    def test_userStory8(self):
        """ test_userStory8: This method validates asserts that the data
            returned for userStory7 is correct. """
        self.setupEnvironment()
        queryResults = self.run_query_obj.mongoStory1(self.db, self.conn, True, 1)
        correctResults = [['averageProductScore', 'averageDeliveryScore', 'averageServiceScore'],
                          [7.4, 8.75, 8.75]]
        self.assertEqual(queryResults, correctResults)

if __name__ == '__main__':
    unittest.main()