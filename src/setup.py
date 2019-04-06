from setuptools import setup, find_packages

import pytspsolver

URL = 'https://github.com/rithinch/pytspsolver'
REQUIRES_PYTHON = ">=3.6.0"
REQUIRED_PKGS = ["numpy", "matplotlib", "networkx", "tsplib95"]
AUTHOR = 'Rithin Chalumuri'
AUTHOR_EMAIL = 'rithinch@gmail.com'
KEYWORDS = ['tsp', 'optimization-experiments', 'python']
DESCRIPTION = 'Python package for rapid experimentation on travelling salesman problem'

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Travelling Salesman Problem :: Experimentation Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.6',
  ]

setup (
        name = pytspsolver.__name__,
        version = pytspsolver.__version__,
        python_requires=REQUIRES_PYTHON,
        packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
        install_requires = REQUIRED_PKGS,
        license='MIT',
        author=AUTHOR,
        url = URL,
        keywords = KEYWORDS,
        description= DESCRIPTION
)