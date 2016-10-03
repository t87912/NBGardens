from mongoDatabase.MongoQueries import CustomerOrderReviews
from sqlDatabase.SQLQueries import queriesForMongo
from datetime import datetime, timedelta

def userStory15(sqlConn, conn, GUI, dateFrom, dateTo):
    """(sqlDB, MongoDB, boolean for GUI, Start date for graph, end date, increment in days):
    This method outputs a graph showing the levels of customer satisfaction over a period of time"""
        
    if (not GUI):
        dateFrom = input("From which date do you want the graph to start?: ")
        dateTo = input("Which date should it finish on?: ")
        
    dateFrom = datetime.strptime(dateFrom, '%Y-%m-%d')
    dateTo = datetime.strptime(dateTo, '%Y-%m-%d')
    dateUntil = dateFrom + timedelta(days=30)
    graphData = []
    whileCount = 0
    while(dateUntil < dateTo and whileCount < 20):
        totalProductScore = 0
        totalDeliveryScore = 0
        totalServiceScore = 0
        dateFroms = dateFrom.date().strftime('%Y/%m/%d') 
        dateUntils = dateUntil.date().strftime('%Y/%m/%d')
        
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
        
        graphData.append([finalProductScore, finalDeliveryScore, finalServiceScore, dateUntil.strftime('%Y/%m/%d')])        
        
        dateUntil   = dateUntil + timedelta(days=30)
        whileCount += 1
    return graphData
    
    
    
    
    
    
    