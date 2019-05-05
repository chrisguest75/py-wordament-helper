# README.md 
A small example class for solving wordament problems.  

The words alpha has been sourced from.
[words_alpha.txt](https://github.com/dwyl/english-words/blob/master/words_alpha.txt)

# Install 

```
export PIPENV_VENV_IN_PROJECT=1
pipenv install --three
pipenv shell
```
# Setting up tests in VSCode
Use shift+cmd+p to open the command palette. 

Select Python:Configure Tests
Select the test directory

# Code Coverage
To execute code coverage on the unittests
```
pytest --cov=. --cov-report html:coverage
```

