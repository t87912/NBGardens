# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 21:24:58 2016

@author: user
"""

def userStory10(MongoQueries, GUI, productID):
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