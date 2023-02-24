from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homePage.html")

@app.route("/interests")
def interests():
    return render_template("interests.html")

@app.route("/Contact")
def contact():
    return render_template("Contact.html")

@app.route("/aboutme")
def Aboutme():
    return render_template("aboutme.html")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)