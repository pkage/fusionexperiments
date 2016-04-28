from mongokit import Document

class Library(Document):
	structure = {
		"name": str,
		"url": str
	}
	use_dot_notation = True
