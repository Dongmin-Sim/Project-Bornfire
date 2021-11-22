import pymongo
import feed_schema 
import subject_schema 
import user_schema 

if __name__ == "__main__":
    connection = pymongo.MongoClient('mongodb://localhost:27017/')
    db = connection.get_database("Bornfire")
    list = db.list_collection_names()

    if "Feed_collection" in list:
        Feed_collection = db.get_collection("Feed_collection")
    else:    
        Feed_collection = feed_schema.create_feed()

    if "User_collection" in list:
        User_collection = db.get_collection("User_collection")
    else:    
        User_collection = user_schema.create_user()

    if "Subject_collection" in list:
        Subject_collection = db.get_collection("Subject_collection")
    else:    
        Subject_collection = subject_schema.create_subject()
