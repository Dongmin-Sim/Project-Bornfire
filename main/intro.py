from collections import defaultdict
from bson.son import SON
from dateutil.relativedelta import relativedelta
from flask import Blueprint, render_template


from .mongo_connect import db
from datetime import datetime

Feed_collection  = db.get_collection("Feed_collection")
Subject_collection = db.get_collection("Subject_collection")

intro = Blueprint("intro", __name__)



@intro.route("/")
def get_intro():
    now = datetime.today()
    today = datetime(now.year, now.month, now.day)
    yesterday = (today + relativedelta(days = -1))
    today_zero = (today + relativedelta(hours=0))
  
 
    pipe = [
        {"$match" : {"Meta.Created_at": {"$gte":yesterday, "$lt": today_zero}}},
        {"$project" :{'Main_subject_num': 1, 'Side_subject_num': 1, 'Feed' :1 ,"Meta.Created_at":1, "Meta.Likes": 1, 'Likes': {"$size": "$Meta.Likes"}, 'Predicted_value':1}},
        {"$sort": SON([('Likes', -1)])},
        {"$limit": 5}
    ]

    

    # cols = list(Feed_collection.find(query).sort("Meta.Likes", 1))
    cols = list(Feed_collection.aggregate(pipe))
    query = {"Main_subject_num": cols[0]['Main_subject_num'], "Side_subject_num" : cols[0]['Side_subject_num']}
    projection = {"Side_subject": 1, "_id": 0}
    yesterday_subject = (Subject_collection.find_one(query,projection))['Side_subject']
    
    predicted_value = defaultdict(int)

    for col in cols:
        value = col['Predicted_value']
        predicted_value[value] += 1
    
    sorted_predicted = sorted(predicted_value.items())
    predicted_value = dict(sorted_predicted)


    return render_template('intro.html', lanks=cols, yesterday_subject = yesterday_subject, predicted_value = predicted_value)

    