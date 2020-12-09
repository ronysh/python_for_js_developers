import json
from decimal import Decimal

from flask import Flask, render_template, jsonify


app = Flask(__name__)

with open("laureate.json") as f:
    nobel_prize_laureates = json.load(f)["laureates"]


@app.route("/")
def hello(name=None):
    return render_template("index.html")


@app.route("/items")
def items():
    return jsonify(nobel_prize_laureates)  # hint "Aa".lower() == "aa"


app.run(debug=True)
