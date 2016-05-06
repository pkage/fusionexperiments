from flask import Flask
from flask.ext.socketio import SocketIO

socketio = SocketIO()

from mongokit import Connection, Document

connection = Connection('localhost', 27017);

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'b5-3356-4814-b876-866a51266fa3';
    app.jinja_env.trim_blocks = True
    app.jinja_env.lstrip_blocks = True

    from .schema import register_models
    register_models(connection);

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    from .edit import edit as edit_blueprint
    app.register_blueprint(edit_blueprint)

    socketio.init_app(app)

    
    return app
