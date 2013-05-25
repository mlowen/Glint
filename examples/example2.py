#! /bin/env python

import glint

class Application(glint.Runner):
	def __init__(self):
		glint.Runner.__init__(self)
		
		self[None] = self.default
		self['hello'] = (self.hello, 'Says hello and exits.')
		self['goodbye'] = (self.goodbye, 'Says goodbye and exits')
	
	def default(self):
		print('This is the default action.')

	def hello(self, name:'The name of who to say hello to.'):
		print('Hello %s.' % name)

	def goodbye(self, name:'Name of who to say good bye to.' = None, niceday:'Tell them to have a nice day.' = False):
		msg = 'Good bye'
		
		if name is not None:
			msg += ' %s' % name
		
		if niceday:
			msg += ', have a nice day.'
		
		print(msg)

if __name__ == '__main__':
	app = Application()	
	app.run()