import pymongo
import os

connection = pymongo.MongoClient(os.environ.get("MONGO_DB_PATH"))
db = connection.get_database("Bornfire")



if __name__ == "__main__":
    try:
        print(db.list_collection_names())
        print("🔥 Connected on Bornfire 🔥")
    except(e):
        
        print("🥶 Connection failed 🥶")