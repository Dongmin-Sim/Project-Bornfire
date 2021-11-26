from typing import KeysView
from flask import Blueprint, render_template, jsonify, request, redirect
from .load_data import load_patient_data, load_sexAge_data, load_total_data, load_platform_data

statistics = Blueprint("statistics", __name__)

@statistics.route("/statistics")
def get_statistics():
    return render_template('statistics.html')


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


@statistics.route("/totalKeyword", methods=['GET'])
def totalKeyword():
    keyword = 'total_daily'
    # keyword = 'total_emotion'
    # keyword = 'total_mood'
    data = load_total_data(keyword)
    
    return jsonify(result=data)


@statistics.route("/platformKeyword", methods=['GET'])
def platformKeyword():
    btnValue = request.args.get('btnValue')
    label, data = load_platform_data(btnValue)
    
    return jsonify(result=[label, data])