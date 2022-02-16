#Imports
from flask import Flask, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'warehouse_admin'
app.config['MYSQL_PASSWORD'] = 'devops'
app.config['MYSQL_DB'] = 'warehouse'

mysql = MySQL(app)


@app.route("/")
def hello_world():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM products;")
    mysql.connection.commit()
    row = cur.fetchall()
    desc = list(zip(*cur.description))[0]
    rowdict = dict(zip(str(row[0]), desc))
    jsondict = jsonify(rowdict)
    cur.close()
    output = ""
    #for x in rows[1]:
        #output = output + str(x)
    return jsondict

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