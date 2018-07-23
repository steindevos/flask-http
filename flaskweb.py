from flask import Flask, request, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def show_hi():
    return render_template("index.html")
    
@app.route("/photos")
def show_photos():
    return render_template("photos.html")

@app.route("/about")
def show_about():
    return render_template("about.html")
    
@app.route("/contact")
def show_contact():
    return render_template("contact.html")
    
@app.route("/searchpost", methods=["POST"])
def do_search_post():
    make = request.form["make"]
    model = request.form["model"]
    year = request.form["year"]
    return "hey you searched for a {0} {1} of the year {2}".format(make, model, year)
    #get (search gets encoded in URL(so watch out with sensitive info)
    #post (does not encode in URL)

@app.route("/searchget")
def do_search_get():
    make = request.args["make"]
    model = request.args["model"]
    year = request.args["year"]
    return "hey you searched for a {0} {1} of the year {2}".format(make, model, year)

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=True)