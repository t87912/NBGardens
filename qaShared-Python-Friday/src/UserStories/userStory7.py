# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""

def userStory7(MongoQueries, GUI, custID): # + GUI (bool) + startDate + endDate etc
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