import os
from flask import flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello There!</h1>"

app.run(host=os.getnev('IP'), port=int(os.getnev('PORT')), debu=True)