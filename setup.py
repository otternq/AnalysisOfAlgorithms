try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    description='A package containing class examples from University of Idaho CS 395',
    author='Nicholas Otter',
    url='http://github.com/otternq/AnalysisOfAlgorithms',
    author_email='otte8229@vandals.uidaho.edu',
    version='0.1',
    packages=['GreatestCommonDenominator'],
    scripts=[],
    name='AnalysisOfAlgorithms',
    install_requires=['nose', 'coverage'],
    tests_require=['nose'],
    test_suite="nose.collector"
)
