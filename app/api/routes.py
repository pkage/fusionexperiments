from . import scripts
from .. import socketio

@scripts.route('/scripts')
def scripts_base():
	return "scripts!"

@socketio.on('execute_script')
def execute_script(data):
	print(data);
