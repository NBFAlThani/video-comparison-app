from flask import Flask, render_template, request,send_from_directory, jsonify, url_for
from flask import redirect

# from scripts import helper
import requests


import json

import time
import os
# import pickle

application = Flask(__name__)

@application.route('/')
def home():    
    # return "hello"
    return render_template("index.html")



@application.route('/submit',methods=['GET','POST'])
def submit():    
    # return "hello"
    print(request.form.keys())
    first_name=request.form["fname"]
    last_name=request.form["lname"]
    print("values are",first_name,last_name)

    # get the videos
    # vid1=request.files["video1"]
    # vid2=request.files["video2"]





    # return "received files"
    return first_name+" "+last_name





if __name__ == "__main__":
    
    application.run(debug=True,port=8111)