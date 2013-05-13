from nose.tools import *
from glint.utils import *

def test_is_none_or_empty_none():
	assert_true(is_none_or_empty(None))

def test_is_none_or_empty_empty_string():
	assert_true(is_none_or_empty(''))

def test_is_none_or_empty_empty_list():
	assert_true(is_none_or_empty([]))

def test_is_none_or_empty_string():
	assert_false(is_none_or_empty('qwerty'))

def test_is_none_or_empty_whitespace_string():
	assert_false(is_none_or_empty(' '))

def test_is_none_or_empty_populated_list():
	assert_false(is_none_or_empty([1, 2]))

# is_none_or_whitespace

def test_is_none_or_whitespace_space_string():
	assert_true(is_none_or_whitespace(' '))

def test_is_none_or_whitespace_tab_string():
	assert_true(is_none_or_whitespace('\t'))

def test_is_none_or_whitespace_newline_string():
	assert_true(is_none_or_whitespace('\n'))

def test_is_none_or_whitespace_multi_string():
	assert_true(is_none_or_whitespace(' \t\n'))

def test_is_none_or_whitespace_populated_string():
	assert_false(is_none_or_whitespace('qwerty'))