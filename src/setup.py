from setuptools import setup, find_packages
import os
import pytspsolver
import io

URL = 'https://github.com/rithinch/pytspsolver'
REQUIRES_PYTHON = ">=3.6.0"
REQUIRED_PKGS = ["numpy", "matplotlib", "networkx", "tsplib95"]
AUTHOR = 'Rithin Chalumuri'
AUTHOR_EMAIL = 'rithinch@gmail.com'
KEYWORDS = ['tsp', 'optimization-experiments', 'python']
DESCRIPTION = 'Easy to use python package for rapid experimentation on the classic travelling salesman problem.'

CLASSIFIERS = [
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Travelling Salesman Problem :: Experimentation Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.6',
  ]


here = os.path.abspath(os.path.dirname(__file__))

# Import the README and use it as the long-description.
# Note: this will only work if 'README.md' is present in your MANIFEST.in file!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION


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
        description= DESCRIPTION,
        long_description=long_description,
        long_description_content_type='text/markdown'
)