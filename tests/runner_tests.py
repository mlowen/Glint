from nose.tools import *
import glint

# Handlers

handler_run = None

def default_handler():
	handler_run = 'default'

# Create with defaults
def create_with_defaults_test():
	runner = glint.Runner()
	
	assert_equal(None, runner._description)
	assert_equal('--', runner._prefix)
	assert_true(runner._show_usage)
	assert_equal(1, len(runner._commands))
	assert_true('help' in runner._commands)

# Create with parameters
def create_with_parameters_test():
	runner = glint.Runner(description = 'test', show_usage = False, prefix = '+')
	
	assert_equal('test', runner._description)
	assert_equal('+', runner._prefix)
	assert_false(runner._show_usage)	
	assert_equal(0, len(runner))

# Add handler
def add_handler_test():
	runner = glint.Runner()
	runner['test'] = default_handler
	
	assert_equal(2, len(runner._commands))
	assert_equal(default_handler, runner._commands['test']._method)

# Add handler with description
def add_handler_with_description_test():
	runner = glint.Runner()
	runner['test'] = (default_handler, 'testing')
	
	assert_equal(2, len(runner._commands))
	assert_equal(default_handler, runner._commands['test']._method)
	assert_equal('testing', runner._commands['test'].description)

# Add handler that is not a method

# Add handler with description that is not a method

# Add handler with different prefix

# Add multiple handlers

# Check length

# Check contains

# Return usage 

# Run correct handler

# Run default handler

# Exception when unable to find handler and show usage is false

# Exception when bad parameters are passed to command and show usage is false