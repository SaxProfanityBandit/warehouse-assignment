#Imports
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/products")
def get_products():
    pass

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