import inspect

from . import utils

class Command:
	def __init__(self, method, description, prefix):
		self._method = method
		self._prefix = prefix
		self.description = description
		
		self.positional = []
		self.optional = []
		self.flags = []
		
		sig = inspect.signature(self._method)
		
		for name in sig.parameters:
			param = sig.parameters[name]
			arg = (name, param.annotation if param.annotation is not inspect.Parameter.empty else None)
			
			if param.default is not inspect.Parameter.empty:
				if isinstance(param.default, bool):
					self.flags.append(arg)
				else:
					self.optional.append(arg)
			else:
				self.positional.append(arg)
				
	
	def run(self, args):
		if utils.is_none_or_empty(args):
			res = self._method()
		else:
			kwargs = {}
			positionals = []
			index = 0
			pos_index = 0
			
			while index < len(args):
				arg = args[index]
				
				if arg.startswith(self._prefix):
					name = arg[len(self._prefix):]
					
					if any(name in opt[0] for opt in self.optional):
						index += 1
						
						if index < len(args):
							kwargs[name] = args[index]
						else:
							raise Exception('Optional parameter with no value specified: %s' % name)
					elif any(name in flag[0] for flag in self.flags):
						kwargs[name] = True
					else:
						raise Exception('Unknown flag %s' % name)
				elif pos_index < len(self.positional):
					name = self.positional[pos_index][0]
					
					kwargs[name] = arg
					positionals.append(name)
				else:
					raise Exception('Unexpected parameter %s' % arg)
				
				index += 1
			
			# Check that all of the positionals have been supplied
			for pos in self.positional:
				if pos[0] not in positionals:
					raise Exception('Expected value for %s was not found.' % pos[0])
			
			res = self._method(**kwargs)