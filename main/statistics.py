from typing import KeysView
from flask import Blueprint, render_template, jsonify, request, redirect
from .load_data import load_patient_data, load_sexAge_data, load_keyword_data, update_keyword_data

statistics = Blueprint("statistics", __name__)

@statistics.route("/statistics")
def get_statistics():
    return render_template('statistics.html')

@statistics.route("/statistics", methods=['POST'])
def get_test_sentiment():
    data = request.json
    context = data.get('context')
    print(context)
    
    from model.predict_sen import get_sentiment

    predicted = get_sentiment(context)
    positive = round(predicted[0], 2)
    negative = round(1 - positive, 2)
    
    print(positive, negative)

    return jsonify(result=[negative, positive])


@statistics.route("/patient", methods=['GET'])
def patient():
    btnValue = request.args.get('btnValue')
    label, data = load_patient_data(btnValue)
    
    return jsonify(result=[label, data])


@statistics.route("/sexAge", methods=['GET'])
def sexAge():
    btnValue = request.args.get('btnValue')
    label, data = load_sexAge_data(btnValue)
    
    return jsonify(result=[label, data])


@statistics.route("/keyword", methods=['GET'])
def initialKeyword():
    btnValue = request.args.get('btnValue')
    data = load_keyword_data(btnValue)
    
    return jsonify(result=data)


@statistics.route("/keyword", methods=['GET'])
def updateKeyword():
    btnValue = request.args.get('btnValue')
    label, data = update_keyword_data(btnValue)
    
    
    return jsonify(result=[label, data])
