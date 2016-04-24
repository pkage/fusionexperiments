#! /usr/bin/env python

from app import create_app, socketio

if __name__ == "__main__":
	app = create_app(debug=True);
	socketio.run(app, port=8080);
