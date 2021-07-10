# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask, render_template, flash, redirect, url_for, make_response, request
from forms import RegistrationForm, LoginForm

# from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '91a80165eabf4597daa8e02eac03600c'


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
#
# db = SQLAlchemy(app)
#
#
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(20), unique=True, nullable=False)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', page_name="Home")


@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        res = make_response(redirect(url_for(form.choice.data.lower())))
        res.set_cookie('login', 'true')
        return res
        # if form.choice.data == 'Citizen':
        #     return redirect(url_for('citizen'))
        # if form.choice.data == 'Councillor':
        #     return redirect(url_for('councillor'))
        # if form.choice.data == 'Admin':
        #     return  redirect(url_for('admin'))
    return render_template('login.html', page_name="Login", form=form)


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created successfully for {form.firstname.data}!', 'success')
        return redirect(url_for('signup'))
    return render_template('signup.html', page_name="Signup", form=form)


@app.route('/account')
def citizen():
    if request.cookies.get('login') == 'true':
        return render_template('citizen_account.html', page_name="account")
    return redirect(url_for('error'))


@app.route('/error')
def error():
    return render_template('error.html')


if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
