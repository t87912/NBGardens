from MongoQueries import CustomerOrderReviews

def userStory11(db, GUI, dateFrom, dateTo):
    """(db is sql database, boolean for GUI, a date from when to get review scores from, and to):
     This method returns the average customer review scores in 3 areas of the business over a given period of time """
        
    if (not GUI):
        dateFrom = input("From which date do you want to get review scores?: ")
        dateTo = input("Until which date?: ")

    totalProductScore = 0
    totalDeliveryScore = 0
    totalServiceScore = 0
    
    query = queriesForMongo[4]
    cursor = sqlDB.cursor()  # Creating the cursor to query the database
    # Executing the query:
    try:
        cursor.execute(query)
        sqlDB.commit()
    except:
        sqlDB.rollback()
    orderIDs = cursor.fetchall()
    
    for orderID in orderIDs:
        
        query = queriesForMongo[3] % (orderID)
		cursor = sqlDB.cursor()  # Creating the cursor to query the database
		# Executing the query:
		try:
			cursor.execute(query)
			sqlDB.commit()
		except:
			sqlDB.rollback()
		orderDate = cursor.fetchall()
        
        if (dateFrom < orderDate < dateTo):        
        
            prodScores = CustomerOrderReviews.fOrder.getProductScoresfOrder()
            totalscore = 0
            count = 0
            for i in prodScores:
                totalscore += i
                count +=1

            avProdScore = totalscore / len(prodScores)
            serviceScore = CustomerOrderReviews.fOrder.getServiceScoresfOrder(i)
            deliveryScore = CustomerOrderReviews.fOrder.getDeliveryScoresfOrder(i)

            totalProductScore += avProdScore
            totalDeliveryScore += serviceScore
            totalServiceScore += deliveryScore

    finalProductScore = totalProductScore / len(count)
    finalDeliveryScore = totalDeliveryScore / len(orderIDs)
    finalServiceScore = totalServiceScore / len(orderIDs)

    if (GUI):
        result = [finalProductScore, finalDeliveryScore, finalServiceScore]
        return [result] #[[finalProductScore, finalDeliveryScore, finalServiceScore]]
