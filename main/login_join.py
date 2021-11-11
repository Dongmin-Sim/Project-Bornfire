from flask import Blueprint, render_template, jsonify, request, redirect

login_join = Blueprint("login_join", __name__)

@login_join.route("/login-join")
def get_login_join():
    return render_template('login-join.html')
