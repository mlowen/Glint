# Glint
[![Build Status](https://travis-ci.org/mlowen/Glint.png?branch=master)](https://travis-ci.org/mlowen/Glint)

Glint is a micro framework for command line applications, it creates the needed parameters that should be passed to the application based on the function signatures that it is supplied.

### Inspiration

The inspiration for Glint came from wanting to have a command driven cli app similar to how git works which I was unable to replicate with [argparse](http://docs.python.org/dev/library/argparse.html).

## Requirements

Glint requires Python 3.3 or higher to run, it has no other dependencies outside of the python core library.

## Installation

To install Glint once you have a copy run from the projects root directory:

```
python ./setup.py install
```

## Usage

All usage documentation for Glint can be found over at [read the docs](https://glint.readthedocs.org/). 

## Future Plans

If you want to see what's coming up in the near future for Glint go visit the [huboard](http://huboard.com/mlowen/Glint/board) for the project.

## Contributing

The source for Glint can be found over at [Github](https://github.com/mlowen/Glint), if you want to contribute that would be a good place to start. If you are wanting to report a bug all of that is kept at github as well in the [issue tracker](https://github.com/mlowen/Glint/issues), the issues are also used to track upcoming work on Glint though features/issues that will be worked on before the next release can be more easily visualised over at [huboard](http://huboard.com/mlowen/Glint/board).  If you want to keep a track of the status of the bleeding edge then you'll able to see the current state at [Travis](https://travis-ci.org/mlowen/Glint).

### Submitting changes

You've downloaded/cloned Glint and made some changes you'd like to have merged in, firstly awesome thanks hugely! There are a couple of guidelines around submitting changes:

* Changes will only be accepted via pull requests on github.
* Any code changes should have some unit tests, if it's a fix for a bug it won't be accepted unless it has tests.
* Again with any code changes if your pull request [breaks the build](https://travis-ci.org/mlowen/Glint/pull_requests) it won't be accepted.

### Running the tests

While Glint doesn't have any dependencies outside of the python core library you will need to install [nose](https://nose.readthedocs.org/en/latest/) to run the tests. Once that is installed you have two options for running the test you can run either:

```
nostests
``` 
or
```
python ./setup.py test
```

## License

Glint is available under the MIT license which is as follows:

Copyright © 2013 Michael Lowen

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.