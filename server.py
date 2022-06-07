from flask import Flask, jsonify, request, flash, render_template, redirect
from jinja2 import StrictUndefined
from random import randint
from model import connect_to_db, db
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


# Route to generate a random Disney avatar
@app.route("/random_disney")
def random_disney():
    """ Choose a random Disney character by calling Disney API"""

    avatar = request.args.get("random_disney")

    if avatar == "random_disney":
        char_id = randint(1, 7438)

    print("random id is", char_id)
    
    url = "https://api.disneyapi.dev/characters/" + str(char_id)
    
    response = requests.get(url)
    data = response.json()

    print(data)

    return render_template("random_disney.html", data=data)


# Route to generate a random Cat avatar
@app.route("/random_cat")
def random_cat():
    """ Randomly choose a cat image"""

    avatar = request.args.get("random_cat")

    if avatar == "random_cat":
        height = randint(300, 600)
        width = randint(300, 600)

    print("width and height is ", width, " x ", height)

    url = "http://placekitten.com/" + str(width) + "/" + str(height)

    return render_template("random_cat.html", data=url)


# Route to generate a random dog avatar
@app.route("/random_dog")
def random_dog():
    """ Randomly choose a dog image"""

    avatar = request.args.get("random_dog")

    if avatar == "random_dog":
        url = "https://dog.ceo/api/breeds/image/random"

    response = requests.get(url)
    data = response.json()

    return render_template("random_dog.html", data=data)


if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(debug=True)