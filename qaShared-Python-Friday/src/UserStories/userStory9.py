from datetime import datetime  
from datetime import timedelta 
from mongoDatabase.MongoQueries import CustomerOrderReviews
from sqlDatabase.SQLQueries import queriesForMongo

def userStory9(GUI, sqlDB, gender, agemin, agemax):
    """(boolean for GUI, sql database reference?, string, int, int):
    This method returns the average ratings for customers of specific gender and age range"""
    if (not GUI):
        county = input("Which gender do you want reviews from? (Male, Female, Both):")
        agemin = int(input("What is the minimum age of customer you want reviews from?:"))
        agemax = int(input("What is the maximum age of customer you want reviews from?:"))
		
    query = queriesForMongo[6] % (gender)
    cursor = sqlDB.cursor()  # Creating the cursor to query the database
    # Executing the query:
    try:
        cursor.execute(query)
        sqlDB.commit()
    except:
        sqlDB.rollback()
    custIDsGender = cursor.fetchall()

    now = datetime.datetime.now()
    dateNow = now.strftime("%Y-%m-%d")
    dateFrom = dateNow - datetime.timedelta(days=365*agemax)
    dateTo   = dateNow - datetime.timedelta(days=365*agemin)
	
    query = queriesForMongo[7] % (dateFrom, dateTo)
    cursor = sqlDB.cursor()  # Creating the cursor to query the database
    # Executing the query:
    try:
        cursor.execute(query)
        sqlDB.commit()
    except:
        sqlDB.rollback()
    custIDsAge = cursor.fetchall()
	
    custIDs = custIDsGender.intersection(custIDsAge)
	
    totalavProductScore = 0
    totalavDeliveryScore = 0
    totalavServiceScore = 0
    count = 0
    for custID in custIDs:
        customerProductScores = CustomerOrderReviews.getProductScoresfCust(custID)
        if len(customerProductScores) == 0:
            break
        else:
            totalProductScores = 0
            for i in customerProductScores:
                totalProductScores += i
            avProductScore = totalProductScores / len(customerProductScores)
            totalavProductScore += avProductScore

            customerDeliveryScores = CustomerOrderReviews.getDeliveryScore(custID)
            totalDeliveryScores = 0
            for i in customerDeliveryScores:
                totalDeliveryScores += i
            avDeliveryScore = totalDeliveryScores / len(customerDeliveryScores)
            totalavDeliveryScore += avDeliveryScore

            customerServiceScores = CustomerOrderReviews.getServiceScore(custID)
            totalServiceScores = 0
            for i in customerServiceScores:
                totalServiceScores += i
            avServiceScore = totalServiceScores / len(customerServiceScores)
            totalavServiceScore += avServiceScore
            count += 1

    finalProductScore = totalavProductScore / count
    finalServiceScore = totalavServiceScore / count
    finalDeliveryScore = totalavDeliveryScore / count
    scoresFromDemos = [finalProductScore, finalDeliveryScore, finalServiceScore]

    if (not GUI):
        print("For customers in " + county + " average review scores are:\n Products: " + finalProductScore + \
              "\n Delivery: " + finalDeliveryScore + "\n Service: " + finalServiceScore)
    else:
        result = [scoresFromDemos]
        return result  # result = [[finalProductScore, finalDeliveryScore, finalServiceScore]]