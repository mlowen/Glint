import sys
import inspect

from . import utils
from .command import *


class Runner:
	def __init__(self, description = None, show_usage = True, prefix = '--'):
		self._commands = {}
		self._show_usage = show_usage
		self._prefix = prefix
		
		self['help'] = (self.help, 'Show this message and exit')
	
	def __setitem__(self, key, value):
		if isinstance(value, tuple):
			self.add(key, value[0], value[1])
		else:
			self.add(key, value)

	def __contains__(self, key):
		return key in self._commands

	def add(self, command, method, description = None):
		if command in self._commands:
			raise Exception('Cannot add two commands with the same name: %s' % command)
		
		self._commands[command] = Command(method, description, self._prefix)

	def run(self, args = None):
		if args is None:
			args = sys.argv[1:]
		
		command = None

		if len(args) == 0:
			if None in self:
				command = self._commands[None]
			else:
				self.usage('No command specified.')
				return	
		else:
			name = args[0]
			
			if name not in self._commands:
				self.usage('Unknown command \'%s\'.' % name)
				return
				
			command = self._commands[name]
		
		if command is not None:
			command.run(args[1:])
	
	def help(self, command = None):
		if command is not None:
			self.command_usage(command)
		else:
			self.usage()
	
	def command_usage(self, command):
		print('hello, you want to find out about %s' % command)
	
	def usage(self, message = None):
		commands = [c for c in self._commands if c is not None]
		max_padding = len(max(commands)) + 3
		
		if not utils.is_none_or_whitespace(message):
			print('%s\n' % message)
		
		print('usage: %s %s\n' % (sys.argv[0], '[<command>]' if None in self else '<command>'))
		
		if len(commands) > 0:
			print('Available commands:')
			
			for name in commands:
				description = self._commands[name].description
				
				if utils.is_none_or_whitespace(description):
					print('  %s' % name)
				else:
					padding = ' ' * (max_padding - len(name))
					
					print('  %s%s%s' % (name, padding, description))
			
			print('\nSee \'%s help <command>\' for help on that command.' % sys.argv[0])