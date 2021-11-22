import pymongo

def create_feed():
    connection = pymongo.MongoClient('mongodb://localhost:27017/')
    db = connection.get_database("Bornfire")

    # usercollection 스키마
    # Feed_collection = db.get_collection("Feed_collection")
    # db.Feed_collection.drop()
    Feed_collection = db.create_collection("Feed_collection")

    #validator 적용하기
    db.command( {
        'collMod': "Feed_collection",
        'validator' :{ '$jsonSchema':{
                'bsonType': "object",
                'required': ["Main_subject_num",'Side_subject_num', 'Meta', 'emotion' ],
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
                                'bsonType': 'timestamp'
                            }
                        }
                    },
                    'Predicted_value': {
                        'bsonType' : 'int'
                    }
                }
            }

        },
        'validationLevel': "moderate"
    })

    return Feed_collection
