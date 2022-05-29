from flask import Flask, jsonify, request, flash, render_template, redirect
import os

# Flask app config
app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.jinja_env.undefined = StrictUndefined





if __name__ == "__main__":
    # DebugToolbarExtension(app)
    
    app.run()