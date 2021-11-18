from flask import Blueprint, render_template, jsonify, request, redirect,url_for
import pymongo
import re
import bcrypt

connection = pymongo.MongoClient('mongodb://localhost:27017/')
db = connection.get_database("Bornfire")

join = Blueprint("join", __name__)

@join.route("/join", methods=["POST"])
def post_join():
    # 숫자, 특수문자 1회이상, 영문은 2개이상 사용하여 8자리 이상 입력
        validation_pw = re.compile('(?=.*\d{1,50})(?=.*[~`!@#$%\^&*()-+=]{1,50})(?=.*[a-zA-Z]{2,50}).{8,50}$') 
        validation_email = re.compile('^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
        email = request.form.get("user_email")
        pw = request.form.get("user_pw")
        pw2 = request.form.get("user_pw2")
        if pw != pw2:
            print("비밀번호가 일치 하지 않습니다.")
        if validation_email.match(email) != None:
            pass
        else:
            print("이메일 정규식 에러")
        if validation_pw.match(pw) != None:
            pass
        else:
            print("비밀번호 정규식 에러")

        hashed_pw = bcrypt.hashpw(pw.encode('utf-8'),bcrypt.gensalt())
        hashed_pw=hashed_pw.decode('utf-8')
        collection = db.get_collection("User_collection")
        collection.insert_one({"User_email":email,"User_pw":hashed_pw,"User_emotion":[]})
        return redirect(url_for('login.get_login'))
