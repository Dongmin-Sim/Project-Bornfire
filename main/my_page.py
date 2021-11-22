from urllib.parse import uses_fragment
from flask import Blueprint, render_template, jsonify, request, redirect, session
import pymongo

mypage = Blueprint("mypage", __name__)

connection = pymongo.MongoClient("mongodb://localhost:27017/")

db = connection.get_database("Bornfire")


@mypage.route("/my-page", methods=['GET'])
def get_myPage():
    return render_template('my-page.html')

    if session['user_email']:
        # user email
        user_email = session['user_email']

        # 
        col = db.get_collection("User_collection")
        
        # 세션의 email로 검색
        my_account = col.find_one({"User_email": user_email})

        # myfeedlog를 일자별로 list 형태로 전달예정
        my_feed_log  = my_account[User_feed_log]

        # predicted_value 값 월별로 총합 전달
        predicted_value = my_account['predicted_value']

        data = {
            'user_email': user_email, 
            'my_feed_log': my_feed_log,
            'predicted_value': predicted_value
        }
        
        return render_template('my-page.html', data=data)

    else:
        return redirect("/login-join")


# 비밀번호 변경
@mypage.route("/my-page", methods=['POST'])
def post_mypage():
    return