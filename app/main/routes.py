from . import main
from flask import render_template

@main.route('/')
def main():
	return render_template('layouts/chair.html', chair='Systems');
