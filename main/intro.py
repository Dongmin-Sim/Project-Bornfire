from os import pipe
from bson.son import SON
from dateutil.relativedelta import relativedelta
from flask import Blueprint, render_template, jsonify, request, redirect
from pymongo.message import query
from .mongo_connect import db
from datetime import datetime

Feed_collection  = db.get_collection("Feed_collection")

intro = Blueprint("intro", __name__)

@intro.route("/")
def get_intro():
    now = datetime.today()
    today = datetime(now.year, now.month, now.day)
    yesterday = (today + relativedelta(days = -1))
    today_zero = (today + relativedelta(hours=0))
  
 
    pipe = [
        {"$match" : {"Meta.Created_at": {"$gte":yesterday, "$lt": today_zero}}},
        {"$project" :{'Feed' :1 ,"Meta.Created_at":1, "Meta.Likes": 1, 'Likes': {"$size": "$Meta.Likes"}}},
        {"$sort": SON([('Likes', -1)])},
        {"$limit": 5}
    ]

    # cols = list(Feed_collection.find(query).sort("Meta.Likes", 1))
    cols = list(Feed_collection.aggregate(pipe))

    return render_template('intro.html')

    