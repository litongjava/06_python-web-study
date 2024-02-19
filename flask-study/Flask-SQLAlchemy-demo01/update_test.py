from app import app, db
from models import User

with app.app_context():
  user_admin = User.query.filter_by(username='admin').first()
  # 更新用户
  user_admin.username = 'new_admin'
  db.session.commit()