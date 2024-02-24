from functools import wraps

from flask import redirect, url_for
from flask_login import current_user


def requires_roles(*roles):
  def wrapper(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
      if current_user.is_authenticated and any(role in roles for role in current_user.roles):
        return f(*args, **kwargs)
      # return redirect(url_for('login_page'))  # 如果用户没有角色，重定向到登录页面
      return {"code": 0, "mesage": "please login"}

    return wrapped

  return wrapper
