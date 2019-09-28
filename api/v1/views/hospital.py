from api.v1.views import app_views
from api.v1.app import mysql


from flask import jsonify


@app_views.route('/hospitals')
def views_hospitals():
    """
    Return the current hospitals in a JSON file form
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM hospital')
    hospital = cur.fetchall()
    list_hospital = []
    dict_hospital = {}
    print(hospital)
    for el in hospital:
        dict_hospital.update({"id": el[0]})
        dict_hospital.update({"name": el[1]})
        dict_hospital.update({"latitude": el[2]})
        dict_hospital.update({"longitude": el[3]})
        dict_hospital.update({"address": el[4]})
        dict_hospital.update({"general_em": el[5]})
        dict_hospital.update({"odonto_em": el[6]})
        dict_hospital.update({"contact": el[7]})
        dict_hospital.update({"phone_number": el[8]})
        list_hospital.append(dict_hospital)
        dict_hospital = {}
    return jsonify(list_hospital)

@app_views.route('/hospitals/<hospital_id>')
def views_hospital(hospital_id=None):
    """
    Return the current hospitals in a JSON file form
    """
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM hospital WHERE id ={}'.format(hospital_id))
    hospital = cur.fetchall()
    list_hospital = []
    dict_hospital = {}
    for el in hospital:
        dict_hospital.update({"id": el[0]})
        dict_hospital.update({"name": el[1]})
        dict_hospital.update({"latitude": el[2]})
        dict_hospital.update({"longitude": el[3]})
        dict_hospital.update({"address": el[4]})
        dict_hospital.update({"general_em": el[5]})
        dict_hospital.update({"odonto_em": el[6]})
        dict_hospital.update({"contact": el[7]})
        dict_hospital.update({"phone_number": el[8]})
        list_hospital.append(dict_hospital)
        # dict_hospital = {}
    return jsonify(dict_hospital)
