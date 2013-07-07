API - glint
###########

.. py:module:: glint

.. py:class:: Runner[([description = None[, show_usage = True[, prefix = '--']]])]

	The Runner class is the core of the Glint framework it handles the routing of the commands to the correct methods.

	:param description: A string describing the application which will be printed out when the help command is run.
	:type description: string or None
	:param show_usage: A flag to specify whether to add the help command.
	:type show_usage: bool
	:param prefix: The prefix used to identify optional arguments and flags.
	:type prefix: string

	.. describe:: r[key] = value

		Assigns a method to be run when the command matches ``key``, value can be one of two things:

		* A function,
		* A tuple containing a function and a description to be displayed when the help command is run.

	.. describe:: len(r)

		Returns the number of commands in the runner.

	.. describe:: key in r

		Returns if the current runner contains a command which matches ``key``

	.. py:method:: Runner.run([args = None])

		This method parses the arguments which are passed to it and runs the appropriate command.  If the ``args`` parameter is ``None``
		then ``run`` will use ``sys.argv``.

		:param args: The arguments used to determine what command to run.
		:type args: List or None

	.. py:method:: Runner.help([command = None])

		This method returns a list of strings which contains help information.  If the ``show_usage`` flag is true then this information
		will first be printed to stdout.  If the ``command`` argument is not none then it will return help information specific to that 
		command.

		:param command: The command to retrieve help information about.
		:type command: string or None
		:rtype: list of strings.