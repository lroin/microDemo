#coding:utf-8
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'vMZm1BZI8AHR1Nd0gij'
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \'sqlite:///' + os.path.join(basedir, 'db.sqlite3')
    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:20954136qq@zsdgn.cc:3306/blog?charset=utf8mb4'
    SQLALCHEMY_TRACK_MODIFICATIONS = False