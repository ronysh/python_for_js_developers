import json
from decimal import Decimal

from flask import Flask, render_template, jsonify


app = Flask(__name__)

data = [
    {"id": 1, "name": "olive oil", "price": 8.99},
    {"id": 2, "name": "flour", "price": 3.50},
    {"id": 3, "name": "salt", "price": 2.50},
    {"id": 4, "name": "yeast", "price": 1.50},
    {"id": 5, "name": "whole canned tomatoes", "price": 4.50},
]

@app.route('/')
def hello(name=None):
    return render_template('index.html')

@app.route('/items')
def items():
    return jsonify(data)

app.run(debug=True)
