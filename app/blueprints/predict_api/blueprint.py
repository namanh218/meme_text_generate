from flask import Blueprint, render_template, request

predict_api = Blueprint('predict_api', __name__)
@predict_api.route('/route_name')
def route_name():
    return render_template('predict_api.html') 
