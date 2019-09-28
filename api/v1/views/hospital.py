from api.v1.views import app_views
from api.v1.app import mysql


from flask import jsonify


@app_views.route('/hospital')
def views_hospital():
    """
    Return the current hospitals in a JSON file form
    """
    return jsonify({"greet":"Hello"})
