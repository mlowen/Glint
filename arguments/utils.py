import re

def is_none_or_empty(obj):
	return obj is None or len(obj) == 0

def is_none_or_whitespace(string):
	return is_none_or_empty(string) or re.match(r'^\s+$', string) is not None

def enum(**enums):
	return type('Enum', (), enums)