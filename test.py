#! /bin/env python

import arguments

def default():
	print('This is the default taske')

def version():
	print('version - 0.1.0.0')

runner = arguments.Runner()	

runner[None] = default
runner['version'] = version

if __name__ == '__main__':
	runner.run()