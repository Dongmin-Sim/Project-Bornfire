from flask import Blueprint, render_template, jsonify, request, redirect, session
from .models import  User_collection
from datetime import datetime

mypage = Blueprint("mypage", __name__)

@mypage.route("/my-page", methods=['GET'])
def get_myPage():
    
    if session.get('user_email') is not None:
        # user email
        user_email = session['user_email']
    
        col = User_collection
        
        # 세션의 email로 검색
        feed_log = col.find_one({"User_email": user_email}, {"User_feed_log":True, "_id":False})['User_feed_log']
        
        print(feed_log)
        print(type(feed_log))

        # TODO: 일일 피드 통계량
        
        today = datetime.today().strftime("%Y-%m-%d")
        print(today)
            # TODO: 지난 일주일 통계로 
        for log in feed_log:
            print(type(log))
            print(list(log.keys()))
            print(list(log.values()))

        # TODO: 월별 긍/부정 비율 그래프

        data = {
            'user_email': user_email, 
            # 'my_feed_log': my_feed_log,
            # 'predicted_value': predicted_value
        }
        
        return render_template('my-page.html', data=data)

    else:
        return redirect("/login-join")


# 비밀번호 변경
@mypage.route("/my-page", methods=['POST'])
def post_mypage():
    # TODO : 비밀번호 변경시
    return