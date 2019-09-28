from api.v1.views import app_views
from flask import jsonify

@app_views.route('/eps')
def views_eps():
    """
    Return the current eps in a JSON file form
    """
    return jsonify({"Greet": "HOLA"})