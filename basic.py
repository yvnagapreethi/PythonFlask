# Set up your imports and your flask app.
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    # This home page should have the form.
    return render_template("index.html")


# This page will be the page after the form
@app.route('/report')
def report():
    lower_letter = False
    upper_letter = False
    last_num = False

    username = request.args.get('username')

    lower_letter = any(letter.islower() for letter in username)
    upper_letter = any(letter.isupper() for letter in username)
    last_num = username[-1].isdigit()

    report = lower_letter and upper_letter and last_num

    return render_template('report.html', report=report,
                           lower_letter=lower_letter, upper_letter=upper_letter,
                           last_num=last_num)


if __name__ == '__main__':
    app.run(debug=True)
