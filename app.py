from flask import Flask, render_template, request, abort, session, flash, redirect, send_from_directory, url_for
from base import app #db
#from models import User
#import models
#import KPIs
#import sys
#import json
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
def landing():
    return redirect("/index", code=302)

   
@app.route("/index")
def index():
#    read = Title.query.filter_by(read = False).all()

#    return render_template("index.html", read = read)
     return render_template("index.html")
    
@app.route("/3d-modeling")
def modeling():

     return render_template("3dmodeling.html")
 
@app.route("/interior-virtual-deco")
def blueprint():

     return render_template("interior.html")
 
@app.route("/exterior-virtual-deco")
def virtualdeco():

     return render_template("exterior.html")

@app.route("/matterport")
def matterport():

     return render_template("matterport.html")

@app.route("/matterport2")
def matterport2():

     return render_template("matterport2.html")

@app.route("/images/<image>.png")
def serve_image(image):
    return send_from_directory("images/", filename="{}.png".format(image))


if __name__ == '__main__':
    app.run(debug = True)