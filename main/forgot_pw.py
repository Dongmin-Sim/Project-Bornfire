from flask import Blueprint, render_template, jsonify, request, redirect, url_for
import bcrypt
import re
from .models import User_collection as collection


forgot_pw = Blueprint("forgot_pw", __name__)

@forgot_pw.route("/forgot-pw", methods=["GET","POST"])
def forgot():
    if request.method=="GET":
        return render_template('forgot-pw.html')
    else:
        email = request.json
        global query
        query = {"User_email":email['User_email']}
        user = collection.find_one(query)
        # 에러 발생시 -> 아이디를 확인해주세요 넣어야함!
        # 에러가 발생하지 않았을 때 모달을 띄움
        # 모달안에는 질문, 답을 위한 input -> 정답이라면 비밀번호 변경
        return jsonify(user["Verify_question"])

@forgot_pw.route("/change-pw", methods=["POST"])
def change():
    pw = request.form.get("new_pw")
    pw2 = request.form.get("new_pw2")
    validation_pw = re.compile('(?=.*\d{1,50})(?=.*[~`!@#$%\^&*()-+=]{1,50})(?=.*[a-zA-Z]{2,50}).{8,50}$') 

    if validation_pw.match(pw) != None:
        pass
    else:
        return redirect(url_for('forgot_pw.forgot'))
            

    if pw != pw2:
        return redirect(url_for('forgot_pw.forgot'))
    
    if pw == pw2:
        hashed_pw = bcrypt.hashpw(pw.encode('utf-8'),bcrypt.gensalt())
        hashed_pw=hashed_pw.decode('utf-8')
        collection.update_one(query, {"$set" : {"User_pw": hashed_pw}})
        return redirect(url_for('login.get_login'))
        

    

        

