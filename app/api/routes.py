from . import api
from .. import socketio
from flask import render_template

@api.route('/scripts')
def scripts_base():
	return "scripts!"

@api.route('/debug/reload')
def bcast_reload():
	socketio.emit('debug', {'directive': 'reload'});
	return "reloaded!";

@socketio.on('execute_script')
def execute_script(data):
	print(data);

@api.route('render_embed/:id')
def render_embed(id):
	return render_template('embed.html');
