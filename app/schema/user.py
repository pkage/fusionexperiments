from mongokit import Document
from .validators import max_length

class User(Document):
	structure = {
		"username": str,
		"name": unicode,
		"password_hash": str,
		"password_salt": str
	}
	validators = {
		"username": max_length(16),
		"name": max_length(32)
	}
	use_dot_notation = True;
