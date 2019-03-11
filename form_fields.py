from flask import Flask, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, TextAreaField,
                     RadioField, SelectField,
                     SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mykey'


class InfoForm(FlaskForm):

    breed = StringField("What breed are you?", validators=[DataRequired()])
    neutered = BooleanField("Are you neutered?")
    mood = RadioField("Please choose your mood:",
                      choices=[('mood_one', 'Happy'), ('mood_two', 'Excited')])
    food_choice = SelectField("Pick your favourite food",
                              choices=[('chi', 'Chicken'), ('mut', 'Mutton')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():

    form = InfoForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data

        return redirect(url_for('thankyou'))

    return render_template("fields.html", form=form)


@app.route('/thankyou')
def thankyou():

    return render_template('thank_you.html')


if __name__ == "__main__":
    app.run(debug=True)
