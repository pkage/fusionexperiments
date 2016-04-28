from mongokit import Document

class DataSource(Document):
	structure = {
		"name": str,
		"data_url": str
	}
	use_dot_notation = True;
