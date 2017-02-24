#coding=utf-8
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# 初始化flask应用
app = Flask(__name__)
# 读取配置文件
app.config.from_object('config')
# 创建数据库
db = SQLAlchemy(app)

# 初始化flask-Login
lm = LoginManager()
lm.setup_app(app)

import views, models
