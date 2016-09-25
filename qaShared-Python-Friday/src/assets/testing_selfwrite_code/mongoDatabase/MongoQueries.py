#from pymongo import MongoClient
#conn = MongoClient()
#db = conn.NBGardensMongo

#MONGODB_URI = 'mongodb://master:pa$$w0rd@ds019766.mlab.com:19766/nbgardens'

#conn = MongoClient(MONGODB_URI)

#db = conn.get_default_database() 

class OnlineReviews:
    ##### accesses OnlineReviews Collection #####
    def getOnlineReviews(i):
        ##### returns array with all reviews for product with id = i #####
        reviews = db.OnlineReviews.find({"product_id" : i})
        reviewArray = []
        for doc in reviews:
            rev = doc["review"]
            reviewArray.append(rev)
            print(reviewArray)
        return reviewArray
        
    def getOnlineReviewScores(i):
        ##### returns array with all scores for a product with id = i #####
        reviews = db.OnlineReviews.find({"product_id" : i})
        reviewArray = []
        for doc in reviews:
            rev = doc["score"]
            reviewArray.append(rev)
        return reviewArray
        

class ProductDetails:
    ##### accesses ProductDetails Collection #####
    def getProductDetails(i):
        ##### returns a document with all product details contained #####
        product = db.ProductDetails.find({"_id" : i})
        for prod in product:
            det = prod
        return det
            
    def getProductName(i):
        ##### returns the products name from product id #####
        product = db.ProductDetails.find({"_id" : i})
        for prod in product:
            name = prod["name"]
        return name
        
    def getProductDescription(i):
        ##### returns the products description from product id #####
        product = db.ProductDetails.find({"_id" : i})
        for prod in product:
            desc = prod["description"]
        return desc
        
class CustomerOrderReviews(object):
    ##### accesses CustomerOrderReviews Collection #####
    def __init__(self, conn):
        self.conn = conn
        self.db = self.conn.get_default_database() 


    class fOrder(object):
        ##### returns details from customer orders from order number
        def __init__(self, conn):
            self.conn = conn
            self.db = conn.get_default_database() 
            
        def getProductScoresfOrder(self, i):
            reviews = self.db.CustomerReviews.find({"_id":i})
            productScores = []
            for rev in reviews:
                products = rev["products"]
                for prod in products:
                    productScores.append(prod["score"])
            return productScores
            
        def getServiceScoresfOrder(self, i):
            reviews = self.db.CustomerReviews.find({"_id":i})
            for rev in reviews:
                score = rev["customerServiceScore"]
            return score
            
        def getDeliveryScoresfOrder(self, i):
            reviews = self.db.CustomerReviews.find({"_id":i})
            for rev in reviews:
                score = rev["deliveryScore"]
            return score

    def getCustomerOrders(self):
        ##### returns list of cutomer order ID's #####
        reviews = self.db.CustomerReviews.find({})
        custIDs = []
        for rev in reviews:
            custIDs.append(rev["_id"])
        return custIDs

    def getProductScores(self, i):
        ##### returns an array of the products scores from product id #####
        reviews = self.db.CustomerReviews.find({})
        productScores = []
        for rev in reviews:
            products = rev["products"]
            for prod in products:
                if prod["product_id"] == i:
                    productScores.append(prod["score"])
        return productScores

    def getProductScoresfCust(self, i):
        ##### returns an array of the products scores from customer id #####
        reviews = self.db.CustomerReviews.find({})
        productReviews = []
        for rev in reviews:
            if rev["customer_id"] == i:
                products = rev["products"]
                for prod in products:
                    productReviews.append(prod["score"])      
        return productReviews
                    
    def getProductReviewsfProd(self, i):
        ##### returns an array of the products reviews from product id #####
        reviews = self.db.CustomerReviews.find({})
        productReviews = []
        for rev in reviews:
            products = rev["products"]
            for prod in products:
                if prod["product_id"] == i:
                    productReviews.append(prod["review"])
        return productReviews
        
    def getProductReviewsfCust(self, i):
        ##### returns an array of the products reviews from customer id #####
        reviews = self.db.CustomerReviews.find({})
        productReviews = []
        for rev in reviews:
            if rev["customer_id"] == i:
                products = rev["products"]
                for prod in products:
                    productReviews.append(prod["review"])
        return productReviews
        
    def getServiceScore(self, i):
        ##### returns serviceScores for a particular customer from customerID #####
        reviews = self.db.CustomerReviews.find({"customer_id" : i})
        serviceScores = []
        for rev in reviews:
            serviceScore = rev["customerServiceScore"]
            serviceScores.append(serviceScore)
        return serviceScores
        
    def getDeliveryScore(self, i):
        ##### returns deliveryScores for a particular customer from customerID #####
        reviews = self.db.CustomerReviews.find({"customer_id" : i})
        deliveryScores = []
        for rev in reviews:
            deliveryScore = rev["customerServiceScore"]
            deliveryScores.append(deliveryScore)
        return deliveryScores
        
class UserStories:
    
    def averageRatingForCustomer(i):
        ##### gets the average score a customer has given products #####
        scores = CustomerOrderReviews.getProductScoresfCust(i)
        totalScore = 0
        count = 0
        for i in scores:
            totalScore += i
            count += 1
        return totalScore/count
        
    def averageRatingForProduct(i):
        ##### gets the average score a customer has given products #####
        scores = CustomerOrderReviews.getProductScores(i)
        totalScore = 0
        count = 0
        for i in scores:
            totalScore += i
            count += 1
        return totalScore/count
        
    def deliveryScoresOverTime(self):
        ##### UNFINISHED NEED SQL DATE QUERY #####
        reviews = db.CustomerReviews.find()
        totalScore = 0
        count = 0
        for rev in reviews:
            customerOrderID = rev["_id"]
            #if (dateTo < customerOrderDate < dateFrom):     
            totalScore += rev["deliveryScore"]
            count += 1
        return totalScore/count
            
    def customerServiceScoresOverTime(self):
        ##### UNFINISHED NEED SQL DATE QUERY #####
        reviews = db.CustomerReviews.find()
        totalScore = 0
        count = 0
        for rev in reviews:
            customerOrderID = rev["_id"]
            #if (dateTo < customerOrderDate < dateFrom):
            totalScore += rev["customerServiceScore"]
            count += 1
        return totalScore/count    
        
#customerProductScores = CustomerOrderReviews.getProductScoresfCust(1)
#print (customerProductScores)
        
