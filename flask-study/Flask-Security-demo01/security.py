# 设置 Flask-Security
from flask_security import SQLAlchemyUserDatastore, Security

from app import app
from db import db
from models import User, Role

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)