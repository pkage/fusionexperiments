from . import data

@data.route('/data/<data_id>')
def serve_data(data_id):
	return '{data: "' + data_id + '"}';
