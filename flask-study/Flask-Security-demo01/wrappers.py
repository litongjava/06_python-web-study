from functools import wraps

from flask_login import current_user

from PermissionDao import PermissionDao


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


def requires_permissions(*permissions):
  def wrapper(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
      for permission_name in permissions:
        permission_dao = PermissionDao()
        permission = permission_dao.add_permission_if_not_exists(permission_name)
        has_permission = False
        for role in current_user.roles:
          if permission in role.permissions:
            has_permission = True
            break
        if not has_permission:
          return {"code": 0, "message": "Insufficient permissions"}
      return f(*args, **kwargs)

    return decorated_function

  return wrapper
