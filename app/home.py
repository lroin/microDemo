#coding:utf-8
from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user={'name':'kii','number':9527}
    return render_template('index.html', title='Home', user=user)