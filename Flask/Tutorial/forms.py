from flask import Flask, render_template,session,redirect,url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields import BooleanField

from wtforms.fields import SelectField,RadioField
from wtforms.fields import SubmitField
from wtforms.fields import TextAreaField

from wtforms.fields import StringField

from wtforms.fields import DateTimeField
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mk'

class InfoForm(FlaskForm):

    breed = StringField("What Breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Have you been neutered?")
    mood = RadioField("please choose you mood:", choices=[('mood_one','Happy'),('mood_one','Excited')])
    food_choice = SelectField(u'Pick your favorite food:',
                              choices=[("chi","chicken"),("bf","beef"),
                                       ("fish","Fish")])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

@app.route('/', methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['feedback'] = form.feedback.data
        return redirect(url_for('thankyouforms'))
    return render_template('forms.html',form=form)

@app.route('/thankyouforms')
def thankyouforms():
    return render_template('thankyouforms.html')
if __name__ == '__main__':
    app.run(debug=True)