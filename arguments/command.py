import inspect

from . import utils

class Command:
	def __init__(self, method, description):
		self._method = method
		self.description = description
		
		sig = inspect.signature(self._method)
	
	def run(self, args):
		if utils.is_none_or_empty(args):
			self._method()
		else:
			self._method(args)