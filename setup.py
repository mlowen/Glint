import glint

from setuptools import setup, find_packages

setup(
	name = glint.__name__,
	version = glint.__version__,
	description = glint.__description__,
	long_description = glint.__description__,
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Operating System :: OS Independent',
		'License :: OSI Approved :: MIT License',
		'Environment :: Console',
		'Programming Language :: Python :: 3.3',
		'Topic :: Software Development :: Libraries :: Application Frameworks'
	],
	author = glint.__author__,
	author_email = glint.__author_email__,
	url = glint.__homepage__,
	license = glint.__license__,
	packages = find_packages(exclude = [ 'tests', 'examples' ]),
	test_suite = 'nose.collector',
	tests_require = [ 'nose' ],
	zip_safe = False,
	extras_require = {
		'testing': [ 'nose' ]
	}
)