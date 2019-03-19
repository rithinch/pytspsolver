from setuptools import setup, find_packages

import pytspsolver

URL = 'https://github.com/rithinch/pytspsolver'
REQUIRES_PYTHON = ">=3.6.0"
REQUIRED_PKGS = ["numpy", "matplotlib", "networkx"]
AUTHOR = 'Rithin Chalumuri'
AUTHOR_EMAIL = 'rithinch@gmail.com'

setup (
        name = pytspsolver.__name__,
        version = pytspsolver.__version__,
        python_requires=REQUIRES_PYTHON,
        packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
        install_requires = REQUIRED_PKGS,
        license='MIT',
        author=AUTHOR
)