from flask import Blueprint, render_template, jsonify, request, redirect

intro = Blueprint("intro", __name__)

@intro.route("/")
def get_intro():
    return render_template('intro.html')
