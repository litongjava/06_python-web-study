from flask import session, jsonify, request

from server import app

app.debug = True


@app.before_request
def before():
  url = request.path
  passUrl = ["/login", "/regist"]
  if url in passUrl:
    pass
  else:
    _id = session.get("_id", None)
    if not _id:
      return jsonify({"info": "not login"})
    else:
      pass


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000)
