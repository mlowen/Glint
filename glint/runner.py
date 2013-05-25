import sys
import inspect

from .command import *

# Exceptions

class InvalidHandlerException(Exception):
	def __init__(self):
		Exception.__init__(self)

class CommandExistsException(Exception):
	def __init__(self, message):
		Exception.__init__(self)
		
		self.message = message

# Functionality

class Runner:
	def __init__(self, description = None, show_usage = True, prefix = '--'):
		self._commands = {}
		self._description = description
		self._show_usage = show_usage
		self._prefix = prefix
		
		if show_usage:
			self['help'] = (self.help, 'Show this message and exit')
	
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
				self._usage('No command specified.')
				return	
		else:
			name = args[0]
			
			if name not in self._commands:
				self._usage('Unknown command \'%s\'.' % name)
				return
				
			command = self._commands[name]
		
		if command is not None:
			try:
				command.run(args[1:])
			except InvalidCommandException as e:
				print(e.message)
				
				print('\nFor correct usage for command see: %s help --command %s' % (sys.argv[0], name))
	
	def help(self, command = None):
		if command is not None:
			self._command_usage(command)
		else:
			self._usage()
	
	# Private methods
	
	def _add(self, command, method, description = None):
		if command in self._commands:
			raise CommandExistsException('Cannot add two commands with the same name: %s' % command)
		elif not inspect.isroutine(method):
			raise InvalidHandlerException() 
		
		self._commands[command] = Command(method, description, self._prefix)
	
	def _print_arguments(self, title, args, max_padding):
		print('%s:\n' % title)
			
		for a in args:
			if utils.is_none_or_whitespace(a[1]):
				print('  %s' % a[0])
			else:
				padding = ' ' * (max_padding - len(a[0]))
				
				print('  %s%s%s' % (a[0], padding, a[1]))
		
		print('') # Added in for padding
	
	def _max_padding(self, args):
		max_padding = 0
		
		for a in args:
			l = len(a)
			max_padding = l if l > max_padding else max_padding
					
		return max_padding + 3
			
	def _usage(self, message = None):
		commands = [c for c in self._commands if c is not None]
		max_padding = self._max_padding(commands)
		
		print('%s\n' % message if not utils.is_none_or_whitespace(message) else '')
		
		print('usage: %s %s\n' % (sys.argv[0], '[<command>]' if None in self else '<command>'))
		
		if len(commands) > 0:
			self._print_arguments('Available commands', [(c, self._commands[c].description) for c in commands], max_padding)
			
			print('See \'%s help --command <command>\' for help on that command.' % sys.argv[0])
	
	def _command_usage(self, command_name):
		if command_name not in self._commands:
			print('Unknown command %s, run \'%s help\' for a list of commands.' % (command_name, sys.argv[0]))
			return
		
		command = self._commands[command_name]
		
		positionals = command.positional
		optionals = [('%s%s <%s>' % (self._prefix, o[0], o[0]), o[1]) for o in command.optional]
		flags = [('%s%s' % (self._prefix, f[0]), f[1]) for f in command.flags]
		
		max_padding = self._max_padding([p[0] for p in positionals] + [o[0] for o in optionals] + [f[0] for f in flags])
		
		if not utils.is_none_or_whitespace(command.description):
			print('\n%s' % command.description)
		
		params = (
			sys.argv[0], 
			command_name, 
			' '.join(['<%s>' % p[0] for p in positionals]), 
			' '.join(['[%s]' % o[0] for o in optionals]), 
			' '.join(['[%s]' % f[0] for f in flags])
		)
		
		print('\nusage: %s %s %s %s %s\n' % params)
		
		if len(command.positional) > 0: self._print_arguments('Arguments', positionals, max_padding)		
		if len(command.optional) > 0: self._print_arguments('Optional Arguments', optionals, max_padding)
		if len(command.flags) > 0: self._print_arguments('Flags', flags, max_padding)