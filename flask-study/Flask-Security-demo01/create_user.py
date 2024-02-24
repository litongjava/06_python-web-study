from flask_security.utils import encrypt_password

from app import app
from db import db
from security import user_datastore


def create_user():
  db.create_all()
  if not user_datastore.find_role("admin"):
    user_datastore.create_role(name="admin", description="Administrator")
  if not user_datastore.find_user(email="admin@example.com"):
    user_datastore.create_user(email="admin@example.com", password=encrypt_password("password"), roles=["admin"])
  db.session.commit()


with app.app_context():
  create_user()
