#Imports
from lib2to3.pytree import convert
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import json
import mysql.connector
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'warehouse_admin'
app.config['MYSQL_PASSWORD'] = 'devops'
app.config['MYSQL_DB'] = 'warehouse'


#mysql = MySQL(app)

db = mysql.connector.connect(
    host='127.0.0.1',
    user='warehouse_admin',
    passwd='devops',
    db='warehouse',
)
app.config['JSON_AS_ASCII'] = False



@app.route("/")
def hello_world():
    #cur = mysql.connection.cursor(dictionary=True)
    #cur.execute("SELECT * FROM products;")
    #mysql.connection.commit()
    #row = cur.fetchall()
    #json_data = convert_to_json(row, 2)
    #cur.close()
    #print(type(json_data))

    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM products;')
    result = cursor.fetchall()

    #return f"json: {json.dumps(result)}"
    #return result[0]
    return convert_to_json(result[0])



    #return json_data

def convert_to_json(dict):
    for key in dict:
        if type(dict[key]) is datetime:
            dict[key] = str(dict[key])
    data = f"json: {json.dumps(dict, ensure_ascii=False)}"
    return data

@app.route("/products")
def get_products():
    return "We got plenty of products here!"

app.route("/products")
def post_products():
    pass

app.route("/products/1")
def get_product_1():
    pass

app.route("/products/1")
def put_products():
    pass



if __name__ == '__main__':
    app.run(debug = True)