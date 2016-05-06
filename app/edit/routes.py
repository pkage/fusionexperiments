from . import edit
from flask import render_template

@edit.route('/edit')
def serve_editor():
	return render_template("edit.html");

