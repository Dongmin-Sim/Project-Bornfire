import pymongo

connection = pymongo.MongoClient('mongodb://localhost:27017/')
db = connection.get_database("Bornfire")

Feed_collection = db.get_collection("Feed_collection")
User_collection = db.get_collection("User_collection")
