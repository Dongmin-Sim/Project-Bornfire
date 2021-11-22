from flask import Blueprint, render_template, jsonify, request, redirect, session, url_for
from . import nickname
import pymongo
import re
import bcrypt

connection = pymongo.MongoClient('mongodb://localhost:27017/')
db = connection.get_database("Bornfire")

login = Blueprint("login", __name__)

@login.route("/login-join", methods=["GET","POST"])
def get_login():
    if request.method == "GET":
        return render_template('login-join.html')
    else:
        email = request.form.get("user_email")
        pw = request.form.get("user_pw")
        user = db.User_collection.find_one({"User_email":email})
        if bcrypt.checkpw(pw.encode('utf-8'),user["User_pw"].encode('utf-8')):
            session['nickname'] = nickname.make_nickname()
            session['user_email'] = email
            return redirect(url_for('intro.get_intro'))
        else:
            return redirect(url_for('login.get_login'))

@login.route("/logout")
def get_logout():
    session.pop('nickname',None)
    session.pop('user_email',None)
    return redirect(url_for('intro.get_intro'))

    


