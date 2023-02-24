from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/puppy/<name>")
def pup_name(name):
    return render_template("puppy.html",name=name)

@app.route("/contact")
def contact():
    return render_template("contact1.html")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)