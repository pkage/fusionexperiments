from flask import Flask
from flask.ext.socketio import SocketIO

socketio = SocketIO()

from pymongo import MongoClient

mongo_client = MongoClient()
mongo_client = MongoClient('localhost', 27017)
mongo_db = mongo_client['fe']

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'fc2e1d79-f983-4d4a-8956-53acb063ef98';
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    socketio.init_app(app)
    return app
