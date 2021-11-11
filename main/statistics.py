from flask import Blueprint, render_template, jsonify, request, redirect

statistics = Blueprint("statistics", __name__)

@statistics.route("/statistics")
def get_statistics():
    return render_template('statistics.html')
