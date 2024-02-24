from flask import Flask

import env_config

app = Flask(__name__)
# 数据库配置：这里以 SQLite 为例
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test02.db'
# 确保添加了 SECRET_KEY
app.config['SECRET_KEY'] = env_config.SECRET_KEY
# 增加 SECURITY_PASSWORD_SALT 配置
app.config['SECURITY_PASSWORD_SALT'] = env_config.SECURITY_PASSWORD_SALT