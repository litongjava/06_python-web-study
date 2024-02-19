from app import app, db  # 注意这里从app模块同时导入了app和db
from models import User  # noqa

# 创建并激活应用上下文
with app.app_context():
  db.create_all()
