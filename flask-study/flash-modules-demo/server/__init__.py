from apiflask import APIFlask

# create app
app = APIFlask(__name__)

# register auth
from .auth import auth as auth_blueprint

app.register_blueprint(auth_blueprint)

# register version
from .version import version as version_blueprint

app.register_blueprint(version_blueprint)
