# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:48:47 2016

@author: Administrator
"""

from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query
import matplotlib.pyplot as plt
import os
import sys
import logging
import time

class AllUserStories (object):
    
    def __init__(self):
        empty = 0
        # some instructions

    def validateDateInput(self, date):
        """ validateDateInput: This method accepts a date as a parameter and
            will return true/false depending on whether the date is in the
            right format or not. Date should be in format YYYY-MM-DD. """
        try:
            # Try putting the date in the right format using strptime()
            date = time.strptime(date, "%Y-%m-%d")
            validDate = True
        except:
            print ("Error: Please input a date in the correct format.")
            validDate = False
        return validDate 
        
    def validateProductIDInput(self, productID):
        """ validateProductIDInput: This method accepts a product id (e.g. 
            prod id = 1) and validates it. True/false is returned. """
        try:
            int(productID)
            validID = True
        except:
            print ("Error: Please input a valid product ID.")
            validID = False
        return validID
        
    def validateAmountInput(self, amount):
        """ validateAmountInput: This method accepts an amount (e.g. 
            amount = 1 or 1.0) and validates it. True/false is returned. """
        try:
            float(amount)
            validAmount = True
        except:
            print ("Error: Please input a valid amount.")
            validAmount = False
        return validAmount
        
 
#    def userStory1(self, db, GUI, startDate, endDate):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
#        
#        # If called in terminal program, get user to set input:        
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ")    
#        
#        sqlParse = queries[1] % (startDate, endDate)
#              
#        sql = sqlParse
#        results = query(db, sql)
#        
#        # If GUI return the data
#        if (GUI):
#            return [results]
#  
#  
#    def userStory2(self, db, GUI, startDate, endDate):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
#        # If called in terminal program, get user to set input 
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ") 
#            endDate = input("Please enter the end date (YYYY-MM-DD): ")
#            
#        sqlParse = queries[2] % (startDate, endDate)
#                  
#        sql = sqlParse
#        results = query(db, sql) 
#        if (GUI):  # If GUI return the data
#            return [results]
    
    
#    def userStory3(self, db, GUI, amount, startDate, endDate):
#        """ useCase3: Accepts parameter 'period' which is a period, 1-4 """
#    
#        if (not GUI):
#            amount = input("Please enter the amount: ")
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ")
#              
#        sqlParse = queries[3] % (startDate, endDate, amount)
#        sql = sqlParse
#        results = query(db, sql)
#        
#        # If GUI return the data
#        if (GUI):
#            return [results]
  

#    def userStory4(self, db, GUI, startDate, endDate):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """  
#
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ")           
#        
#        sqlParse = queries[4] % (startDate, endDate)
#        sql = sqlParse
#        results = query(db, sql)
#            
#        # If GUI return the data
#        if (GUI):
#            return [results]
            
#
#    def userStory5(self, db, GUI, startDate, endDate, productID):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
#        
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ") 
#            productID = input("Please enter the productID: ") 
#        
#        sqlParse = queries[5] % (startDate, endDate, productID)
#        sql = sqlParse
#        results = query(db, sql)
#        
#        # If GUI return the data
#        if (GUI):
#            return [results]
 

#    def userStory6(self, db, GUI, startDate, endDate):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
#   
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ") 
#        
#        sqlParse = queries[6] % (startDate, endDate)
#        sql = sqlParse
#        
#        results = query(db, sql)
#        
#        # If GUI return the data
#        if (GUI):
#            return [results]
            
            
    def mongoStory1(self, MongoQueries, GUI, custID): # + GUI (bool) + startDate + endDate etc
        """ userStory7(Boolean for GUI, customer id): This method does xyz """
        if (not GUI):
            custID = int(input("What is the customer ID you want to view review scores for?: "))
        
        customerProductScores = MongoQueries.CustomerOrderReviews.getProductScoresfCust(custID)
        
        if len(customerProductScores) == 0:
            customerReviewScores = "N/A"        
        else:
            totalProductScores = 0
            
            for i in customerProductScores:
                totalProductScores += i
            
            avProductScore = totalProductScores / len(customerProductScores)
            customerDeliveryScores = MongoQueries.CustomerOrderReviews.getDeliveryScore(custID)
            totalDeliveryScores = 0
    
            for i in customerDeliveryScores:
                totalDeliveryScores += i
            
            avDeliveryScore = totalDeliveryScores / len(customerDeliveryScores)
            customerServiceScores = MongoQueries.CustomerOrderReviews.getServiceScore(custID)
            totalServiceScores = 0
    
            for i in customerServiceScores:
                totalServiceScores += i
    
            avServiceScore = totalServiceScores / len(customerServiceScores)
            customerReviewScores = [avProductScore, avDeliveryScore, avServiceScore]
        
        if (not GUI):
            #!!!! to get customer name need SQL QUERY !!!!#
            print(customerReviewScores)
            
        if (GUI):
            result = [customerReviewScores]
            return result # result = [[prodID, date date ], [], []]

     
    def mongoStory2(self, MongoQueries, GUI, gender):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        #if (not GUI):
          #  custID = int(input("What gender would you like to search for customer scores by? /n Select from M or F"))
        #if (GUI):
            #!!!!! need an SQL statement to create table of Male/Female Customers, same for age !!!!#
        print("TBC: need some SQL")
        
    
    
    def mongoStory3(self, MongoQueries, GUI):
        """ useCase9: """    
        print("TBC: need some SQL")
        
        
        
    def mongoStory4(self, MongoQueries, GUI, productID):
        """ useCase10 """
        print("TBC: need some SQL")
        if(not GUI):
            prodID = int(input("What is the product ID you want to view review scores for?: "))
        
        customerReviewScores = MongoQueries.CustomerOrderReviews.getProductScores(prodID)
        if len(customerReviewScores) == 0:
            avCustomerScore = "N/A"
            
        else:
            totalReviewScores = 0
            for i in customerReviewScores:
                totalReviewScores += i
            avCustomerScore = totalReviewScores / len(customerReviewScores)
            
        onlineReviewScores = MongoQueries.OnlineReviews.getOnlineReviewScores(prodID)
        if len(onlineReviewScores) == 0:
            avOnlineScore = "N/A"
        
        else:
            totalReviewScores = 0
            for i in onlineReviewScores:
                totalReviewScores += i
            avOnlineScore = totalReviewScores / len(onlineReviewScores)
        
        reviewScores = [avCustomerScore, avOnlineScore]
        
        if(not GUI):
            print("Customer Score    Online Score \n" + str(reviewScores[0]) + "               " + str(reviewScores[1]))
        
        if(GUI):
            result = [reviewScores]
            return result

   
    def mongoStory5(self, MongoQueries, GUI):
        """ useCase11 """
        #!!!!! very similar to 7 but with dates, needs SQL !!!!#
        print("TBC: need some SQL")    
    
    
    def mongoStory6(MongoQueries, GUI):
        """ useCase15 """
        #!!!! againn need SQL for date !!!!#
        print("TBC: need some SQL")
    
    
    def userStory12(self, db, GUI, productID):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        
        if (not GUI):
            validProductID = False
            while (not validProductID):    
                productID = input("Please enter the productID: ") 
                validProductID = self.validateProductIDInput(productID)
        
        sqlParse = queries[12] % (productID)
        sql = sqlParse
        results = query(db, sql)
        
        # If GUI return the data
        if (GUI):
            return [results]
            
            
#    def userStory13(self, db, GUI, startDate, endDate):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ")    
#    
#        sqlParse = queries[13] % (startDate, endDate)
#          
#        sql = sqlParse
#        results = query(db, sql)
#        
#        products = []
#        totals = []        
#        for r in range(0, len(results)):
#            products.append(results[r][0])
#            totals.append(results[r][1])
#        
#        print ("Plotting the data...")
#        plt.plot(products, totals, "#993A54")
#        plt.xlabel('Product ID')
#        plt.ylabel('Amount of sales')
#        plt.title('Amount of sales for a particular product over a period of time')
#        plt.grid(True)
#        #string = eval(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Image Files'))).replace('\\','\\\\')
#        #string = string.replace('\\','\\\\')
#        #print (string)
#        plt.savefig("graph.png")
#        #plt.savefig("\\Image Files\\userStory13.png")
#        plt.show()    
#        
#        # If GUI return the data
#        if (GUI):
#            return [results]
        
#    def userStory14(db, GUI, startDate, endDate, employeeID):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ")  
#            employeeID = input("Please enter the employee ID: ")  
#    
#        sqlParse = queries[14] % (startDate, endDate, employeeID)
#        sql = sqlParse
#        results = query(db, sql)
#        
#        dates = []
#        totals = []        
#        for r in range(0, len(results)):
#            dates.append(results[r][1])
#            totals.append(results[r][2])      
#        
#        if (len(results) == 0):
#            print ("There is no sales data available for this employee for the specified timeframe.")
#            if (GUI):
#                results = ["There is no sales data available for this employee for the specified timeframe."]
#        else:
#            # dates ratings product
#            print ("Plotting the data...")
#            plt.plot_date(dates, totals, "#993A54")
#            plt.legend(loc=1)
#            plt.xlabel('Date (YYYY-MM-DD)')
#            plt.xticks(rotation=45)
#            plt.ylabel('Number of Sales')
#            plt.title('Amount of sales made by a particular salesperson over a period of time')
#            plt.grid(True)
#            #plt.savefig("C:\\Users\\Administrator\\Desktop\\qaShared-python-20160907T080629Z\\qaShared-python\\qaShared-python\\for git\\Image Files\\userStory14.png")
#            plt.savefig("graph.png")
#            plt.show()
#
#        # If GUI return the data
#        if (GUI):
#            return [results]
        
        
#    def userStory16(self, db, GUI, startDate, endDate):
#        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
#        if (not GUI):
#            startDate = input("Please enter the start date (YYYY-MM-DD): ")
#            endDate = input("Please enter the end date (YYYY-MM-DD): ")    
#    
#        sqlParse = queries[16] % (startDate, endDate)
#          
#        sql = sqlParse
#        results = query(db, sql)
#        
#        ids = []
#        totals = [] 
#        amounts = []
#        for r in range(0, len(results)):
#            ids.append(results[r][0])
#            totals.append(results[r][1])
#            amounts.append(results[r][2])
#        
#        # dates ratings product
#        print ("Plotting the data...")
#        plt.plot(ids, totals, amounts, "#993A54")
#        plt.legend(loc=1)
#        plt.xlabel('Date (YYYY-MM-DD)')
#        plt.xticks(rotation=45)
#        plt.ylabel('Number of Sales')
#        plt.title('Amount of sales made by a particular salesperson over a period of time')
#        plt.grid(True)
#        #plt.savefig("C:\\Users\\Administrator\\Desktop\\qaShared-python-20160907T080629Z\\qaShared-python\\qaShared-python\\for git\\Image Files\\userStory16.png")
#        plt.savefig("graph.png")        
#        plt.show()        
#        
#        # If GUI return the data
#        if (GUI):
#            return [results]


#    def userStory17(self, GUI, query):
#        """ customeQuery: Executes user custom query. Need validation here. """
#        if (not GUI):
#            query = input("Input SQL query: ")
#        
#        self.logger = logging.info('Custom SQL query: %s', query)
#        cursor = self.db.cursor() # Creating the cursor to query the database
#        # Executing the query:
#        try:
#            cursor.execute(query)
#            self.db.commit()
#        except:
#            self.db.rollback()
#
#        results = cursor.fetchall()
#        for row in results:
#            toPrint = []
#            for i in range(0, len(row)):
#                toPrint.append([row[i]])
#            print (toPrint)
#        
#        if (GUI):
#            return results
    
    
#    def userStory18(self):
#         print ("Returning to main menu...")
#  
#  
#    def userStory19(self):
#         print ("Exiting the program...")
#         sys.exit(0)
         
         
    def userStorySeries1(self, db, GUI, startDate, endDate, query_number):
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (not GUI):
            validStartDate = False
            validEndDate = False
            while (not validStartDate):    
                startDate = input("Please enter the start date (YYYY-MM-DD): ")
                validStartDate = self.validateDateInput(startDate)
            while (not validEndDate):
                endDate = input("Please enter the end date (YYYY-MM-DD): ") 
                validEndDate = self.validateDateInput(endDate)
        
            sqlParse = queries[query_number] % (startDate, endDate)
            sql = sqlParse
            
            results = query(db, sql)
            
            if (query_number == 13):
                products = []
                totals = []        
                for r in range(0, len(results)):
                    products.append(results[r][0])
                    totals.append(results[r][1])
                
                print ("Plotting the data...")
                plt.plot(products, totals, "#993A54")
                plt.xlabel('Product ID')
                plt.ylabel('Amount of sales')
                plt.title('Amount of sales for a particular product over a period of time')
                plt.grid(True)
                #string = eval(os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'Image Files'))).replace('\\','\\\\')
                #string = string.replace('\\','\\\\')
                #print (string)
                plt.savefig("graph.png")
                #plt.savefig("\\Image Files\\userStory13.png")
                plt.show()
            
            elif (query_number == 16):
                ids = []
                totals = [] 
                amounts = []
                for r in range(0, len(results)):
                    ids.append(results[r][0])
                    totals.append(results[r][1])
                    amounts.append(results[r][2])
                
                # dates ratings product
                print ("Plotting the data...")
                plt.plot(ids, totals, amounts, "#993A54")
                plt.legend(loc=1)
                plt.xlabel('Date (YYYY-MM-DD)')
                plt.xticks(rotation=45)
                plt.ylabel('Number of Sales')
                plt.title('Amount of sales made by a particular salesperson over a period of time')
                plt.grid(True)
                #plt.savefig("C:\\Users\\Administrator\\Desktop\\qaShared-python-20160907T080629Z\\qaShared-python\\qaShared-python\\for git\\Image Files\\userStory16.png")
                plt.savefig("graph.png")        
                plt.show()
            
        # If GUI return the data
        if (GUI):
            return [results]
    
    def userStorySeries2(self, db, GUI, startDate, endDate, additional_attribute, query_number):
        """ useCase3: Accepts parameter 'period' which is a period, 1-4 """
    
        if (not GUI):
            validStartDate = False
            validEndDate = False
            while (not validStartDate):    
                startDate = input("Please enter the start date (YYYY-MM-DD): ")
                validStartDate = self.validateDateInput(startDate)
            while (not validEndDate):
                endDate = input("Please enter the end date (YYYY-MM-DD): ") 
                validEndDate = self.validateDateInput(endDate)
            if (query_number == 3):
                validAmount = False
                while (not validAmount):
                    amount_or_productid = input("Please enter the amount: ")
                    validAmount = self.validateAmountInput(amount_or_productid)
            else:
                validProductID = False
                while (not validProductID):
                    if (query_number == 14):
                        amount_or_productid = input("Please enter the employeeID: ")
                    else:
                        amount_or_productid = input("Please enter the productID: ")                        
                    validProductID = self.validateProductIDInput(amount_or_productid)
                    
        sqlParse = queries[query_number] % (startDate, endDate, amount_or_productid)
        sql = sqlParse
        results = query(db, sql)
        
        if (query_number == 14):
            
            dates = []
            totals = []        
            for r in range(0, len(results)):
                dates.append(results[r][1])
                totals.append(results[r][2])      
            
            if (len(results) == 0):
                print ("There is no sales data available for this employee for the specified timeframe.")
                if (GUI):
                    results = ["There is no sales data available for this employee for the specified timeframe."]
            else:
                # dates ratings product
                print ("Plotting the data...")
                plt.plot_date(dates, totals, "#993A54")
                plt.legend(loc=1)
                plt.xlabel('Date (YYYY-MM-DD)')
                plt.xticks(rotation=45)
                plt.ylabel('Number of Sales')
                plt.title('Amount of sales made by a particular salesperson over a period of time')
                plt.grid(True)
                #plt.savefig("C:\\Users\\Administrator\\Desktop\\qaShared-python-20160907T080629Z\\qaShared-python\\qaShared-python\\for git\\Image Files\\userStory14.png")
                plt.savefig("graph.png")
                plt.show()
                
        # If GUI return the data
        if (GUI):
            return [results]       