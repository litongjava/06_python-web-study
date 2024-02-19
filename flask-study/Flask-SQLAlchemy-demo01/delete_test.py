from app import app, db
from models import User

with app.app_context():
  user_admin = User.query.filter_by(username='new_admin').first()
  db.session.delete(user_admin)
  db.session.commit()
