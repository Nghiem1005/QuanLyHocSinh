from flask import render_template, request, redirect
from my_app import app
import hashlib


@app.route("/")
def home():
    return render_template("TraCuu.html")





if __name__ == '__main__':
    app.run(debug=True)