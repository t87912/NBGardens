from datetime import datetime  
from datetime import timedelta 
from mongoDatabase.MongoQueries import CustomerOrderReviews
from sqlDatabase.SQLQueries import queriesForMongo

def userStory9(sqlConn, conn, GUI, gender, agemin, agemax):
    """(boolean for GUI, sql database reference?, string, int, int):
    This method returns the average ratings for customers of specific gender and age range"""
    if (not GUI):
        gender = input("Which gender do you want reviews from? (Male, Female, Both):")
        agemin = int(input("What is the minimum age of customer you want reviews from?:"))
        agemax = int(input("What is the maximum age of customer you want reviews from?:"))
    else:
        agemin = int(agemin)
        agemax = int(agemax) 
    
    query = queriesForMongo[6] % (gender)
    cursor = sqlConn.cursor()  # Creating the cursor to query the database
    # Executing the query:
    try:
        cursor.execute(query)
        sqlConn.commit()
    except:
        sqlConn.rollback()
    custIDsGender = cursor.fetchall()

    now = datetime.now().date()
    
    dateFrom = now
    dateTo = now
    for i in range(0, agemax):
        dateFrom = dateFrom + timedelta(days=-365)
    for i in range(0, agemin):
        dateTo   = dateTo + timedelta(days=-365)
    
    dateFrom = str(dateFrom)
    dateTo = str(dateTo)
    
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
    
    if(count == 0):
        count = 1
        
    finalProductScore = totalavProductScore / count
    finalServiceScore = totalavServiceScore / count
    finalDeliveryScore = totalavDeliveryScore / count
    scoresFromDemos = [finalProductScore, finalDeliveryScore, finalServiceScore]

    if (not GUI):
        print("For " + gender +" customers between the ages of " + str(agemin) + " and " + agemax + " average review scores are:\n Products: " + finalProductScore + \
              "\n Delivery: " + finalDeliveryScore + "\n Service: " + finalServiceScore)
    else:
        result = [scoresFromDemos]
        return result  # result = [[finalProductScore, finalDeliveryScore, finalServiceScore]]