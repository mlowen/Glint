import sys
import inspect

from .command import *
from .usage import *

# Exceptions

class InvalidHandlerException(Exception):
	def __init__(self):
		Exception.__init__(self)

class CommandExistsException(Exception):
	def __init__(self, message):
		Exception.__init__(self)
		
		self.message = message

class UnknownCommandException(Exception):
	def __init__(self, command):
		Exception.__init__(self)
		
		self.command = command

class NoCommandException(Exception):
	def __init__(self):
		Exception.__init__(self)

# Functionality

class Runner:
	def __init__(self, description = None, show_usage = True, prefix = '--'):
		self._commands = {}
		self._description = description
		self._show_usage = show_usage
		self._prefix = prefix
		
		if show_usage:
			self['help'] = (self.help, 'Show this message and exit.')
	
	# Accessors
	
	def __setitem__(self, key, value):
		if isinstance(value, tuple):
			self._add(key, value[0], value[1])
		else:
			self._add(key, value)

	def __contains__(self, key):
		return key in self._commands
	
	def __len__(self):
		return len(self._commands)
	
	# Public methods
	
	def run(self, args = None):
		if args is None:
			args = sys.argv[1:]
		
		command = None

		if len(args) == 0:
			if None in self:
				command = self._commands[None]
			else:
				if not self._show_usage:
					raise NoCommandException()
				
				self._usage('No command specified.')
				return	
		else:
			name = args[0]
			
			if name not in self._commands:
				if not self._show_usage:
					raise UnknownCommandException(name)
				
				self._usage('Unknown command \'%s\'.' % name)
				
				return
				
			command = self._commands[name]
		
		if command is not None:
			try:
				command.run(args[1:])
			except InvalidCommandException as e:
				if not self._show_usage:
					raise e
				
				print(e.message)
				print('\nFor correct usage for command see: %s help --command %s' % (sys.argv[0], name))
	
	def help(self, command = None):
		if command is not None:
			return self._command_usage(command)
		else:
			return self._usage()
	
	# Private methods
	
	def _add(self, command, method, description = None):
		if command in self._commands:
			raise CommandExistsException('Cannot add two commands with the same name: %s.' % command)
		elif not inspect.isroutine(method):
			raise InvalidHandlerException() 
		
		self._commands[command] = Command(method, description, self._prefix)
		
	def _usage(self, message = None):
		usage = Usage(self._prefix)
		
		usage.has_default = None in self
		usage.has_help = self._show_usage
		
		for cmd in [c for c in self._commands if c is not None]:
			usage.add_command(cmd, self._commands[cmd].description)
		
		if self._show_usage:
			print('%s\n' % message if not utils.is_none_or_whitespace(message) else '')
			print(usage)
		else:
			return usage
			
		return None
	
	def _command_usage(self, command_name):
		if command_name not in self._commands:
			if not self._show_usage:
				raise UnknownCommandException(command_name)
			
			print('Unknown command %s, run \'%s help\' for a list of commands.' % (command_name, sys.argv[0]))
			return
		
		command = self._commands[command_name]
		
		usage = command.usage()
		usage.name = command_name
		
		if not self._show_usage:
			return usage
		
		print(usage)
		return None
		