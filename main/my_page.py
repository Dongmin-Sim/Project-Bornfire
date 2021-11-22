from flask import Blueprint, render_template, jsonify, request, redirect
import pymongo

mypage = Blueprint("mypage", __name__)

connection = pymongo.MongoClient("mongodb://localhost:27017/")

db = connection.get_database("Bornfire")

User_collection = db.get_collection("User_collection")

@mypage.route("/my-page")
def get_myPage():
    return render_template('my-page.html')


