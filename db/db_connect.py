import pymongo
import os

connection = pymongo.MongoClient(os.environ.get("MONGO_DB_PATH"))
print("db" ,connection)
# connection = pymongo.MongoClient("mongodb://bornfire:project3@cluster0-shard-00-00.nvora.mongodb.net:27017,cluster0-shard-00-01.nvora.mongodb.net:27017,cluster0-shard-00-02.nvora.mongodb.net:27017/Bornfire?ssl=true&replicaSet=atlas-10s4ho-shard-0&authSource=admin&retryWrites=true&w=majority")
db = connection.get_database("Bornfire")


try:
    print(db.list_collection_names())
    print("🔥 Connected on Bornfire 🔥")
except:
    print("🥶 Connection failed 🥶")





