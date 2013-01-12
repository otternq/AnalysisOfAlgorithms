AnalysisOfAlgorithms
====================

Class examples from University of Idaho CS 395

Greatest Common Denominator
--------------
This module contains functions/classes to calculate the Greatest Common Denominator. Euclids method is such an algorithm.

###EuclidsMethod###
To run Euclids method navigate to `GreatestCommonDenominator` and execute the python file with two numbers as arguments
```
$ cd GreatestCommonDenominator/
$ ls
EuclidsMethod.py  EuclidsMethod.pyc	__init__.py		__init__.pyc
$ python EuclidsMethod.py 64 46
2

```

Running Tests
-------------
After `nose` is installed on your system, simply run the command `nosetests` from the main project folder

```
$ ls
GreatestCommonDenominator  setup.py  README.md  tests
$ nosetests
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK

```

Requirements
-----------

###nose###
This package is structured to use nosetests, if you do not want to run unit tests then this requirement can be skipped

####installation####
To install the nose package, use python's easy install feature, `easy_install nose` (on my Mac I had to run `sudo easy_install nose`)

Resources
-----------
- [Python Structure](http://learnpythonthehardway.org/book/ex46.html)
