#! /bin/env python

import arguments

def default():
	print('This is the default taske')

def version():
	print('version - 0.1.0.0')

def optional(foo:'this is a description' = 4):
	print('We have optional arguments')

runner = arguments.Runner()	

runner[None] = default
runner['version'] = version
runner['optional'] = optional

if __name__ == '__main__':
	runner.run()