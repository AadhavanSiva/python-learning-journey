# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask

app = Flask(__name__)

@app.route('/puppy')
def index():
    return "<h1>Hello puppy</h1>"
@app.route("/information")
def info():
    return "<h1>puppies are cute "

@app.route("/puppyLatin/<name>")
def puppyLatin(name):
    return latinName(name)

def latinName(name):
    result = False

    last_pos = len(name) - 1
    if name[last_pos].lower() != "y":
        result = "{}y".format(name)
    else:
        result = "{}iful".format(name[0:last_pos])
    return result


@app.route("/puppy/<name>")
def puppy(name):
    return "100th letter {} ".format(name[100])

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

