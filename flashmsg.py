from flask import Flask, flash, render_template, url_for, redirect, session
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'nmykey'


class SimpleFlash(FlaskForm):

    breed = StringField("Enter the breed")
    submit = SubmitField("Click Me.")


@app.route('/', methods=['GET', 'POST'])
def index():

    form = SimpleFlash()

    if form.validate_on_submit():
        session['breed'] = form.breed.data
        flash("The breed is {}".format(session['breed']))
        redirect(url_for("index"))

    return render_template("flash_index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
