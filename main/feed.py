from flask import Blueprint, render_template, jsonify, request, redirect, session, abort
import datetime
from bson import ObjectId
from pymongo import cursor
from .mongo_connect import db
from .nickname import make_nickname
import functools
import time
import random
from apscheduler.schedulers.background import BackgroundScheduler

User_collection = db.get_collection("User_collection")
Feed_collection = db.get_collection("Feed_collection")
Subject_collection = db.get_collection("Subject_collection")


def s_supply():
    global m_num
    global s_num
    global subject
    m_num = random.randint(1,13)
    s_num = random.randint(0,4)
    subject = Subject_collection.find_one({"$and" : [{"Main_subject_num":m_num},{"Side_subject_num":s_num}]})['Side_subject']

s_supply()

sched = BackgroundScheduler(daemon = True,timezone="Asia/Seoul")
sched.add_job(s_supply,'interval',seconds=60)
sched.start()

feed = Blueprint("feed", __name__)



def login_required(func):
    @functools.wraps(func)
    def wrapped_view(**kwargs):
        user = session.get('user_email')
        if user is None:
            return abort(404)
        return func(**kwargs)

    return wrapped_view

@feed.route("/feed")
def get_feed():
    
    query = {"$and" : [{"Main_subject_num":m_num},{"Side_subject_num":s_num}]}

    cols = Feed_collection.find(query).sort('_id',-1).limit(9)

    col_list = []
    for col in cols:
        col_list.append({
            '_id' : col["_id"],
            'nickname': make_nickname(),
            'context' : col['Feed'],
            'thumbs-up': len(col['Meta']['Likes'])
        })

    return render_template('feed.html', datas = col_list, subject = subject)


@feed.route('/feed', methods=['POST'])
@login_required
def post_feed():
    data = request.json
    email = str(session['user_email'])
    context = str(data.get('context'))
    if len(context) == 0:
        return abort(501)
    
    #TODO 분석 툴이 들어 와서 emotion에 저장. 
    from model.predict_sen import get_sentiment

    predicted = get_sentiment(context)

    time = datetime.datetime.utcnow()
    emotion = predicted[1]
    print(emotion)
    
    log = {str(time): emotion}
    User_collection.update_one({'User_email': email}, { '$push': { 'User_feed_log': log } })

    data = {
        'Main_subject_num' : m_num,
        'Side_subject_num': s_num,
        'Feed' : context,
        "Meta": {'Likes': [], "Created_at": time},
        'Predicted_value' : emotion
    }
    # Feed_collection.remove({})
    Feed_collection.insert_one(data)
    query = {"$and" : [{"Main_subject_num":m_num},{"Side_subject_num":s_num}]}

    cols = Feed_collection.find(query).sort('_id',-1).limit(1)
    #TODO [DB 정보 확인]DB에서 error가 났을 때,  예외 처리 필요. 
    
    col_list = []
    for col in cols:
        col_list.append({
            '_id' : str(col["_id"]), 
            'nickname': make_nickname(),
            'context' : col['Feed'],
            'thumbs-up': len(col['Meta']['Likes'])
        })

    return (jsonify(col_list))

@feed.route("/inifinity", methods=['POST'])
def infinity_page():
    data = request.json
    query = {"$and" : [{"Main_subject_num":m_num},{"Side_subject_num":s_num}]}

    cols = Feed_collection.find(query).sort('_id',-1).skip(10*data['page']).limit(9)

    col_list = []
    for col in cols:
        col_list.append({
            '_id' : str(col["_id"]),
            'nickname': make_nickname(),
            'context' : col['Feed'],
            'thumbs-up': len(col['Meta']['Likes'])
        })

# TODO subject collection 넘겨 주는 것 필요.
    return jsonify(col_list)

@feed.route('/likes', methods=["UPDATE"])
@login_required
def like():
    data = request.json
    email = str(session['user_email'])

    #query
    find_query = {'_id': ObjectId(data)}
    update_query = { '$push': { 'Meta.Likes': email } }
    delete_query = {'$pull': { 'Meta.Likes': email }}


    like_list = Feed_collection.find_one(find_query)['Meta']['Likes']

    if len(like_list)==0 or email not in like_list:
        Feed_collection.update_one(find_query, update_query)
        return jsonify(len(like_list)+1)



    Feed_collection.update_one(find_query, delete_query)
    return jsonify(len(like_list)-1)
    