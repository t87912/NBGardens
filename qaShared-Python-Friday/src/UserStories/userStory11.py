from mongoDatabase.MongoQueries import CustomerOrderReviews
from sqlDatabase.SQLQueries import queriesForMongo
from datetime import datetime

def userStory11(sqlConn, conn, GUI, dateFrom, dateTo):
    """(db is sql database, boolean for GUI, a date from when to get review scores from, and to):
     This method returns the average customer review scores in 3 areas of the business over a given period of time """
        
    if (not GUI):
        dateFrom = input("From which date do you want to get review scores?: ")
        dateTo = input("Until which date?: ")

    totalProductScore = 0
    totalDeliveryScore = 0
    totalServiceScore = 0
    
    query = queriesForMongo[4]
    cursor = sqlConn.cursor()  # Creating the cursor to query the database
    # Executing the query:
    try:
        cursor.execute(query)
        sqlConn.commit()
    except:
        sqlConn.rollback()
    orderIDs = cursor.fetchall()
    
    dateFrom = datetime.strptime(dateFrom, '%Y/%m/%d')
    dateTo = datetime.strptime(dateTo, '%Y/%m/%d')
    
    reviewsCount = 0
    
    for orderID in orderIDs:
        orderID = orderID[0]
        
        query = queriesForMongo[3] % (orderID)
        cursor = sqlConn.cursor()  # Creating the cursor to query the database
        # Executing the query:
        try:
            cursor.execute(query)
            sqlConn.commit()
        except:
            sqlConn.rollback()
        orderDate = cursor.fetchall()
        
        orderDate = orderDate[0][0]
        orderDate = datetime.combine(orderDate, datetime.min.time())
        
        if (dateFrom < orderDate < dateTo):        
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

    finalProductScore = totalProductScore / reviewsCount
    finalDeliveryScore = totalDeliveryScore / reviewsCount
    finalServiceScore = totalServiceScore / reviewsCount

    if (GUI):
        result = [finalProductScore, finalDeliveryScore, finalServiceScore]
        return [result] #[[finalProductScore, finalDeliveryScore, finalServiceScore]]
