Commands
========

Commands are at the heart of Glint, a command defines what code should be run given certain user input.  A command references a function
and like a python function can take various arguments. In this section we are going to walkthrough and build out the code from the quickstart 
to show how to define and use the different types of arguments a command can take.

Defining a Command
------------------

In the quick start we had a basic starting point ::

	#! /bin/env python

	import glint

	def hello():
		print('Hello world.')

	if __name__ == '__main__':
		runner = glint.Runner()
		runner['hello'] = hello
		runner.run()

The simplist way to define a command is once a ``Runner`` has been created to then assign a method to string ::

	runner['hello'] = hello

Now when the command ``./example.py hello`` is run the hello function will be executed.

Arguments
=========

Commands like the functions that they invoke can accept arguments, Glint supports three separate types of arguments: positional/required,
optional and flags. This section walks you through adding one of each type of argument to our example script above.

Positional/Required arguments
-----------------------------

Commands like the functions that they invoke can accept arguments, Glint supports three separate types of arguments the first of 
which is the position or required arguments. To define a positional argument you add a parameter to the function that the command
invokes which has no default value, in our example it would look like the following. ::

	def hello(name):
		print('Hello %s.' % name)

Now when we invoke the hello command we need to supply a value for name e.g. ``./example.py hello mike`` the string "mike" will be 
passed to the hello function in the name variable. When multiple positional arguments exist the values supplied will be assigned to 
the parameters in the order that the values are given. If the incorrect number of arguments are supplied then a error message will
be printed out to the screen.

Optional arguments
------------------

The next argument that Glint supports is the optional argument, you define an optional argument by by adding a parameter to the 
function with a default value.  In our example script we would update the hello function to look like the following. ::

	def hello(name, message = None):
		print('Hello %s.' % name)
		
		if message is not None:
			print('I want to tell you: %s' % message)

To invoke an optional argument from the command line you need to supply the optional prefix (which by default is ``--``) followed by
the name of the parameter a space and then the value. For our example script it would look like. ::

	./example.py hello mike --message "some stuff"

It doesn't matter where the optional argument is positioned they can be interspersed among the other arguments positional or otherwise.

Flags
-----

The final type of argument that Glint supports in the flag. The flag is a boolean argument it is either true or false, to define a flag 
you add a parameter to your function which has the default value of ``False`` in our example script this would look like the following. ::

	def hello(name, wave = False, message = None):
		print('Hello %s.' % name)
		
		if wave:
			print('I\'m waving at you!')
		
		if message is not None:
			print('I want to tell you: %s' % message)

To invoke a flag it is similar to an optional argument you supply the optional prefix followed by the name of the parameter, unlike the optional 
argument however there is no need to supply a value the presence of the flag is enough to tell Glint that the value should be set to true. For our
example script invoking the flag would look like. ::

	./example.py hello mike --wave

Also like the optional argument it doesn't matter where in the arguments the flag is supplied.

Final script
------------

Now we've added the different types of arguments that Glint supports our complete example script looks like: ::

	#! /bin/env python

	import glint

	def hello(name, wave = False, message = None):
		print('Hello %s.' % name)
		
		if wave:
			print('I\'m waving at you!')
		
		if message is not None:
			print('I want to tell you: %s' % message)

	if __name__ == '__main__':
		runner = glint.Runner()
		runner['hello'] = hello
		runner.run()

Special Commands
================

Within Glint there are two special commands that work differently than what has previously been
described. This section describes those special commands and how to work with them.

The None command
----------------

The ``None`` command is a special command for when no arguments are supplied to your application but rather than throwing an error you want a function
to be run. To define the None command you assign a function in the runner with the command text of ``None``, in our example script from above this would 
look like the following. ::

	#! /bin/env python

	import glint

	def hello(name, wave = False, message = None):
		print('Hello %s.' % name)
		
		if wave:
			print('I\'m waving at you!')
		
		if message is not None:
			print('I want to tell you: %s' % message)

	def default():
		print('No command has been supplied.')

	if __name__ == '__main__':
		runner = glint.Runner()
		
		runner[None] = default
		runner['hello'] = hello
		
		runner.run()

Now when the script is run and no command is supplied then the message "No command has been supplied." will be printed to the console. It is important to note
that currently the ``None`` command has the limitation that it cannot accept any arguments, if arguments are supplied then they will be ignored.

The help command
----------------

The help command is a command that has been built into Glint that prints out information regarding the available commands and their arguments to the console.
This is invoked at the command line by running ``./example.py help`` to see the list of commands that are available, to see what parameters a particular command
accepts you would run ``./example.py help --command <command name>``. We go into more depth on the help command in the :doc:`help section <help>`.

.. toctree::
	:hidden:
	
	help