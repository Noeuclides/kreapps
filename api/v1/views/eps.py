from api.v1.views import app_views
from api.v1.app import mysql


from flask import jsonify

@app_views.route('/eps')
def views_eps():
    """
    Return the current eps in a JSON file form
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM eps')
    eps = cur.fetchall()
    list_eps = []
    dict_eps = {}
    for el in eps:
        dict_eps.update({"id":el[0]})
        dict_eps.update({"name":el[1]})
        dict_eps.update({"phone":el[2]})
        dict_eps.update({"free_line":el[3]})
        list_eps.append(dict_eps)
        dict_eps = {}
    return jsonify(list_eps)


@app_views.route('/eps/<eps_id>')
def views_eps_id(eps_id=None):
    """
    Return the current eps in a JSON file form
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM eps where id= {}'.format(eps_id))
    eps = cur.fetchall()
    list_eps = []
    dict_eps = {}
    for el in eps:
        dict_eps.update({"id": el[0]})
        dict_eps.update({"name": el[1]})
        dict_eps.update({"phone": el[2]})
        dict_eps.update({"free_line": el[3]})
        list_eps.append(dict_eps)
        dict_eps = {}
    return jsonify(list_eps)
