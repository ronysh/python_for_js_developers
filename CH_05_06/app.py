import json
from decimal import Decimal

from flask import Flask, render_template, jsonify


app = Flask(__name__)

with open('laureate.json') as f:
    nobel_prize_laureates = json.load(f)["laureates"]


first_name_with_a = [laureate for laureate in nobel_prize_laureates if 'a' in laureate["firstname"].lower()]

@app.route("/")
def hello(name=None):
    return render_template("index.html")

@app.route("/items")
def items():
    return jsonify(first_name_with_a)

app.run(debug=True)


app.run(debug=True)
