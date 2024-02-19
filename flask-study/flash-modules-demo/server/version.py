from apiflask import APIBlueprint

version = APIBlueprint('version', __name__)


@version.route('/version')
def version_api():
  return "v1.0.0"
