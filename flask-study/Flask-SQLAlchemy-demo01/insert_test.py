# 创建新用户
from app import app, db
from models import User

admin = User(username='admin')
guest = User(username='guest')
with app.app_context():
  # 将新建用户添加到会话中
  db.session.add(admin)
  db.session.add(guest)
  # 提交会话到数据库
  db.session.commit()
