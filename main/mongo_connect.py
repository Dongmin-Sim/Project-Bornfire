import pymongo

connection = pymongo.MongoClient("mongodb://bornfire:project3@cluster0-shard-00-00.nvora.mongodb.net:27017,cluster0-shard-00-01.nvora.mongodb.net:27017,cluster0-shard-00-02.nvora.mongodb.net:27017/Bornfire?ssl=true&replicaSet=atlas-10s4ho-shard-0&authSource=admin&retryWrites=true&w=majority")
db = connection.get_database("Bornfire")



if __name__ == "__main__":
    try:
        print(db.list_collection_names())
        print("🔥 Connected on Bornfire 🔥")
    except:
        print("🥶 Connection failed 🥶")