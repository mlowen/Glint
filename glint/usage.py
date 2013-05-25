import re
import sys

from . import utils

class Usage:
	def __init__(self, prefix):
		self.has_default = False
		self.has_help = False

		self.name = ''
		self.description = ''
		
		self._prefix = prefix
		self._commands = []
		self._positional_arguments = []
		self._optional_arguments = []
		self._flags = []
	
	def add_command(self, name, description):
		self._commands.append((name, description))
	
	def add_positional_argument(self, name, description):
		self._positional_arguments.append((name, description))
	
	def add_optional_argument(self, name, description):
		print('Adding optional argument: %s' % name)
		
		self._optional_arguments.append(('%s%s' % (self._prefix, name), description, name))
	
	def add_flag(self, name, description):
		self._flags.append(('%s%s' % (self._prefix, name), description))
	
	def __str__(self):
		lines = []
		
		max_padding = self._max_padding()
		
		commands = self._get_commands(max_padding)
		positionals = self._get_positional_arguments(max_padding)
		optionals = self._get_optional_arguments(max_padding)
		flags = self._get_flags(max_padding)
		
		if not utils.is_none_or_whitespace(self.description):
			lines.append('\n%s\n' % self.description)
		
		usage = 'usage: %s %s %s %s %s %s' % (sys.argv[0], self.name, commands[0], positionals[0], optionals[0], flags[0])
		
		lines.append('%s\n' % re.sub(r'\s+', ' ', usage))
		
		lines += commands[1] + positionals[1] + optionals[1] + flags[1]
		
		if self.has_help:
			lines.append('See \'%s help --command <command>\' for help on that command.' % sys.argv[0])
		
		return '\n'.join(lines[0:-1] if utils.is_none_or_whitespace(lines[-1:][0]) else lines)
		
	# Private Functions
	
	def _max_padding(self):
		args = [c[0] for c in (self._commands + self._positional_arguments + self._optional_arguments + self._flags)]
		
		max_padding = 0
		
		for a in args:
			l = len(a)
			max_padding = l if l > max_padding else max_padding
					
		return max_padding + 3
	
	def _format_arguments(self, title, args, max_padding):
		lines = [ '%s:\n' % title ]
			
		for a in args:
			if utils.is_none_or_whitespace(a[1]):
				lines.append('  %s' % a[0])
			else:
				padding = ' ' * (max_padding - len(a[0]))
				
				lines.append('  %s%s%s' % (a[0], padding, a[1]))
		
		lines.append('') # Added in for padding
		
		return lines
	
	def _get_commands(self, max_padding):
		if len(self._commands) > 0:
			command = '[<command>]' if self.has_default else '<command>'
			command_list = self._format_arguments('Commands', self._commands, max_padding)
			
			return (command, command_list)
		
		return ('', [])
	
	def _get_positional_arguments(self, max_padding):
		if len(self._positional_arguments) > 0:
			positionals = ' '.join(['<%s>' % p[0] for p in self._positional_arguments])
			positionals_list = self._format_arguments('Arguments', self._positional_arguments, max_padding)
			
			return (positionals, positionals_list)
		
		return ('', [])
		
	def _get_optional_arguments(self, max_padding):		
		if len(self._optional_arguments) > 0:
			optionals = ' '.join(['[%s <%s>]' % (o[0], o[2]) for o in self._optional_arguments])
			optionals_list = self._format_arguments('Optional Arguments', self._optional_arguments, max_padding)
			
			return (optionals, optionals_list)
			
		return ('', [])
	
	def _get_flags(self, max_padding):
		if len(self._flags) > 0:
			flags = ' '.join(['[%s]' % f[0] for f in self._flags])
			flags_list = self._format_arguments('Flags', self._flags, max_padding)
			
			return (flags, flags_list)
		
		return ('', [])
