from flask import Flask, jsonify

from db_connection import *

app = Flask(__name__)


@app.route('/')
def hello():
    return "welcome"


@app.route('/get_locations', methods=['GET'])
def getLocation():
    # connecting to local db connection defined in config file
    db = get_db_conection()
    cursor = db.cursor()

    # fetching distinct states from table
    sql = "select distinct state from location"
    cursor.execute(sql)
    records = cursor.fetchall()

    response = {}
    data = []
    # for each state in records tuple
    for each in records:
        keyjson = {}
        keyjson['state'] = each[0]

        # fetching list of districts
        subsql = "select id,district,pincode from location where state='" + each[0] + "';"
        cursor.execute(subsql)
        subrecords = cursor.fetchall()

        district_list = []
        # Creating list of districts dictionary
        for district in subrecords:
            each_dictrict = {}
            each_dictrict['id'] = district[0]
            each_dictrict['name'] = district[1]
            each_dictrict['pincode'] = district[2]
            district_list.append(each_dictrict)

        # appending list of districts to json
        keyjson['districts'] = district_list
        data.append(keyjson)
        response['data'] = data

    return jsonify(response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
