# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 11:05:13 2016

@author: Administrator
"""

import getpass

class Login(object):
    """ Login: Gets user login details and returns them in a string """
    def __init__(self):
        self.printWelcome()
        self.username = self.getUsername()
        self.password = self.getPassword()      

    def printWelcome(self):
        """ printWelcome: Prints the welcome message """
        print ("Welcome to the NB Gardens Accounts and Sales Analytics System (ASAS)")
    
    def getUsername(self):
        """ getUsername: Get userinput for the username """
        username = input("Username: ")
        return username
        
    def getPassword(self):
        """ getPassword: Get userinput for the password, getpass module 
            should be used to print '*'s as the user types in password,
            this doesn't work in Spyder IDE though. """
        #password = input("Password: ")
        password = getpass.getpass('Password: ')
        print ("") # For formatting
        return password
        
    def getLoginDetails(self):
        """ getLoginDetails: Simply returns a list with user/password  """
        return [self.username, self.password]





