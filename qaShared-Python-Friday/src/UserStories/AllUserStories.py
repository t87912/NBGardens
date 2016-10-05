# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 11:48:47 2016

@author: Administrator
"""

# Import other classes/functions:
from mongoDatabase.MongoQueries import CustomerOrderReviews
from mongoDatabase.MongoQueries import OnlineReviews
from sqlDatabase.SQLQueries import queries
from sqlDatabase.Query import query
from sqlDatabase.SQLQueries import queriesForMongo
from assets.counties import counties

# Other imports:
from exportToCSV import exportToCSV
import matplotlib.pyplot as plt
import time
import numpy as np
from datetime import datetime  
from datetime import timedelta

class AllUserStories (object):
    """ AllUserStories: Explain """
    def __init__(self):
        empty = 0
        empty += 1
        
    def newUserStory(self, db, GUI, autoGen, query_number):
        userStories = autoGen[3]
        
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
            print ("Error: Please input a valid ID.")
            validID = False
        return validID
        
    def validateAgeInput(self, age):
        """ validateProductIDInput: This method accepts a product id (e.g.
            prod id = 1) and validates it. True/false is returned. """
        try:
            int(age)
            validAge = True
        except:
            print ("Error: Please input a valid age.")
            validAge = False
        return validAge

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
        
    def validateCountyInput(self, county):
        if (county in counties):
            validCounty = True
        else:
            print ("Error: Please input a valid county.")
            validCounty = False
        return validCounty
        
    def validateGenderInput(self, gender):
        if (gender in ["Male","Female"]):
            validGender = True
        else:
            print ("Error: Please input a valid gender (Male, Female).")
            validGender = False
        return validGender

    def mongoStory1(self, sqlConn, conn, GUI, custID): # mongo 7
        """ userStory7(Boolean for GUI, customer id): This method does xyz """
        if (not GUI):
            validCustID = False
            while (not validCustID):
                custID = input("CustomerID: ")
                validCustID = self.validateProductIDInput(custID)
            
        custID = int(custID)
        customerProductScores = CustomerOrderReviews(conn).getProductScoresfCust(custID)
        
        if len(customerProductScores) == 0:
            customerReviewScores = "N/A"
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
            for u in range(0, len(customerReviewScores)):
                print (customerReviewScores[u])    
        if (GUI):
            return customerReviewScores

    def mongoStory2(self, sqlConn, conn, GUI, county): # mongo 8
        """ useCase1: Accepts parameter 'period' which is a period, 1-4 """
        if (not GUI):
            validCounty = False
            while (not validCounty):
                county = input("County: ")
                validCounty = self.validateCountyInput(county)
    
        query = queriesForMongo[5] % (county)
        cursor = sqlConn.cursor()  # Creating the cursor to query the database
        # Executing the query:
        try:
            cursor.execute(query)
            sqlConn.commit()
        except:
            sqlConn.rollback()
        custIDs = cursor.fetchall()
        
    
        totalavProductScore = 0
        totalavDeliveryScore = 0
        totalavServiceScore = 0
        count = 0
        for custIDi in custIDs:
            custID = custIDi[0]
            customerProductScores = CustomerOrderReviews(conn).getProductScoresfCust(custID)
            if len(customerProductScores) == 0:
                break
            else:
                totalProductScores = 0
                for i in customerProductScores:
                    totalProductScores += i
                avProductScore = totalProductScores / len(customerProductScores)
                totalavProductScore += avProductScore
    
                customerDeliveryScores = CustomerOrderReviews(conn).getDeliveryScore(custID)
                totalDeliveryScores = 0
                for i in customerDeliveryScores:
                    totalDeliveryScores += i
                avDeliveryScore = totalDeliveryScores / len(customerDeliveryScores)
                totalavDeliveryScore += avDeliveryScore
    
                customerServiceScores = CustomerOrderReviews(conn).getServiceScore(custID)
                totalServiceScores = 0
                for i in customerServiceScores:
                    totalServiceScores += i
                avServiceScore = totalServiceScores / len(customerServiceScores)
                totalavServiceScore += avServiceScore
                count += 1
        if (count==0):
            scoresFromCounty = "N/A"
        else:
            finalProductScore = totalavProductScore / count
            finalServiceScore = totalavServiceScore / count
            finalDeliveryScore = totalavDeliveryScore / count
            scoresFromCounty = [["finalProductScore","finalDeliveryScore","finalServiceScore"],
                                [finalProductScore, finalDeliveryScore, finalServiceScore]]
    
        if (not GUI):
            #print (scoresFromCounty)
            for u in range(0, len(scoresFromCounty)):
                print (scoresFromCounty[u])    
            #print("For customers in " + county + " average review scores are:\n Products: " + finalProductScore + \
             #     "\n Delivery: " + finalDeliveryScore + "\n Service: " + finalServiceScore)
        else:
            result = [scoresFromCounty]
            return result  # result = [[finalProductScore, finalDeliveryScore, finalServiceScore]]

    def mongoStory3(self, sqlConn, conn, GUI, gender, agemin, agemax): # mongo 9
        """ useCase9: """
        if (not GUI):
            validGender = False
            while (not validGender):
                gender = input("Gender (Male, Female): ")
                validGender = self.validateGenderInput(gender)
            validAgeMin = False
            while (not validAgeMin):
                agemin = input("Minimum age: ")
                validAgeMin = self.validateAgeInput(agemin)
            validAgeMax = False
            while (not validAgeMax):
                agemax = input("Maximum age: ")
                validAgeMax = self.validateAgeInput(agemax)
        else:
            agemin = int(agemin)
            agemax = int(agemax) 
        
        agemin = int(agemin)
        agemax = int(agemax)
        gender = str(gender)
        query = queriesForMongo[6] % (gender)
        cursor = sqlConn.cursor()  # Creating the cursor to query the database
        # Executing the query:
        try:
            cursor.execute(query)
            sqlConn.commit()
        except:
            sqlConn.rollback()
        custIDsGender = cursor.fetchall()
    
        now = datetime.now()   
        
        dateFrom = now
        dateTo = now
        for i in range(0, agemax):
            dateFrom = dateFrom + timedelta(days=-365)
        for i in range(0, agemin):
            dateTo   = dateTo + timedelta(days=-365) 
        
        query = queriesForMongo[7] % (dateFrom, dateTo)
        cursor = sqlConn.cursor()  # Creating the cursor to query the database
        # Executing the query:
        try:
            cursor.execute(query)
            sqlConn.commit()
        except:
            sqlConn.rollback()
        custIDsAge = cursor.fetchall()
        
        custIdsAgeSorted = []
        for i in custIDsAge:
            custIdsAgeSorted.append(i[0])
        custIdsGenderSorted = []
        for i in custIDsGender:
            custIdsGenderSorted.append(i[0])
        
        custIDs = list(set(custIdsAgeSorted) & set(custIdsGenderSorted))
    	
        totalavProductScore = 0
        totalavDeliveryScore = 0
        totalavServiceScore = 0
        count = 0
        for custID in custIDs:
            customerProductScores = CustomerOrderReviews(conn).getProductScoresfCust(custID)
            if len(customerProductScores) == 0:
                break
            else:
                totalProductScores = 0
                for i in customerProductScores:
                    totalProductScores += i
                avProductScore = totalProductScores / len(customerProductScores)
                totalavProductScore += avProductScore
    
                customerDeliveryScores = CustomerOrderReviews(conn).getDeliveryScore(custID)
                totalDeliveryScores = 0
                for i in customerDeliveryScores:
                    totalDeliveryScores += i
                avDeliveryScore = totalDeliveryScores / len(customerDeliveryScores)
                totalavDeliveryScore += avDeliveryScore
    
                customerServiceScores = CustomerOrderReviews(conn).getServiceScore(custID)
                totalServiceScores = 0
                for i in customerServiceScores:
                    totalServiceScores += i
                avServiceScore = totalServiceScores / len(customerServiceScores)
                totalavServiceScore += avServiceScore
                count += 1
    
        finalProductScore = totalavProductScore / count
        finalServiceScore = totalavServiceScore / count
        finalDeliveryScore = totalavDeliveryScore / count
        scoresFromDemos = [["finalProductScore","finalDeliveryScore","finalServiceScore"],
                           [finalProductScore, finalDeliveryScore, finalServiceScore]]
    
        if (not GUI):
            #print (scoresFromCounty)
            for u in range(0, len(scoresFromDemos)):
                print (scoresFromDemos[u]) 
        else:
            result = scoresFromDemos
            return result  # result = [[finalProductScore, finalDeliveryScore, finalServiceScore]]



    def mongoStory4(self, sqlConn, conn, GUI, prodID): # mongo 10
        """ useCase10 """
        
        if(not GUI):
            validProdID = False
            while (not validProdID):
                prodID = input("Product ID: ")
                validProdID = self.validateProductIDInput(prodID)
                
        prodID = int(prodID)
        customerReviewScores = CustomerOrderReviews(conn).getProductScores(prodID)
        if len(customerReviewScores) == 0:
            avCustomerScore = "N/A"  
        else:
            totalReviewScores = 0
            for i in customerReviewScores:
                totalReviewScores += i
            avCustomerScore = totalReviewScores / len(customerReviewScores)
        
        onlineReviewScores = OnlineReviews(conn).getOnlineReviewScores(prodID)
        if len(onlineReviewScores) == 0:
                avOnlineScore = "N/A"
            
        else:
            totalReviewScores = 0
            for i in onlineReviewScores:
                totalReviewScores += i
            avOnlineScore = totalReviewScores / len(onlineReviewScores)
            
        reviewScores = [["avCustomerScore","avOnlineScore"],
                        [avCustomerScore, avOnlineScore]]
            
        if(not GUI):
            for u in range(0, len(reviewScores)):
                print (reviewScores[u])            
            
        if(GUI):
            result = reviewScores
            return result
            
    def mongoStory5(self, sqlConn, conn, GUI, dateFrom, dateTo): # mongo 11
        if (not GUI):
            #dateFrom = input("From which date do you want to get review scores?: ")
            #dateTo = input("Until which date?: ")
            validStartDate = False
            validEndDate = False
            while (not validStartDate):
                dateFrom = input("Please enter the start date (YYYY-MM-DD): ")
                validStartDate = self.validateDateInput(dateFrom)
            while (not validEndDate):
                dateTo = input("Please enter the end date (YYYY-MM-DD): ")
                validEndDate = self.validateDateInput(dateTo)
    
        query = queriesForMongo[4] % (dateFrom, dateTo)
        cursor = sqlConn.cursor()  # Creating the cursor to query the database
        # Executing the query:
        try:
            cursor.execute(query)
            sqlConn.commit()
        except:
            sqlConn.rollback()
        orderIDs = cursor.fetchall()
        
        #print(orderIDs)
        totalProductScore = 0
        totalDeliveryScore = 0
        totalServiceScore = 0
        reviewsCount = 0
        for orderID in orderIDs:
            orderID = orderID[0]
            prodScores = CustomerOrderReviews(conn).getProductScoresfOrder(orderID)
            
            totalscore = 0
            count = 0
            for i in prodScores:
                totalscore += i
                count +=1
                    
            if (count == 0):
                count = 1
    
            avProdScore = totalscore / count
            serviceScore = CustomerOrderReviews(conn).getServiceScoresfOrder(orderID)
            deliveryScore = CustomerOrderReviews(conn).getDeliveryScoresfOrder(orderID)
                
            if (serviceScore!=0):
                reviewsCount +=1
    
            totalProductScore += avProdScore
            totalDeliveryScore += serviceScore
            totalServiceScore += deliveryScore
            
        if(reviewsCount == 0):
            reviewsCount = 1
            
        finalProductScore = totalProductScore / reviewsCount
        finalDeliveryScore = totalDeliveryScore / reviewsCount
        finalServiceScore = totalServiceScore / reviewsCount
        result = [["finalProductScore","finalDeliveryScore","finalServiceScore"],
                  [finalProductScore, finalDeliveryScore, finalServiceScore]]
        
        if (not GUI):
            for u in range(0, len(result)):
                print (result[u]) 
    
        if (GUI):
            return result #[[finalProductScore, finalDeliveryScore, finalServiceScore]]
            
    def mongoStory6(self, sqlConn, conn, GUI, dateFrom, dateTo): # mongo 15
        """ useCase15 """
        if (not GUI):
            validStartDate = False
            validEndDate = False
            while (not validStartDate):
                dateFrom = input("Please enter the start date (YYYY-MM-DD): ")
                validStartDate = self.validateDateInput(dateFrom)
            while (not validEndDate):
                dateTo = input("Please enter the end date (YYYY-MM-DD): ")
                validEndDate = self.validateDateInput(dateTo)
            
        dateFrom = datetime.strptime(dateFrom, '%Y-%m-%d')
        dateTo = datetime.strptime(dateTo, '%Y-%m-%d')
        dateUntil = dateFrom + timedelta(days=30)
        graphData = []
        whileCount = 0
        while(dateUntil < dateTo and whileCount < 20):
            totalProductScore = 0
            totalDeliveryScore = 0
            totalServiceScore = 0
            dateFroms = dateFrom.date().strftime('%Y-%m-%d') 
            dateUntils = dateUntil.date().strftime('%Y-%m-%d')
            
            query = queriesForMongo[4] % (dateFroms, dateUntils)
            cursor = sqlConn.cursor()  # Creating the cursor to query the database
            # Executing the query:
            try:
                cursor.execute(query)
                sqlConn.commit()
            except:
                sqlConn.rollback()
            orderIDs = cursor.fetchall()
    
            reviewsCount = 0
            
            for orderID in orderIDs:
                orderID = orderID[0]
                prodScores = CustomerOrderReviews(conn).getProductScoresfOrder(orderID)
            
                totalscore = 0
                count = 0
                for i in prodScores:
                    totalscore += i
                    count +=1
                    
                if (count == 0):
                    count = 1
    
                avProdScore = totalscore / count
                serviceScore = CustomerOrderReviews(conn).getServiceScoresfOrder(orderID)
                deliveryScore = CustomerOrderReviews(conn).getDeliveryScoresfOrder(orderID)
                
                if (serviceScore!=0):
                    reviewsCount +=1
    
                totalProductScore += avProdScore
                totalDeliveryScore += serviceScore
                totalServiceScore += deliveryScore
            
            if(reviewsCount == 0):
                reviewsCount = 1
            
            finalProductScore = totalProductScore / reviewsCount
            finalDeliveryScore = totalDeliveryScore / reviewsCount
            finalServiceScore = totalServiceScore / reviewsCount
            
            graphData.append([finalProductScore, finalDeliveryScore, finalServiceScore, dateUntil.strftime('%Y-%m-%d')])        
            
            dateUntil   = dateUntil + timedelta(days=30)
            whileCount += 1
            
        result = ["finalProductScore","finalDeliveryScore","finalServiceScore","date"]
        graphData.insert(0, result)
        
        # graph the results:
        productScores = []
        deliveryScores = []
        serviceScores = []
        datesList = []
        for r in range(1, len(graphData)):
            productScores.append(graphData[r][0])
            deliveryScores.append(graphData[r][1])
            serviceScores.append(graphData[r][2])
            date_object = datetime.strptime(graphData[r][3], '%Y-%m-%d')
            datesList.append(date_object)
    
        if (len(graphData) == 1):
            print ("There is no data available for the specified timeframe.")
            if (GUI):
                graphData = [["There is no data available for the specified timeframe."]]
        else:
            print ("Plotting the data...")
            #plt.plot(datesList, productScores)
            #plt.plot(datesList, deliveryScores)
            #plt.plot(datesList, serviceScores)
            plt.plot_date(datesList, productScores)            
            plt.plot_date(datesList, deliveryScores)
            plt.plot_date(datesList, serviceScores)            
            #width = 0.35       # the width of the bars
            # Below is a hacky solution to showing the bars on seperate x axis
            # positions, just take 0.2 off each to offset
            # Bascially aligns prodID bar directly over prodID x tick
            plt.xlabel('Date (YYYY-MM-DD)')
            plt.ylabel('Customer satisfaction (x/10)')
            plt.title('Levels of customer satisfaction in a range of areas between %s and %s' % (dateFrom, dateTo))
            plt.grid(True)
            plt.savefig("assets\\graph.png")
            plt.show()

        if (not GUI):
            for u in range(0, len(graphData)):
                print (graphData[u])       
        
        if (GUI):
            return graphData

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
            return results
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
            return results
        else:
            exportToCSV(results)

    def userStorySeries2(self, db, GUI, startDate, endDate, amount_or_productid, query_number):
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
                #plt.legend(loc=1)
                plt.xlabel('Date (MMM-YYYY)')
                plt.xticks(rotation=45)
                plt.ylabel('Value of Sales (£)')
                plt.title('Amount of sales made by salespersonID %s between %s and %s' % (amount_or_productid, startDate, endDate))
                plt.grid(True)
                plt.savefig("assets\\graph.png")
                plt.show()

        # If GUI return the data
        if (GUI):
            return results
        else:
            exportToCSV(results)
