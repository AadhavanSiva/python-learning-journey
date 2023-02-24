from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thankYou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    last_pos = len(first) - 1
    result = 0
    if (first.isupper() == False) and (first.islower() == False) and (first[last_pos].isnumeric()) and (first.isnumeric() == False):
        result = "Passed"
    else:
        result = "Failed"
    return render_template('thankyou.html',first=first,last=last,result=result)

if __name__ == '__main__':
    app.run(debug=True)