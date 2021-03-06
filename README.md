# README.md 
[![image](https://img.shields.io/github/license/chrisguest75/py-wordament-helper.svg)](https://img.shields.io/github/license/chrisguest75/py-wordament-helper.svg) [![image](https://img.shields.io/travis/com/chrisguest75/py-wordament-helper.svg)](https://img.shields.io/travis/com/chrisguest75/py-wordament-helper.svg) [![image](https://img.shields.io/codecov/c/gh/chrisguest75/py-wordament-helper.svg)](https://img.shields.io/codecov/c/gh/chrisguest75/py-wordament-helper.svg)


A package for solving simple Wordament problems.  
The purpose is to have some code tha I use to solve real world deployment challenges.

* For a full dictionary it seems to take up 400MiB of heap space.
* There are two interfaces - the dictionary trie and a board solver that uses the trie. 
* The suite of unittests are coverage enabled.
* It can be used as a github protocol package by being referenced directly from here.
* Travis is configured of the build and codecov.io is used for coverage reporting
* Badges are generated at shield.io (the ecosystem that exists is great)
* The code is not meant to be super optimal - for its purpose all the better that it isn't.

# How it works
You build a dictionary trie structure full of words.  The trie is efficient for search. Each node in the trie has a marker to mark a legimate word. 

Once the dictionary is built, you pass a string representation of the 4x4 grid and the solver will do a depth first search tracking through the trie - in an innefficient way.  An improvement would be to use the visitor pattern.  Each legal word found is added to the output.  The board is marked each time on the stack to prevent double usage of letters.  

The example words alpha have been sourced from.
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
./examples/main.py is an example of how to use the interface.
If in the pipenv environment you can run ./examples/main.py from inside the examples directory.  

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

# Complexity and Maintainabiity metrics
Use radon to return code complexity and maintainability metrics. 
```
radon cc ./
radon mi ./
radon hal ./
```
# Building package for distribution

```
python3 setup.py sdist
```