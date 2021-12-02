from os import abort, error
from flask import Blueprint, render_template, jsonify, request, redirect,url_for, flash
from .user_validate import password_validate,email_validate
import pymongo
import bcrypt
from .mongo_connect import db


join = Blueprint("join", __name__)
collection = db.get_collection("User_collection")

@join.route("/join", methods=["POST"])
def post_join():
    # 숫자, 특수문자 1회이상, 영문은 2개이상 사용하여 8자리 이상 입력
        email = request.form.get("user_email")
        pw = request.form.get("user_pw")
        pw2 = request.form.get("user_pw2")
        question = request.form.get("user_question")
        answer = request.form.get("user_answer")
        answer = answer.replace(" ","")
        password_validate(pw,pw2)
        email_validate(email)
        if len(question) == 0 or len(answer) == 0:
            return redirect(url_for('login.get_login'))
            
        
        hashed_pw = bcrypt.hashpw(pw.encode('utf-8'),bcrypt.gensalt())
        hashed_pw=hashed_pw.decode('utf-8')
        
        try:
            collection.insert_one({"User_email":email, "User_pw":hashed_pw,"User_feed_log":[],"Verify_question": {question:answer}})
            flash('회원가입이 완료되었습니다 🔥')
            return redirect(url_for('login.get_login'))
        except pymongo.errors.DuplicateKeyError:
            flash('이미 존재하는 아이디 입니다. ')
            return redirect(url_for('login.get_login'))
            
        
