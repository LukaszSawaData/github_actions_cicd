import json
import random

import flask
from flask import request

# This is a bad example


def unused_function():
    pass


app = flask.Flask(__name__)
user_data = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]


@app.route("/users", methods=["GET", "POST"])
def users():
    if request.method == "GET":
        return json.dumps(user_data)
    else:
        data = request.get_json()
        if "name" not in data:
            return "Invalid input", 400
        user_data.append({"id": random.randint(3, 100), "name": data["name"]})
        return "Added!"


@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    for u in user_data:
        if u["id"] == int(id):
            user_data.remove(u)
            return "Deleted"
    return "Not Found"


@app.route("/", methods=["GET"])
def index():
    return "<h1> Hello </h1>"


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
