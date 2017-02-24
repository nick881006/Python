# coding=utf-8
import os

CSRF_ENABLED = True
SECRET_KEY = 'python-learning'

basedir = os.path.abspath(os.path.dirname(__file__))
#数据库文件的路径
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')