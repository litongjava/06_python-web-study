from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# 数据库配置：这里以 SQLite 为例
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
# 初始化 SQLAlchemy
db = SQLAlchemy(app)
