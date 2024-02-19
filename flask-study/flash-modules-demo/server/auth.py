from apiflask import APIBlueprint
from flask import request, session, jsonify

from server.log import logger

auth = APIBlueprint('auth', __name__)


@auth.route('/login')
def login():
  user = request.form.get('user')
  pwd = request.form.get('pwd')

  if user == 'admin' and pwd == '123':
    session['user'] = user
    logger.info(f"Successful login attempt by user: {user}")
    return jsonify({"status": "success"})

  logger.info(f"Failed login attempt with username: {user}")
  return jsonify({"error": "username or password is not correct"})
