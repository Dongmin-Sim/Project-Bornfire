from flask import Blueprint, render_template, jsonify, request, redirect, session, url_for
import functools
from .models import  User_collection
from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import defaultdict
import bcrypt

mypage = Blueprint("mypage", __name__)

def login_required(func):
    @functools.wraps(func)
    def wrapped_view(**kwargs):
        user = session.get('user_email')
        if user is None:
            return redirect(url_for('index'))
        return func(**kwargs)
    return wrapped_view


col = User_collection

@mypage.route("/my-page", methods=['GET'])
@login_required
def get_myPage():
    global col
    if session.get('user_email') is not None:
        # user
        user_email = session['user_email']
        
        # 유저의 feed_log 불러오기
        feed_log = col.find_one({"User_email": user_email}, {"User_feed_log":True, "_id":False})['User_feed_log']
        
        # 피드 작성 최신 순으로 
        feed_log.reverse()

        # TODO: 일일 피드 통계량
        days = []
        daily_feed = defaultdict(int)
        now = datetime.today()
        today = datetime(now.year, now.month, now.day)

        for i in range(0, 8):
            new_date = today + relativedelta(days=-i)
            new_date = str(new_date.date())

            daily_feed[new_date] = 0
            days.append(new_date)
        
        daily_feed = dict(sorted(daily_feed.items()))

        for log in feed_log:
            key = list(log.keys())[0]
            feed_date = key[:10]

            if feed_date not in days:
                break
            daily_feed[feed_date] += 1


        # TODO: 월별 긍/부정 비율 그래프
        predicted_value = defaultdict(int)
        month = str(today.month)
        
        for log in feed_log:
            key = list(log.keys())[0]
            value = list(log.values())[0]
            feed_month = key[5:7]

            if feed_month != month:
                break
            predicted_value[value] += 1
        
        # temp = dict({'a':5, 'b':1})
        # print(type(temp))
        # print((list(temp.values())))
        # return data
        data = {
            'user_email': user_email, 
            'my_feed_log': [list(daily_feed.keys()), list(daily_feed.values())],
            'predicted_value': predicted_value
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
    
    # 세션의 email로 검색
    user_email = session['user_email']
    user_pw = col.find_one({"User_email": user_email})['User_pw']
    
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