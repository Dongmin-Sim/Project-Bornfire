import pymongo
from collections import OrderedDict
# from datetime import datetime

def create_user():
    connection = pymongo.MongoClient('mongodb://localhost:27017/')
    db = connection.get_database("Bornfire")

    # usercollection 스키마
    db.User_collection.drop()

    User_collection = db.create_collection("User_collection")

    vexpr = {
        "$jsonSchema" : {
            "title" : "User_schema",
            "description" : "User schema contains email, password, emotion",
            "bsonType" : "object",
            "required" : ["User_email", "User_pw"],
            "properties" : {
                "User_email" : {
                    "bsonType" : "string",
                    "pattern" : "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                },
                "User_pw" : {
                    "bsonType" : "string",
                },
                "User_feed_log" : {
                    "bsonType" : "array",
                    "items" : { # {Created_at:Predicted_value}
                        "type" : "object"
                    }
                },
                "Verify_question": {
                    "bsonType" : "object" #{"question:answer"}의 형태로 집어넣을 예정
                }
            }
        }
    }
    db.User_collection.create_index([('User_email', 1)], name='User_email', unique=True)




    cmd = OrderedDict([('collMod','User_collection'),
                                    ('validator', vexpr),
                                    ('validationLevel', 'strict')])

    db.command(cmd)

    return User_collection
