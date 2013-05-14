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

def missing_positional_argument_test():
	command = Command(single_positional_argument_handler, '', '--')
	
	assert_raises(InvalidCommandException, command.run, [])

# test unexpected positional

def extra_positional_argument_test():
	command = Command(single_positional_argument_handler, '', '--')
	
	assert_raises(InvalidCommandException, command.run, ['foo', 'bar'])

# test optional

def optional_parameter_handler(a = None):
	assert_equal('foo', a)

def optional_parameter_test():
	command = Command(optional_parameter_handler, '', '--')

	assert_equal(0, len(command.positional))
	assert_equal(1, len(command.optional))
	assert_equal(0, len(command.flags))

	command.run(['--a', 'foo'])

# test optional not supplied

def optional_parameter_not_supplied_handler(a = None):
	assert_is_none(a)

def optional_parameter_not_supplied_test():
	command = Command(optional_parameter_not_supplied_handler, '', '--')

	command.run([])	

# test optional and positional
def optional_and_positional_parameters_handler(a, b = None):
	assert_equal('foo', a)
	assert_equal('bar', b)

def optional_and_positional_paramenters_test():
	command = Command(optional_and_positional_parameters_handler, '', '--')

	assert_equal(1, len(command.positional))
	assert_equal(1, len(command.optional))
	assert_equal(0, len(command.flags))

	command.run(['foo', '--b', 'bar'])

# test optional before positional
def optional_before_positional_paramenters_test():
	command = Command(optional_and_positional_parameters_handler, '', '--')

	command.run(['--b', 'bar', 'foo'])

# test positional and optional not specified

def positional_with_unspecified_optional_handler(a, b = None):
	assert_equal('foo', a)
	assert_is_none(b)

def positional_with_unspecified_optional_test():
	command = Command(positional_with_unspecified_optional_handler, '', '--')
	command.run(['foo'])

# test optional with no value
def optional_parameter_with_no_value_test():
	command = Command(optional_parameter_handler, '', '--')
	
	assert_raises(InvalidCommandException, command.run, ['--a'])

# test flag
def flag_handler(a = False):
	assert_true(a)

def flag_test():
	command = Command(flag_handler, '', '--')

	assert_equal(0, len(command.positional))
	assert_equal(0, len(command.optional))
	assert_equal(1, len(command.flags))

	command.run(['--a'])

# test flag not supplied
def flag_not_supplied_handler(a = False):
	assert_false(a)

def flag_not_supplied_test():
	command = Command(flag_not_supplied_handler, '', '--')
	command.run([])

# test flag and positional
def flag_and_positional_parameter_handler(a, b = False):
	assert_equal('foo', a)
	assert_true(b)

def flag_positional_parameter_test():
	command = Command(flag_and_positional_parameter_handler, '', '--')
	
	assert_equal(1, len(command.positional))
	assert_equal(0, len(command.optional))
	assert_equal(1, len(command.flags))

	command.run(['foo', '--b'])

# test flag before positional

def flag_before_positional_parameter_test():
	command = Command(flag_and_positional_parameter_handler, '', '--')
	
	assert_equal(1, len(command.positional))
	assert_equal(0, len(command.optional))
	assert_equal(1, len(command.flags))

	command.run(['--b', 'foo'])

# test positional with unspecified flag

# test flag and optional

# test flag and optional and positional

# test optional and positional and unspecfied flag

# test optional and flag and uspecified positional

# test optional and uspecified flag and positional

# test unknown flag