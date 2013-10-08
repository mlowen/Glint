import inspect

from . import utils
from .usage import Usage

class InvalidCommandException(Exception):
	def __init__(self, message):
		Exception.__init__(self)
		
		self.message = message

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
				arg = (arg[0].replace('_', '-'), arg[1])
				
				if isinstance(param.default, bool):
					self.flags.append(arg)
				else:
					self.optional.append(arg)
			else:
				self.positional.append(arg)
	
	def run(self, args):
		kwargs = {}
		index = 0
		pos_index = 0
		
		while index < len(args):
			arg = args[index]
			
			if arg.startswith(self._prefix):
				name = arg[len(self._prefix):]
				equals_pos = name.find('=')
				
				if equals_pos >= 0 and any(name[:equals_pos] in opt[0] for opt in self.optional):
					kwargs[name[:equals_pos].replace('-', '_')] = name[(equals_pos + 1):]
				elif any(name in opt[0] for opt in self.optional):
					index += 1
					
					if index < len(args):
						kwargs[name.replace('-', '_')] = args[index]
					else:
						raise InvalidCommandException('Optional parameter with no value specified: %s%s' % (self._prefix, name))
				elif any(name in flag[0] for flag in self.flags):
					kwargs[name.replace('-', '_')] = True
				else:
					raise InvalidCommandException('Unknown flag %s%s' % (self._prefix, name))
			elif pos_index < len(self.positional):
				name = self.positional[pos_index][0]
				
				kwargs[name] = arg
				pos_index += 1
			else:
				raise InvalidCommandException('Unexpected parameter %s' % arg)
			
			index += 1
		
		# Check that all of the positionals have been supplied
		for pos in self.positional:
			if pos[0] not in kwargs:
				raise InvalidCommandException('Expected value for %s was not found.' % pos[0])
		
		res = self._method(**kwargs)
		
	def usage(self):
		usage = Usage(self._prefix)
		usage.description = self.description
		
		for p in self.positional: usage.add_positional_argument(p[0], p[1])
		for o in self.optional: usage.add_optional_argument(o[0], o[1])
		for f in self.flags: usage.add_flag(f[0], f[1])
		
		return usage