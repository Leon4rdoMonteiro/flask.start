from flask import Blueprint

apps = Blueprint('apps', __name__)

@apps.route('/<string:name>', methods=['GET'])
def hello(name):
    return { 'message' : 'Hello, %s!' % name } , 200