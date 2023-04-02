import os
from forms import AddForm, DelForm
from flask import Flask,render_template,url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
public_key = "pk_test_6pRNASCoBOKtIshFeQd4XMUh"

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MOODIFICATION'] = False
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
app.app_context().push()

Migrate(app,db)

class Puppy(db.Model):
    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.Text)
    # owner = db.relationship('Owner', backref='puppy',uselist=False)

    def __init__(self,name,age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy details: {self.name} {self.age}"

# class Owner(db.Model):
#     __tablename__ = "owners"
#     id = db.Column(db.Integer,primary_key=True)
#     name = db.Column(db.Text)
#     puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))
#
#     def __init__(self,name,puppy_id):
#         self.name = name
#         self.puppy_id = puppy_id
#     def __repr__(self):
#         if self.owner:
#             return f"Puppy name is {self.name} and owner is {self.owner.name}"
#         else:
#             return f"Puppy name: {self.name} and no owner assigned yet!"



@app.route('/')
def index():
    return list_pup()

@app.route('/puppyco')
def puppyco():
    return render_template('puppyco.html')

@app.route('/add',methods=['GET','POST'])
def add_pup():
    form = AddForm()
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        breed = form.breed.data
        new_pup = Puppy(name,age,breed)
        db.session.add(new_pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('add.html', form=form)

@app.route('/dontate')
def donate():
    return render_template('donate.html',public_key=public_key)

@app.route('/payment',methods=['POST'])
def payment():
    customer = stripe.Customer.create(email=request.form['stripeEmail'],
                                      source=request.form['stripeToken'])
    charge = stripe.Charge.create(
        customer=customer.id,
        amount=1,
        currency='usd',
        description='Donation')
    return redirect(url_for('payment'))

@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()

    return render_template('list.html',puppies=puppies)


@app.route('/delete_pup/<id>/', methods=['GET','POST'])
def delete_pup(id):
    pup = Puppy.query.get(id)
    db.session.delete(pup)
    db.session.commit()

    return redirect(url_for('list_pup'))

#@app.route('/edit_pup/<id>/')
#def edit_pup(id):



@app.route('/delete/<id>/', methods=['GET','POST'])
def del_pup(id):
    form = DelForm()
    if form.validate_on_submit():
        del_id = form.id.data
        pup = Puppy.query.get(del_id)
        db.session.delete(pup)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form, id=id)

if __name__ == '__main__':
    app.run(debug=True)


