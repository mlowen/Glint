from nose.tools import *
from glint.command import *

# test single positional

def single_positional_argument_handler(test):
	assert_equal('test', test)

def single_positional_argument_test():
	command = Command(single_positional_argument_handler, '', '--')
	
	assert_equal(1, len(command.positional))
	assert_equal(0, len(command.optional))
	assert_equal(0, len(command.flags))
	
	command.run(['test'])

# test two positional

def two_positional_arguments_handler(a, b):
	assert_equal('foo', a)
	assert_equal('bar', b)

def two_positional_arguments_test():
	command = Command(two_positional_arguments_handler, '', '--')
	
	assert_equal(2, len(command.positional))
	assert_equal(0, len(command.optional))
	assert_equal(0, len(command.flags))
	
	command.run(['foo', 'bar'])

# test no positional supplied

# test unexpected positional

# test optional

# test optional not supplied

# test optional and positional

# test optional before positional

# test optional with no value

# test flag

# test flag not supplied

# test flag and positional

# test flag before positional

# test flag and optional

# test flag and optional and positional

# test unknown flag