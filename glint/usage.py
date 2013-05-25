import sys

from . import utils

class Usage:
	def __init__(self, prefix):
		self.has_default = False
		self.has_help = False
		
		self._prefix = prefix
		self._commands = []
		self._positional_arguments = []
		self._optional_arguments = []
		self._flags = []
	
	def add_command(self, name, description):
		self._commands.append((name, description))
	
	def __str__(self):
		lines = []
		
		max_padding = self._max_padding()
		
		lines.append('usage: %s %s\n' % (sys.argv[0], '[<command>]' if self.has_default else '<command>'))
		
		if len(self._commands) > 0:
			lines += self._format_arguments('Commands', self._commands, max_padding)  
		
		if self.has_help:
			lines.append('See \'%s help --command <command>\' for help on that command.' % sys.argv[0])
		
		return '\n'.join(lines)
		
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