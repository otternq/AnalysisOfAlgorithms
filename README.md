Analysis Of Algorithms
====================

Implementation of algorithms discussed in CS/MATH 395 along with unit tests and scripts.

Unit Tests are ran at [TravisCI](https://travis-ci.org/otternq/AnalysisOfAlgorithms/)

Project Status
-----------
| Master | Development |
| ------ | ----------- |
| [![Build Status](https://travis-ci.org/otternq/AnalysisOfAlgorithms.png?branch=master)](https://travis-ci.org/otternq/AnalysisOfAlgorithms) | [![Build Status](https://travis-ci.org/otternq/AnalysisOfAlgorithms.png?branch=development)](https://travis-ci.org/otternq/AnalysisOfAlgorithms) |

CS/MATH 395
--------
University of Idaho CS/MATH 395 (Spring 2013)

[Class Website](http://marvin.cs.uidaho.edu/Teaching/CS395/index.html)


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
Euclids Method Mod: 
2
Euclids Method Minus: 
2
Euclids Method Mod Min: 
2
$ python EuclidsMethod.py 55 22
Euclids Method Mod: 
11
Euclids Method Minus: 
11
Euclids Method Mod Min: 
11

```

Running Tests
-------------
After `nose` is installed on your system, simply run the command `nosetests` from the main project folder

```
$ ls
GreatestCommonDenominator  setup.py  README.md  tests
$ nosetests
........
----------------------------------------------------------------------
Ran 8 tests in 0.015s

OK

```

Requirements
-----------

###nose###
This package is structured to use nosetests, if you do not want to run unit tests then this requirement can be skipped

####installation####
To install the nose package, use python's easy install feature, `easy_install nose` (on my Mac I had to run `sudo easy_install nose`)

Platform
---------
Language: Python

###Developed on###
- <b>Operating System</b>: Mac OS X
- <b>Python Version</b>: Python 2.7.2 and Python 3.3

Resources
-----------
- [Python Structure](http://learnpythonthehardway.org/book/ex46.html)
