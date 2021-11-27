from flask import Blueprint, render_template, jsonify, request, redirect

content_service = Blueprint("content_service", __name__)

@content_service.route("/content_service")
def get_content_service():
    return render_template('content-service.html')
