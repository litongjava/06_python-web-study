# 创建新用户
from app import app, db
from models import User

# 查询所有用户
with app.app_context():
  users = User.query.all()
  print(users)

  # 根据用户名查询
  user_admin = User.query.filter_by(username='admin').first()
  print(user_admin)