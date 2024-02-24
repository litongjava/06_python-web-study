from db import db
from models import Permission


class PermissionDao:
  def add_permission_if_not_exists(self, permission_name):
    # 使用给定的权限名称查询数据库看是否已存在该权限
    permission = Permission.query.filter_by(name=permission_name).first()

    # 如果不存在，则创建新的权限
    if not permission:
      permission = Permission(name=permission_name)
      db.session.add(permission)  # 将新权限添加到数据库会话
      db.session.commit()  # 提交会话到数据库，保存更改

    return permission  # 返回权限实例（不管是新创建的还是已存在的）
