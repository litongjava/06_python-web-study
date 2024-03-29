from apiflask import APIBlueprint
from flask import redirect, url_for
from flask_login import login_required, login_user, logout_user

from models import User
from wrappers import requires_roles, requires_permissions

auth = APIBlueprint('auth', __name__)


@auth.route('/login')
def login():
  # 登录逻辑，在实际情况中会更复杂
  user = User.query.get(1)
  login_user(user)
  return redirect(url_for('auth.protected'))


@auth.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('home'))


@auth.route('/')
def home():
  return 'Home Page'


@auth.route('/protected')
@login_required  # 确保用户必须登录
@requires_roles('admin')  # 使用装饰器限制只有具备 'admin' 角色的用户才能访问
def protected():
  return 'Protected Page - for Admins Only!'


@auth.route('/some-protected-route')
@requires_permissions('edit_post', 'delete_post')  # 例：需要编辑和删除帖子的权限
@login_required
def some_protected_view():
  # 视图逻辑
  return 'This is a protected view.'
