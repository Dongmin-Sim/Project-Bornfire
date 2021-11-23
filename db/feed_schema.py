import pymongo
from .db_connect import db as db


def create_feed():

    db.create_collection("Feed_collection")

    vexpr = { 
        '$jsonSchema':{
                'bsonType': "object",
                'required': ["Main_subject_num",'Side_subject_num', 'Meta', 'Predicted_value' ],
                'properties': {
                    'Main_subject_num' :{
                        'bsonType' : "int",
                    },
                    'Side_subject_num':{
                        'bsonType' : "int",
                    },
                    'Feed' : {
                        'bsonType': "string",
                        'minLength': 1
                    },
                    'Meta':{
                        'bsonType': "object",
                        'required' : ["Likes", "Created_at"],
                        'properties' : {
                            'Likes' :{
                                'bsonType' : 'array',
                                'items':{
                                    "bsonType" : "string",
                                    "pattern" : "^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
                                },
                                "uniqueItems": True
                            },
                            'Created_at':{
                                'bsonType': 'date'
                            }
                        }
                    },
                    'Predicted_value': {
                        'bsonType' : 'int'
                    }
                }
            }
        }

    db.command({
        'collMod' : "Feed_collection",
        'validator' : vexpr,
        'validationLevel' : "moderate"
    })

create_feed()
