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
    return "Welcome to the index of this warehouse.\n"

@app.route("/products", methods=['GET', 'POST'])
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
            return make_response("Added new product.\n", 201)

    return make_response("Wrong type of request.\n", 400)


@app.route("/products/<int:_id>", methods=['GET', 'DELETE', 'PUT'])
def product(_id):
    if request.method == 'GET':
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM products WHERE Id={};'.format(_id))
        result = cursor.fetchall()
        return make_response(jsonify(result), 200)
    elif request.method == 'DELETE':
        cursor = db.cursor(dictionary=True)
        cursor.execute('DELETE FROM products WHERE Id={};'.format(_id))
        db.commit()
        return make_response("Product with ID {} deleted.\n".format(_id), 200)
    elif request.method == 'PUT':
        cursor = db.cursor(dictionary=True)
        json_data = request.json
        cursor.execute('UPDATE products SET price={}, amount={} WHERE Id={};'.format(json_data['price'], json_data['amount'], _id))
        db.commit()
        return make_response("Product with ID {} updated.\n".format(_id), 200)

@app.route("/customers", methods=['GET', 'POST'])
def get_customers():
    if request.method == 'GET':
        return make_response(get_json("customers"), 200)
    elif request.method == 'POST':
        json_data = request.json
        if json_data is not None:
            cursor = db.cursor(dictionary=True)
            query = (
                "INSERT INTO customers (first_name, last_name, street, postal_code, age) "
                "VALUES (%s, %s, %s, %s, %s);"
            )
            data = (json_data['first_name'], json_data['last_name'], json_data['street'], json_data['postal_code'], json_data['age'])
            cursor.execute(query, data)
            db.commit()
            if cursor is not None:
                result = cursor.fetchone()
                print(result)
            return make_response("Added new customer.\n", 201)

    return make_response("Wrong type of request.\n", 400)

@app.route("/customers/<int:_id>", methods=['GET', 'DELETE', 'PUT'])
def customer(_id):
    if request.method == 'GET':
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM customers WHERE Id={};'.format(_id))
        result = cursor.fetchall()
        return make_response(jsonify(result), 200)
    elif request.method == 'DELETE':
        cursor = db.cursor(dictionary=True)
        cursor.execute('DELETE FROM customers WHERE Id={};'.format(_id))
        db.commit()
        return make_response("Customer with ID {} deleted.\n".format(_id), 200)
    elif request.method == 'PUT':
        cursor = db.cursor(dictionary=True)
        json_data = request.json
        cursor.execute('UPDATE customers SET age={} WHERE Id={};'.format(json_data['age'], _id))
        db.commit()
        return make_response("Customer with ID {} updated.\n".format(_id), 200)

@app.route("/staff", methods=['GET', 'POST'])
def get_staff():
    if request.method == 'GET':
        return make_response(get_json("staff"), 200)
    elif request.method == 'POST':
        json_data = request.json
        if json_data is not None:
            cursor = db.cursor(dictionary=True)
            query = (
                "INSERT INTO staff (first_name, last_name, employee_since, age) "
                "VALUES (%s, %s, %s, %s);"
            )
            data = (json_data['first_name'], json_data['last_name'], json_data['employee_since'], json_data['age'])
            cursor.execute(query, data)
            db.commit()
            if cursor is not None:
                result = cursor.fetchone()
                print(result)
            return make_response("Added new staff.\n", 201)

    return make_response("Wrong type of request.\n", 400)

@app.route("/staff/<int:_id>", methods=['GET', 'DELETE', 'PUT'])
def staff(_id):
    if request.method == 'GET':
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM staff WHERE Id={};'.format(_id))
        result = cursor.fetchall()
        return make_response(jsonify(result), 200)
    elif request.method == 'DELETE':
        cursor = db.cursor(dictionary=True)
        cursor.execute('DELETE FROM staff WHERE Id={};'.format(_id))
        db.commit()
        return make_response("Staff with ID {} deleted.\n".format(_id), 200)
    elif request.method == 'PUT':
        cursor = db.cursor(dictionary=True)
        json_data = request.json
        cursor.execute('UPDATE staff SET last_name="{}" WHERE Id={};'.format(json_data['last_name'], _id))
        db.commit()
        return make_response("Staff with ID {} updated. \n".format(_id), 200)

@app.route("/orders", methods=['GET', 'POST'])
def get_orders():
    if request.method == 'GET':
        return make_response(get_json("orders"), 200)
    elif request.method == 'POST':
        json_data = request.json
        if json_data is not None:
            cursor = db.cursor(dictionary=True)
            query = (
                "INSERT INTO orders (product_id, customer_id, staff_id) "
                "VALUES (%s, %s, %s);"
            )
            data = (json_data['product_id'], json_data['customer_id'], json_data['staff_id'])
            cursor.execute(query, data)
            db.commit()
            if cursor is not None:
                result = cursor.fetchone()
                print(result)
            return make_response("Added new order.\n", 201)

    return make_response("Wrong type of request.\n", 400)

@app.route("/orders/<int:_id>", methods=['GET', 'DELETE', 'PUT'])
def order(_id):
    if request.method == 'GET':
        cursor = db.cursor(dictionary=True)
        cursor.execute('SELECT * FROM orders WHERE product_id={};'.format(_id))
        result = cursor.fetchall()
        return make_response(jsonify(result), 200)
    elif request.method == 'DELETE':
        cursor = db.cursor(dictionary=True)
        cursor.execute('DELETE FROM orders WHERE Id={};'.format(_id))
        db.commit()
        return make_response("Order with ID {} deleted.\n".format(_id), 200)
    elif request.method == 'PUT':
        cursor = db.cursor(dictionary=True)
        json_data = request.json
        cursor.execute('UPDATE orders SET last_name="{}" WHERE Id={};'.format(json_data['last_name'], _id))
        db.commit()
        return make_response("Order with ID {} updated. \n".format(_id), 200)

def get_json(table):
    cursor = db.cursor(dictionary=True)
    cursor.execute('SELECT * FROM {};'.format(table))
    result = cursor.fetchall()
    return jsonify(result)




if __name__ == '__main__':
    app.run(debug = True)