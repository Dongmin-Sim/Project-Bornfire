from flask import Blueprint, render_template, jsonify, request, redirect
from .load_data import load_patient_data, load_sexAge_data

intro = Blueprint("intro", __name__)

@intro.route("/")
def get_intro():
    return render_template('intro.html')

@intro.route("/patient", methods=['GET'])
def patient():
    btnValue = request.args.get('btnValue')
    label, data = load_patient_data(btnValue)
    
    return jsonify(result=[label, data])


@intro.route("/sexAge", methods=['GET'])
def sexAge():
    btnValue = request.args.get('btnValue')
    label, data = load_sexAge_data(btnValue)
    
    return jsonify(result=[label, data])