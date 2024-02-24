from flask_security import UserMixin, RoleMixin

from db import db

# 用户和角色的多对多关系
users_roles = db.Table('users_roles',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                       )


# 定义模型
class Role(db.Model, RoleMixin):
  id = db.Column(db.Integer(), primary_key=True)
  name = db.Column(db.String(80), unique=True)
  description = db.Column(db.String(255))


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(600), nullable=False)
  active = db.Column(db.Boolean())
  roles = db.relationship('Role', secondary=users_roles, backref=db.backref('users', lazy='dynamic'))
