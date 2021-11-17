from flask import Blueprint, render_template, jsonify, request, redirect

mypage = Blueprint("mypage", __name__)

@mypage.route("/my-info")
def get_myPage():
    return render_template('my-emotion.html')
