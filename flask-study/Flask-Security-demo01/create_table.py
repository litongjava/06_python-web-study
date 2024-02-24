from app import app
from db import db
from models import *  # noqa

with app.app_context():
  db.create_all()
