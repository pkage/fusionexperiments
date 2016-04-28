from mongokit import Document
from .validators import max_length

class Experiment(Document):
	structure = {
		"name": unicode,
		"author": unicode,
		"description": unicode,
		"libraries": list,
		"js": unicode,
		"html": unicode
	}
	validators = {
		"name": max_length(32),
		"author": max_length(32),
		"description": max_length(500)
	}
	use_dot_notation = True;

