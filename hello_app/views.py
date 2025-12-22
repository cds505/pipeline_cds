from datetime import datetime
from flask import Flask, redirect, url_for,render_template
from . import app

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")


#To test this function, On the Website you can simply add /url_for/
#To the end of the URL
@app.route("/url_for/")
def url_for_test_page():
    return redirect(url_for('contact'))
#This will redirect the /url_for/ link to the contact page.


@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")
