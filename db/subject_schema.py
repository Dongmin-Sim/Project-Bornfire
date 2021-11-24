import pymongo
from db_connect import db

def create_subject():

    db.create_collection("Subject_collection")

    vexpr = {
        "$jsonSchema" : {
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
    }
    db.command({
        'collMod' : "Subject_collection",
        'validator' : vexpr,
        'validationLevel' : "moderate"
    })

create_subject()