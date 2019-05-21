# README.md 
[![image](https://img.shields.io/github/license/chrisguest75/py-wordament-helper.svg)](https://img.shields.io/github/license/chrisguest75/py-wordament-helper.svg) [![image](https://img.shields.io/travis/com/chrisguest75/py-wordament-helper.svg)](https://img.shields.io/travis/com/chrisguest75/py-wordament-helper.svg) [![image](https://img.shields.io/codecov/c/gh/chrisguest75/py-wordament-helper.svg)](https://img.shields.io/codecov/c/gh/chrisguest75/py-wordament-helper.svg)


A small example class for solving wordament problems.  

The words alpha has been sourced from.
[words_alpha.txt](https://github.com/dwyl/english-words/blob/master/words_alpha.txt)

# Install 
To install locally you can clone the repo
```
export PIPENV_VENV_IN_PROJECT=1
pipenv install --three
pipenv shell
```

To install as part of a project
```
pipenv install git+https://github.com/chrisguest75/py-wordament-helper#egg=py-wordament-helper
```

# Example
./main.py is an example of how to use the interface.
You can run ./main.py from the root.  

# Setting up tests in VSCode
Use shift+cmd+p to open the command palette. 

Select Python:Configure Tests
Select the test directory

# Code Coverage
To execute code coverage on the unittests
```
pytest --cov=. --cov-report html:coverage
open ./coverage/index.html
```


