#coding:utf-8
from app import app
from flask import render_template, flash, redirect, url_for,request
from .forms import LoginForm
from .models import User 
from flask_login import current_user, login_user

@app.route('/')
@app.route('/index')
def index():
    user={'name':current_user.username,'number':9527}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user, remember=form.remember_me.data)
        flash('Logged in successfully.')
        return redirect(url_for('index'))
    return render_template('login.html', form=form)