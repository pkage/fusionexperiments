def max_length(length):
	def validate(value):
		if len(value) <= length:
			return True
		raise Exception("%s must be at least %s long" % length);
	return validate

