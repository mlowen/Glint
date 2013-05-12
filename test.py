#! /bin/env python

import arguments

def default():
	print('This is the default action.')

def hello(name:'The name of who to say hello to.'):
	print('Hello %s.' % name)

def goodbye(name:'Name of who to say good bye to.' = None, niceday:'Tell them to have a nice day.' = False):
	msg = 'Good bye'
	
	if name is not None:
		msg += ' %s' % name
	
	if niceday:
		msg += ', have a nice day.'
	
	print(msg)

runner = arguments.Runner()

runner[None] = default
runner['hello'] = (hello, 'Says hello and exits.')
runner['goodbye'] = (goodbye, 'Says goodbye and exits')

if __name__ == '__main__':
	runner.run()