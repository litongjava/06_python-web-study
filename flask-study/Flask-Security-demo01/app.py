from apiflask import APIFlask
from flask_login import LoginManager

import env_config

app = APIFlask(__name__)
# 数据库配置：这里以 SQLite 为例
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test02.db'
# 确保添加了 SECRET_KEY
app.config['SECRET_KEY'] = env_config.SECRET_KEY
# 增加 SECURITY_PASSWORD_SALT 配置
app.config['SECURITY_PASSWORD_SALT'] = env_config.SECURITY_PASSWORD_SALT

login_manager = LoginManager(app)


@login_manager.user_loader
def load_user(user_id):
  from models import User
  return User.query.get(int(user_id))


@app.route("/hc", methods=["GET"])
def healthcheck():
  """
  Health check endpoint for the backend API.
  Returns:
      JSON object: Contains a status message and HTTP status code.
  """
  return {"message": "API is up and running!", "status": "OK"}


from auth_controller import auth

app.register_blueprint(auth)
