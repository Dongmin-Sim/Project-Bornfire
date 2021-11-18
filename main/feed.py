from flask import Blueprint, render_template, jsonify, request, redirect

feed = Blueprint("feed", __name__)

@feed.route("/feed")
def get_feed():
    return render_template('feed.html')

@feed.route('/feed', methods=['POST'])
def post_feed():
    data = request.json
    print(data)
    return (jsonify("ok"))