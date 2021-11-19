from flask import Blueprint, render_template, jsonify, request, redirect
import pymongo
import datetime

from pymongo import cursor

feed = Blueprint("feed", __name__)

connection = pymongo.MongoClient('mongodb://localhost:27017/')
db = connection.get_database("Bornfire")

Feed_collection = db.get_collection("Feed_collection")

@feed.route("/feed")
def get_feed():
    # 이값을 받으면 될 듯. 
    # cursor = request.args.get('cursor')
    cur= 1
    #TODO 디비 갯수 확인 필요 할 듯. 
    cols = Feed_collection.find().sort('_id',-1).skip(10*cur).limit(10)

    col_list = []
    for col in cols:
        col_list.append({
            'nickname': col['nickname'],
            'context' : col['feed'],
            'thumbs-up': col['meta']['thumps-up']
        })


    return render_template('feed.html', datas = col_list)

@feed.route('/feed', methods=['POST'])
def post_feed():
    data = request.json
    nickname = str(data.get('nickname'))
    context = str(data.get('context'))
# 분석 툴이 들어 와서 emotion에 저장. 
# '''
# user_collection에 저장한다. 
# ''' 
    emotion = "good"
    data = {
        'Subject_number' : 1,
        'nickname' : nickname,
        'feed' : context,
        "meta": {'thumps-up': 1, "createAt": datetime.datetime.utcnow()},
        'emotion' : emotion
    }
    # Feed_collection.remove({})
    Feed_collection.insert_one(data)

    cols = Feed_collection.find().sort('_id',-1).limit(1)
    col_list = []
    for col in cols:
        col_list.append({
            'nickname': col['nickname'],
            'context' : col['feed'],
            'thumbs-up': col['meta']['thumps-up']
        })

    return (jsonify(col_list))