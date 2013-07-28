Inheritance
===========

So far in all of our examples we've been creating a separate runner and assigning commands to it, on this page we
are going to look at another way of setting up an application to use Glint via inheritance. Considering most of this 
content is covered else where in the documentation we're not going to step through the example, we're going to use
the final script from the :doc:`commands section <commands>` and port it to use inheritance. ::

	#! /bin/env python

	import glint

	class Application(glint.Runner):
		def __init__(self):
			glint.Runner.__init__(self)
			
			self[None] = self.default
			self['hello'] = self.hello
			
		def hello(self, name, wave = False, message = None):
			print('Hello %s.' % name)
			
			if wave:
				print('I\'m waving at you!')
			
			if message is not None:
				print('I want to tell you: %s' % message)
		
		def default(self):
			print('No command has been given to the application.')

	if __name__ == '__main__':
		app = Application()
		app.run()

.. toctree::
	:hidden:
	
	api