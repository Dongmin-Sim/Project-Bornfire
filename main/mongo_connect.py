import pymongo
from .env import MONGO_DB_PATH

connection = pymongo.MongoClient(MONGO_DB_PATH)
db = connection.get_database("Bornfire")



if __name__ == "__main__":
    try:
        print(db.list_collection_names())
        print("🔥 Connected on Bornfire 🔥")
    except:
        print("🥶 Connection failed 🥶")