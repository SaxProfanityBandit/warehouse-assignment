#Imports
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'warehouse_admin'
app.config['MYSQL_PASSWORD'] = 'devops'
app.config['MYSQL_DB'] = 'warehouse'
app.config['JSON_AS_ASCII'] = False

mysql = MySQL(app)


@app.route("/")
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products;")
    mysql.connection.commit()
    row = cur.fetchone()
    json_data = jsonify([x for x in row])
    cur.close()
    output = ""
    return json_data

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