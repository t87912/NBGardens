# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:48:47 2016

@author: Administrator
"""

from mongoDatabase.MongoQueries import CustomerOrderReviews


from exportToCSV import exportToCSV
from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query
import matplotlib.pyplot as plt
import time
import numpy as np

class AllUserStories (object):

    def __init__(self):
        empty = 0
        empty += 1
        # some instructions
        
    def newUserStory(self, db, GUI, autoGen, query_number):
        #print ("Query number: %s" % (query_number))
        userStories = autoGen[3]
        # [["%s. Print a list of all products", "SELECT * FROM Product", [0,0,0]]]
        #print (userStories)
        
        sqlQuery = userStories[query_number][1]
        queryInputs = userStories[query_number][2]
        needInputs = False
        
        for y in range(0, len(userStories[query_number][2])):
            if (userStories[query_number][2][y] == 1):
                needInputs = True
        
        if (needInputs):
            validStartDate = False
            validEndDate = False
            validProductID = False
            validAmount = False
            inputs = []
            for x in range(0, len(queryInputs)):
                if (queryInputs[x] == 1 and x == 0):
                    while (not validStartDate):
                            startDate = input("Please enter the start date (YYYY-MM-DD): ")
                            validStartDate = self.validateDateInput(startDate)
                            inputs.append(startDate)
                elif (queryInputs[x] == 1 and x == 1):
                    while (not validEndDate):
                            endDate = input("Please enter the end date (YYYY-MM-DD): ")
                            validEndDate = self.validateDateInput(endDate)
                            inputs.append(endDate)
                elif (queryInputs[x] == 1 and x == 2):
                    while (not validProductID):
                            productID = input("Please enter the productID: ")
                            validProductID = self.validateProductIDInput(productID)
                            inputs.append(productID)
                elif (queryInputs[x] == 1 and x == 3):
                    while (not validAmount):
                            amount = input("Please enter the productID: ")
                            validAmount = self.validateAmountInput(amount)
                            inputs.append(amount)

            #inputsString = ""            
            #for i in range(0, len(inputs)):
             #   if (len(inputs) == i+1):
              #      inputsString += inputs
               # elif (i == len(inputs)-1):
                #    inputsString += inputs
                #elif (i+1 == len(inputs)):
                    
                
            #strToEval = "sqlParse = sqlQuery % (" + inputsString + ")"
            sqlParse = sqlQuery % (startDate, endDate)

            query(db, sqlParse)
        else:
            query(db, sqlQuery)
        

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

    #def mongoStory1(self, MongoQueries, GUI, custIDi): # + GUI (bool) + startDate + endDate etc
    def mongoStory1(self, sqlConn, conn, GUI, custID): # mongo 7
        """ userStory7(Boolean for GUI, customer id): This method does xyz """
        if (not GUI):
            custID = int(input("What is the customer ID you want to view review scores for?: "))
        customerProductScores = CustomerOrderReviews(conn).getProductScoresfCust(custID)
        
        if len(customerProductScores) == 0:
            customerReviewScores = "N/A"
            print ("warning n/a")
        else:
            totalProductScores = 0
            for i in customerProductScores:
                totalProductScores += i
            avProductScore = totalProductScores / len(customerProductScores)
    
            customerDeliveryScores = CustomerOrderReviews(conn).getDeliveryScore(custID)
            totalDeliveryScores = 0
            for i in customerDeliveryScores:
                totalDeliveryScores += i
            avDeliveryScore = totalDeliveryScores / len(customerDeliveryScores)
    
            customerServiceScores = CustomerOrderReviews(conn).getServiceScore(custID)
            totalServiceScores = 0
            for i in customerServiceScores:
                totalServiceScores += i
            avServiceScore = totalServiceScores / len(customerServiceScores)
    
            customerReviewScores = [["averageProductScore","averageDeliveryScore", "averageServiceScore"],
                                    [avProductScore, avDeliveryScore, avServiceScore]]
    
        if (not GUI):
            #print (customerReviewScores)
            for u in range(0, len(customerReviewScores)):
                print (customerReviewScores[u])
    
        if (GUI):
            result = customerReviewScores
            return result
#        if (not GUI):
#            custID = int(input("What is the customer ID you want to view review scores for?: "))
#
#        customerProductScores = MongoQueries.CustomerOrderReviews.getProductScoresfCust(custID)
#
#        if len(customerProductScores) == 0:
#            customerReviewScores = "N/A"
#        else:
#            totalProductScores = 0
#
#            for i in customerProductScores:
#                totalProductScores += i
#
#            avProductScore = totalProductScores / len(customerProductScores)
#            customerDeliveryScores = MongoQueries.CustomerOrderReviews.getDeliveryScore(custID)
#            totalDeliveryScores = 0
#
#            for i in customerDeliveryScores:
#                totalDeliveryScores += i
#
#            avDeliveryScore = totalDeliveryScores / len(customerDeliveryScores)
#            customerServiceScores = MongoQueries.CustomerOrderReviews.getServiceScore(custID)
#            totalServiceScores = 0
#
#            for i in customerServiceScores:
#                totalServiceScores += i
#
#            avServiceScore = totalServiceScores / len(customerServiceScores)
#            customerReviewScores = [avProductScore, avDeliveryScore, avServiceScore]
#
#        if (not GUI):
#            #!!!! to get customer name need SQL QUERY !!!!#
#            print(customerReviewScores)
#
#        if (GUI):
#            result = [customerReviewScores]
#            return result # result = [[prodID, date date ], [], []]


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
        else:
            exportToCSV(results)


    def userStorySeries1(self, db, GUI, startDate, endDate, query_number):
        """ useCase 1, 2, 4, 6, 13, 16: Accepts parameter 'period' which is a period, 1-4 """
        """
        Called to run a query and retrieve appropriate user input as part of the query string.
        additional ifs are used for case 13 and 16 for graphing

        @attention: method encapsulates use cases: 1, 2, 4, 6, 13, 16. original methods are deprecated.

        @param db: mysql db connection passed
        @param GUI: informs of GUI use
        @param startDate: date in string form ("00-00-0000") as a date to start query serach from
        @param endDate: date in string form ("00-00-0000") as a date to end query serach from
        @param query_number: chosen query option - acts as identifier. used to initate use case 14
        @return results: invoked if gui is TRUE, therby params are passed into the method through gui input
        """
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
#            products = []
#            totals = []
#            for r in range(1, len(results)):
#                products.append(results[r][0])
#                totals.append(results[r][1])
#
#            print ("Plotting the data...")
#            plt.plot(products, totals, "#993A54")
#            plt.xlabel('Product ID')
#            plt.ylabel('Amount of sales')
#            plt.title('Amount of sales for a particular product over a period of time')
#            plt.grid(True)
#            plt.savefig("graph.png")
#            plt.show()
        
            products = []
            totals = []
            for r in range(1, len(results)):
                products.append(results[r][0])
                totals.append(results[r][1])
        
            if (len(results) == 1):
                print ("There is no data available for the specified timeframe.")
                if (GUI):
                    results = [["There is no data available for the specified timeframe."]]
            else:
                print ("Plotting the data...")
                #plt.plot(products, totals, "#993A54")
                #width = 0.35       # the width of the bars
                products2 = products[:] # Copy ids into ids2
                # Below is a hacky solution to showing the bars on seperate x axis
                # positions, just take 0.2 off each to offset
                # Bascially aligns prodID bar directly over prodID x tick
                for i in range(0,len(products2)):
                    products2[i] -= 0.2
                plt.bar(products2, totals, width=0.4)
                plt.xticks(np.arange(min(products), max(products)+1, 1.0))
                plt.xlabel('Product ID')
                plt.ylabel('Amount of sales')
                plt.title('Amount of sales for all products between %s and %s' % (startDate, endDate))
                plt.grid(True)
                plt.savefig("assets\\graph.png")
                plt.show()

        elif (query_number == 16):
#            ids = []
#            totals = []
#            amounts = []
#            for r in range(1, len(results)):
#                ids.append(results[r][0])
#                totals.append(results[r][1])
#                amounts.append(results[r][2])
#
#            # dates ratings product
#            print ("Plotting the data...")
#            plt.plot(ids, totals, amounts, "#993A54")
#            plt.legend(loc=1)
#            plt.xlabel('Date (YYYY-MM-DD)')
#            plt.xticks(rotation=45)
#            plt.ylabel('Number of Sales')
#            plt.title('Amount of sales made by a particular salesperson over a period of time')
#            plt.grid(True)
#            plt.savefig("graph.png")
#            plt.show()
        
            ids = []
            totals = [] 
            amounts = []
            
            for r in range(1, len(results)):
                ids.append(results[r][0])
                totals.append(results[r][1])
                amounts.append(results[r][2]) 
            
            if (len(results) == 1):
                print ("There is no data available for the specified timeframe.")
                if (GUI):
                    results = [["There is no data available for the specified timeframe."]]
            else:
                # dates ratings product
                print ("Plotting the data...")
                ids2 = ids[:] # Copy ids into ids2
                # Below is a hacky solution to showing the bars on seperate x axis
                # positions, just take 0.35 off each to offset
                for i in range(0,len(ids2)):
                    ids2[i] -= 0.35
                # Force x axis to show every ID, not go up in intervals > 1
                plt.xticks(np.arange(min(ids), max(ids)+1, 1.0))
                plt.bar(ids, amounts,width=0.3,color='g',align='center')
                plt.bar(ids2, totals,width=0.3,color='r',align='center')
                plt.legend(['Stock Available', 'Number of Sales'], loc='upper left')
                plt.xlabel('Product ID')
                plt.ylabel('Number of Stock')
                plt.title('Number of stock available for all products with the number of sales between %s and %s' % (startDate, endDate))
                plt.grid(True)
                plt.savefig("assets\\graph.png")        
                plt.show()

        # If GUI return the data
        if (GUI):
            return [results]
        else:
            exportToCSV(results)


    def userStorySeries2(self, db, GUI, startDate, endDate, additional_attribute, query_number):
        """ useCase 3, 5, 14: Accepts parameter 'period' which is a period, 1-4 """
        """
        Called to run a method and retrieve appropriate user input if gui is false
        use case 14 is executed depending on query_number -> draw graphs etc

        @attention: method encapsulates use cases: 3, 5, 14. original methods are deprecated.

        @param db: mysql db connection passed
        @param GUI: informs of GUI use
        @param startDate: date in string form ("00-00-0000") as a date to start query serach from
        @param endDate: date in string form ("00-00-0000") as a date to end query serach from
        @param additional_attribute: empty passed param
        @param query_number: chosen query option - acts as identifier. used to initate use case 14
        @return results: invoked if gui is TRUE
        """
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
            for r in range(1, len(results)):
                dates.append(results[r][1])
                totals.append(results[r][2])      
            
            if (len(results) == 1):
                print ("There is no data available for the specified timeframe.")
                if (GUI):
                    results = [["There is no data available for the specified timeframe."]]
            else:
                # dates ratings product
                print ("Plotting the data...")
                plt.plot_date(dates, totals, "#993A54")
                plt.legend(loc=1)
                plt.xlabel('Date (MMM-YYYY)')
                plt.xticks(rotation=45)
                plt.ylabel('Value of Sales (£)')
                plt.title('Amount of sales made by salespersonID %s between %s and %s' % (amount_or_productid, startDate, endDate))
                plt.grid(True)
                plt.savefig("assets\\graph.png")
                plt.show()

        # If GUI return the data
        if (GUI):
            return [results]
        else:
            exportToCSV(results)
