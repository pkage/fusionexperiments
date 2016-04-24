from . import scripts
from .. import socketio

@api.route('/scripts')
def scripts_base():
	return "scripts!"

@api.on('execute_script')
def execute_script(data):
	print(data);
