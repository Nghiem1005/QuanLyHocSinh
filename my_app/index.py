from flask import render_template, request, redirect
from my_app import app, my_login
from my_app.admin import *
from my_app.models import User
from flask_login import login_user
import hashlib


@app.route("/")
def home():
    return render_template("home.html")





if __name__ == '__main__':
    app.run(debug=True)