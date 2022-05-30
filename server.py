from flask import Flask, jsonify, request, flash, render_template, redirect
from jinja2 import StrictUndefined
from random import randint
import requests
import os

# Flask app config
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """ Show homepage """

    return render_template("index.html")


@app.route("/random_disney")
def random_disney():
    """ Choose a random Disney character and display its image"""

    type = request.args.get("disney")

    if type == "random":
        char_id = randint(1, 7438)

    print("random id is", char_id)
    
    url = "https://api.disneyapi.dev/characters/" + str(char_id)
    

    response = requests.get(url)
    data = response.json()

    print(data)

    return render_template("random_disney.html", data=data)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    
    app.run(debug=True)