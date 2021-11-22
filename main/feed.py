from flask import Blueprint, render_template, jsonify, request, redirect
import datetime
from bson import ObjectId
from pymongo import cursor

from .models import Feed_collection, User_collection

feed = Blueprint("feed", __name__)



@feed.route("/feed")
def get_feed():
    # 이값을 받으면 될 듯. 
    # cursor = request.args.get('cursor')
    cur= 0
    #TODO [무한 스크롤] 디비 갯수 확인 필요 할 듯. 
    cols = Feed_collection.find().sort('_id',-1).skip(10*cur).limit(10)

    col_list = []
    for col in cols:
        col_list.append({
            '_id' : col["_id"],
            # TODO 생성 필요
            'nickname': "개구리상",
            'context' : col['Feed'],
            'thumbs-up': len(col['Meta']['Likes'])
        })

# TODO subject collection 넘겨 주는 것 필요.
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
    emotion = 1
    data = {
        'Main_subject_num' : 1,
        'Side_subject_num': 1,
        'Feed' : context,
        "Meta": {'Likes': [], "Created_at": datetime.datetime.utcnow()},
        'Predicted_value' : emotion
    }
    # Feed_collection.remove({})
    Feed_collection.insert_one(data)

    cols = Feed_collection.find().sort('_id',-1).limit(1)
    #TODO [DB 정보 확인]DB에서 error가 났을 때,  예외 처리 필요. 
    col_list = []
    for col in cols:
        col_list.append({
            '_id' : str(col["_id"]),
            #TODO 이거 함수 그냥 돌려서 
            'nickname': "개구리 상",
            'context' : col['Feed'],
            'thumbs-up': len(col['Meta']['Likes'])
        })

    return (jsonify(col_list))

@feed.route('/thumbs', methods=["UPDATE"])
def thumbs_up():
    data = request.json

    # #update thumbs-up
    # find_query = {'_id': ObjectId(data)}
    # update = {'$inc': {'Meta.thumps-up': 1}}
    # Feed_collection.update_one(find_query, update)

    # #for parse thumbs-up data
    # cols = Feed_collection.find_one(find_query)
    # dict_cols = dict(cols)

    return(jsonify("3"))