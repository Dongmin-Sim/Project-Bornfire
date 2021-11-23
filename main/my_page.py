from flask import Blueprint, render_template, jsonify, request, redirect
import pymongo
from .mongo_connect import db


mypage = Blueprint("mypage", __name__)


User_collection = db.get_collection("User_collection")

@mypage.route("/my-page")
def get_myPage():
    return render_template('my-page.html')


