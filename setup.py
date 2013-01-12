try:
    from setuptools import setup
exept ImportError:
    from distutils.core import setup

config = {
    'description': 'A package containing class examples from University of Idaho CS 395',
    'author': 'Nicholas Otter',
    'url': 'http://github.com/otternq/AnalysisOfAlgorithms',
    'download_url': 'Where to download it.',
    'author_email': 'otte8229@vandals.uidaho.edu',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['GreatestCommonDenominator'],
    'scripts': [],
    'name': 'AnalysisOfAlgorithms'
}