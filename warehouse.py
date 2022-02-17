#Imports
from flask import Flask, jsonify, make_response
import mysql.connector
#from datetime import datetime
from flask import request

app = Flask(__name__)

#app.config['MYSQL_HOST'] = '127.0.0.1'
#app.config['MYSQL_USER'] = 'warehouse_admin'
#app.config['MYSQL_PASSWORD'] = 'devops'
#app.config['MYSQL_DB'] = 'warehouse'


#mysql = MySQL(app)

db = mysql.connector.connect(
    host='127.0.0.1',
    user='warehouse_admin',
    passwd='devops',
    db='warehouse',
)
app.config['JSON_AS_ASCII'] = False



@app.route("/")
def show_index():
    return "Welcome to the index of this warehouse."

@app.route("/products/", methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return make_response(get_json("products"), 200)
    elif request.method == 'POST':
        json_data = request.json
        if json_data is not None:
            cursor = db.cursor(dictionary=True)
            query = (
                "INSERT INTO products (name, price, amount) "
                "VALUES (%s, %s, %s);"
            )
            data = (json_data['name'], json_data['price'], json_data['amount'])
            cursor.execute(query, data)
            db.commit()
            if cursor is not None:
                result = cursor.fetchone()
                print(result)
            return make_response("Test", 201)

    return make_response("Wrong type of request.", 400)


@app.route("/products/<int:_id>", methods=['GET', 'DELETE'])
def get_product(_id):
    if request.method == 'GET':
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM products WHERE Id={};'.format(_id))
        result = cursor.fetchall()
        return make_response(jsonify(result), 200)
    elif request.method == 'DELETE':
        cursor = db.cursor(dictionary=True)
        cursor.execute('DELETE FROM products WHERE Id={};'.format(_id))
        return make_response("Product with ID {} deleted.".format(_id), 200)

@app.route("/customers", methods=['GET'])
def get_customers():
    return get_json("customers")

@app.route("/staff", methods=['GET'])
def get_staff():
    return get_json("staff")

@app.route("/orders", methods=['GET'])
def get_orders():
    return get_json("orders")

def get_json(table):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM {};'.format(table))
    result = cursor.fetchall()
    return jsonify(result)

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