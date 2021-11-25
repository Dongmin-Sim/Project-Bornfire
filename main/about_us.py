from flask import Blueprint, render_template, jsonify, request, redirect

about_us = Blueprint("about_us", __name__)

@about_us.route("/about-us")
def get_about_as():
    return render_template('about-us.html')
