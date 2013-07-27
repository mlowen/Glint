Introduction
============

Glint is a micro-framework for for providing command like functionality to a python command line application. Glint allows an
application to accept command line arguments in the following fashion: ::

	app.py <command> required_arg --optional_arg value --flag

Inspiration
-----------

The inspiration for Glint came from wanting to have a command driven CLI appliation similar to how git works which I was unable 
to replicate with `argparse <http://docs.python.org/dev/library/argparse.html>`_.

Installation
------------

Glint requires Python 3.3 or higher to work, once you have downloaded the latest version from the `release page at GitHub <https://github.com/mlowen/Glint/releases>`_ 
you need to run the following command from the base directory: ::

	python setup.py install

At some point we will be submitting to `the Python Package Index <https://pypi.python.org/pypi>`_ once that is done then it will be the preferred 
method to retreive and install Glint.

Quick start
===========

The smallest working example is the example.py script below ::

	#! /bin/env python

	import glint

	def hello():
		print('Hello world.')

	if __name__ == '__main__':
		runner = glint.Runner()
		runner['hello'] = hello
		runner.run()

This script provides you with two commands: the built in help command and the hello command which was defined in the script.  The built in help command will output 
information that it has about the available commands that can be run, to view the help you would run the following command ``./example.py help`` which would produce output that looks like ::

	usage: ./example.py <command>

	Commands:

	  help    Show this message and exit
	  hello

	See './example.py help --command <command>' for help on that command.

Running the hello command that is defined in the example looks like ``./example.py hello`` which produces the following expected output ::

	Hello World.

For a more comprehensive look see the usage page.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. toctree::
	:hidden:
	
	commands