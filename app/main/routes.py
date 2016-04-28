from . import main
from flask import render_template

@main.route('/')
def front():
	return render_template('front.html');
