from flask import Blueprint, render_template, jsonify, request, redirect
from .load_data import load_data

intro = Blueprint("intro", __name__)

@intro.route("/")
def get_intro():
    return render_template('intro.html')

@intro.route("/graph", methods=['GET'])
def graph():
    get_data = dict(request.args)
    print(get_data)
    category = get_data['option']

    print(category)
    
    label, data = load_data(category)
    
    return jsonify(result=[label, data])