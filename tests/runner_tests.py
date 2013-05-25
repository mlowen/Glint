from nose.tools import *
import glint

# Handlers

handler_run = None

def default_handler():
	handler_run = 'default'

def test_handler():
	handler_run = 'test'

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
@raises(glint.InvalidHandlerException)
def add_handler_that_is_not_a_method_test():
	runner = glint.Runner()
	runner['test'] = 'foo'

# Add handler with description that is not a method
@raises(glint.InvalidHandlerException)
def add_handler_with_description_that_is_not_a_method_test():
	runner = glint.Runner()
	runner['test'] = ('foo', 'bar')

# Add handler with different prefix
def add_handler_with_different_prefix_test():
	runner = glint.Runner(prefix = '+')
	runner[None] = default_handler
	
	for c in runner._commands:
		assert_equal('+', runner._commands[c]._prefix)

# Add multiple handlers
def add_multiple_handlers_test():
	runner = glint.Runner()
	runner[None] = default_handler
	runner['test'] = test_handler
	
	assert_equal(3, len(runner._commands))
	
	assert_true(None in runner._commands)
	assert_equal(default_handler, runner._commands[None]._method)
	
	assert_true('test' in runner._commands)
	assert_equal(test_handler, runner._commands['test']._method)
	
@raises(glint.CommandExistsException)
def add_multiple_handlers_with_same_name_test():
	runner = glint.Runner()
	runner['test'] = default_handler
	runner['test'] = test_handler

# Check length
def length_test():
	runner = glint.Runner()
	assert_equal(1, len(runner))
	
	runner[None] = default_handler
	assert_equal(2, len(runner))
	
	runner['test'] = test_handler
	assert_equal(3, len(runner))

# Check contains
def contains_test():
	runner = glint.Runner()
	
	runner[None] = default_handler
	runner['test'] = test_handler
	
	assert_true('help' in runner)
	assert_true(None in runner)
	assert_true('test' in runner)

# Run default handler
def run_default_handler_test():
	handler_run = None
	
	runner = glint.Runner()
	
	runner[None] = default_handler
	runner['test'] = test_handler
	
	runner.run([])
	
	assert_true('default', handler_run)

# Run correct handler
def run_correct_handler_test():
	handler_run = None
	
	runner = glint.Runner()
	
	runner[None] = default_handler
	runner['test'] = test_handler
	
	runner.run(['test'])
	
	assert_true('test', handler_run)	

# Return none when show_usage is true
def return_none_when_show_usage_true_test():
	runner = glint.Runner()
	
	assert_is_none(runner.help())

# Return usage when show_usage is false
def return_usage_when_show_usage_is_false_test():
	runner = glint.Runner(show_usage = False)
	
	help = runner.help()
	
	assert_is_not_none(help)
	

# Exception when unable to find handler and show usage is false

# Exception when bad parameters are passed to command and show usage is false