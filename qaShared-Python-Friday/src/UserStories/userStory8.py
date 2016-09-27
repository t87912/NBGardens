from mongoDatabase.MongoQueries import CustomerOrderReviews
from sqlDatabase.SQLQueries import queriesForMongo

def userStory8(sqlConn, conn, GUI, county):
    """(boolean for GUI, sql database reference?, string):
    This method returns the average ratings for customers from a specific county"""
    if (not GUI):
        county = input("Which county would you like to search for customer ratings from?")

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
        scoresFromCounty = [finalProductScore, finalDeliveryScore, finalServiceScore]

    if (not GUI):
        print("For customers in " + county + " average review scores are:\n Products: " + finalProductScore + \
              "\n Delivery: " + finalDeliveryScore + "\n Service: " + finalServiceScore)
    else:
        result = [scoresFromCounty]
        return result  # result = [[finalProductScore, finalDeliveryScore, finalServiceScore]]


