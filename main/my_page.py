from flask import Blueprint, render_template, jsonify, request, redirect

mypage = Blueprint("mypage", __name__)

@mypage.route("/my-info")
def get_myPage():
    return render_template('my-page.html')

@mypage.route("/my-emotion")
def get_emotion():
    return render_template('my-emotion.html', date = '8월')

@mypage.route("/my-account")
def get_acount():
    return render_template('my-account.html')

@mypage.route("/my-feed")
def get_feed():
    return render_template('my-emotion.html')