from nose.tools import *
from glint.command import *

# test single positional
def single_positional_handler(test):
	assert_equal('test', test)

def single_positional_test():
	command = Command(single_positional_handler, '', '--')
	
	assert_equal(1, len(command.positional))
	assert_equal(0, len(command.optional))
	assert_equal(0, len(command.flags))
	
	command.run(['test'])

# test two positional

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