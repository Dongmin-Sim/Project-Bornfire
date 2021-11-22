from flask import Blueprint, render_template, jsonify, request, redirect,url_for
from . import user_validate
import pymongo
import bcrypt


connection = pymongo.MongoClient('mongodb://localhost:27017/')
db = connection.get_database("Bornfire")

join = Blueprint("join", __name__)

@join.route("/join", methods=["POST"])
def post_join():
    # 숫자, 특수문자 1회이상, 영문은 2개이상 사용하여 8자리 이상 입력
        email = request.form.get("user_email")
        pw = request.form.get("user_pw")
        pw2 = request.form.get("user_pw2")
        question = request.form.get("user_question")
        answer = request.form.get("user_answer")
        answer = answer.replace(" ","")
        user_validate.password_validate(pw,pw2)
        user_validate.email_validate(email)
        
        hashed_pw = bcrypt.hashpw(pw.encode('utf-8'),bcrypt.gensalt())
        hashed_pw=hashed_pw.decode('utf-8')
        collection = db.get_collection("User_collection")
        collection.insert_one({"User_email":email,"User_pw":hashed_pw,"User_emotion":[],"Verify_question": {question:answer}})
        return redirect(url_for('login.get_login'))
