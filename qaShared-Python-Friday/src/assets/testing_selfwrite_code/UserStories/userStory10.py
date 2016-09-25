from mongoDatabase.MongoQueries import CustomerOrderReviews, OnlineReviews

def userStory10(GUI, prodID):
    """(boolean for GUI, int for productID):
	This method returns an array with the average customer score and average online score for the selected product"""

    if(not GUI):
        prodID = int(input("What is the product ID you want to view review scores for?: "))
        
    customerReviewScores = CustomerOrderReviews.getProductScores(prodID)
    if len(customerReviewScores) == 0:
        avCustomerScore = "N/A"  
    else:
        totalReviewScores = 0
        for i in customerReviewScores:
            totalReviewScores += i
        avCustomerScore = totalReviewScores / len(customerReviewScores)
            
    onlineReviewScores = OnlineReviews.getOnlineReviewScores(prodID)
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