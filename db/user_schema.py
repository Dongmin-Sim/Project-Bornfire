import pymongo
from db_connect import db


def create_user():

    db.create_collection("User_collection")
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
    db.command({
        'collMod' : "User_collection",
        'validator' : vexpr,
        'validationLevel' : "moderate"
    })
    
    db.User_collection.create_index([('User_email', 1)], name='User_email', unique=True)

create_user()



