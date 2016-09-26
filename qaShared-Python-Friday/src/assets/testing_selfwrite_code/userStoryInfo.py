# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 20:01:20 2016

@author: user
"""

# user stories stuff


# userInput validation: [date from, date to, empID/prodID, amount]
# FORMAT:     [TITLE, SQL QUERY]

userStories = [
                ["3. Print all the products in the SQL database", "SELECT * FROM Product", [0,0,0,0]],
                ["4. Print stock for particular product ID","SELECT amount FROM Product Where idProduct = '%s'", [0,0,1,0]],
                ["5. Test","test", [0,0,0,0]]
                ]