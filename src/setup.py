from setuptools import setup

import pytspsolver

setup (
        name = pytspsolver.__name__,
        version = pytspsolver.__version__,
        packages = [ 'pytspsolver','pytspsolver/entities','pytspsolver/solvers', 'pytspsolver/utilities']
)