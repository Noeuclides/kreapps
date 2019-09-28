#!/usr/bin/python3
""" app file
"""
from flask import Flask
from api.v1.views import app_views
from flask import jsonify
import os
from flask_mysqldb import MySQL
from flask_cors import CORS

# configuration mysql connection
# this always up before to create object
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'ieps'
#connection to DB
mysql = MySQL(app)

# settings sessions
app.secret_key = 'mysecretkey'

cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

h = os.environ.get("HBNB_API_HOST", "localhost")
p = os.environ.get("HBNB_API_PORT", "5000")



@app.errorhandler(404)
def _handle_api_error(ex):
    """
    errorhandler funtion
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    app.run(host=str(h), port=int(p), debug=True)
