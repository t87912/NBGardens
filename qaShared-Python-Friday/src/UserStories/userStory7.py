
from mongoDatabase.MongoQueries import CustomerOrderReviews

def userStory7(sqlConn, conn, GUI, custIDi):  # + GUI (bool) + startDate + endDate etc
    """(Boolean for GUI, customer id):
    This method gives the average ratings a customer has given NBGardens """
    if (not GUI):
        custID = int(input("What is the customer ID you want to view review scores for?: "))
    custID = int(custIDi)
    customerProductScores = CustomerOrderReviews(conn).getProductScoresfCust(custID)
    print (customerProductScores)   
    
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

        customerReviewScores = [avProductScore, avDeliveryScore, avServiceScore]

    if (not GUI):
        print("Average Product Score:      " + customerReviewScores[0] + "\n" + \
              "Average Delivery Score:     " + customerReviewScores[1] + "\n" + \
              "Average Service Score:      " + customerReviewScores[1])

    if (GUI):
        result = [customerReviewScores]
        return result  # result = [[avProductScore, avDeliveryScore, avServiceScore]]


#def customQuery(db, GUI, query):
#    """ customeQuery: Executes user custom query. Need validation here. """
#    if (not GUI):
#        query = input("Input SQL query: ")
#
#    cursor = db.cursor() # Creating the cursor to query the database
#    # Executing the query:
#    try:
#        cursor.execute(query)
#        db.commit()
#        results = cursor.fetchall()
#        for row in results:
#            toPrint = []
#            for i in range(0, len(row)):
#                toPrint.append([row[i]])
#            print (toPrint)
#        if (GUI):
#            return results
#    except:
#        db.rollback()
#        print ("Error: SQL query was invalid.")
