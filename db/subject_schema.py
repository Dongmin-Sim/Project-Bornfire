import pymongo
from collections import OrderedDict
# from datetime import datetime

def create_subject():
    connection = pymongo.MongoClient('mongodb://localhost:27017/')
    db = connection.get_database("Bornfire")

    # usercollection 스키마
    Subject_collection = db.create_collection("Subject_collection")

    db.command({
        'collMod':'Subject_collection',
        'validator' :{"$jsonSchema" : {
            "title" : "Subject_schema",
            "description" : "Schema for supply subject",
            "bsonType" : "object",
            "properties" : {
                "Main_subject" : {
                    "bsonType" : "string",
                },
                "Main_subject_num" : {
                    "bsonType" : "int",
                },
                "Side_subject" : {
                    "bsonType" : "string",
                },
                "Side_subject_num" :{
                    "bsonType" : "int"
                }
            }
        }
    },
    'validationLevel': 'moderate'
})

    return Subject_collection
