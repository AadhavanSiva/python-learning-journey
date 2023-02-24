from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    my_var = "Jose"
    letters = list("jose")
    pup_dictionary = ['Fluffy','Sammy']
    return render_template('basic.html',my_var=my_var,letters=letters,pup_dictionary=pup_dictionary)

@app.route("/about")
def about():
    return render_template('about.html')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)