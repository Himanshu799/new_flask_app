from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import requests
import configparser
from flask_cors import CORS
from email import message
from chat import get_response


# source xicor_env/bin/activate  


# from distutils.log import debug


app = Flask(__name__)
# CORS(app)

# @app.route("/baamt")

# @app.get("/")
def index_get():
    return render_template("index.html")

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    #TODO: check if text is valid
    
    response = get_response(text)
    message = {"answer":response}
    print(message)
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=False)
    # app.run(debug=False,host="0.0.0.0" ,port=6000)
    
