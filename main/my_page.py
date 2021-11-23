import re
from flask import Blueprint, render_template, jsonify, request, redirect, session, json, url_for
from flask.helpers import flash
from .models import  User_collection
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict
import pprint
import bcrypt
mypage = Blueprint("mypage", __name__)


col = User_collection

@mypage.route("/my-page", methods=['GET'])
def get_myPage():
    global col
    if session.get('user_email') is not None:
        # user
        user_email = session['user_email']
        
        # 세션의 email로 검색
        feed_log = col.find_one({"User_email": user_email}, {"User_feed_log":True, "_id":False})['User_feed_log']
        feed_log.reverse()



        # TODO: 일일 피드 통계량
        days = []
        result = defaultdict(int)
        now = datetime.today()
        today = datetime(now.year, now.month, now.day)

        for i in range(0, 8):
            new_date = today + relativedelta(days=-i)
            result[str(new_date.date())] = 0
            days.append(str(new_date.date()))

        for log in feed_log:
            key = list(log.keys())[0]
            feed_date_log = key[:10]

            if feed_date_log not in days:
                break
            result[feed_date_log] += 1


        # TODO: 월별 긍/부정 비율 그래프
        

        
        # return data
        data = {
            'user_email': user_email, 
            'my_feed_log': [list(result.keys()), list(result.values())],
            # 'predicted_value': predicted_value
        }
        
        return render_template('my-page.html', data=data)

    else:
        return redirect("/login-join")


# 비밀번호 변경
@mypage.route("/my-page", methods=['POST'])
def change_pw():
    # TODO : 비밀번호 변경시
    global col
    data = request.json
    origin_pw = data['origin_pw']
    new_pw = data['new_pw']
    
    # origin_pw = request.form.get("origin_pw")
    # new_pw = request.form.get("new_pw")
    print('입력값 : ', origin_pw, new_pw)
    # 세션의 email로 검색
    user_email = session['user_email']
    user_pw = col.find_one({"User_email": user_email})['User_pw']
    print('기존값 : ', user_email, user_pw)
    # 기존 비밀번호와 일치하는지 검사 
    if bcrypt.checkpw(origin_pw.encode('utf-8'), user_pw.encode('utf-8')):
        # 새로운 비밀번호 hash
        hashed_pw = bcrypt.hashpw(new_pw.encode('utf-8'),bcrypt.gensalt())
        hashed_pw = hashed_pw.decode('utf-8')
        # 비밀번호 업데이트
        col.update_one(
            {'User_email':user_email},
            { '$set': {"User_pw":hashed_pw}}
        )
        return jsonify({'result':'ok'})
    
        
    return jsonify({'result':'failed'})