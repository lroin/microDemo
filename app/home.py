#coding:utf-8
from app import app
from flask import render_template, flash, redirect, url_for
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user={'name':'kii','number':9527}
    return render_template('index.html', title='Home', user=user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)