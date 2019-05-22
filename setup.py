from distutils.core import setup

setup(
    name='py-wordament-helper',
    version='0.1.2',
    author='Chris Guest',
    author_email='chris@chrisguest.dev',
    packages=['py_wordament_helper', 'test'],
    scripts=[],
    url='https://github.com/chrisguest75/py-wordament-helper',
    license='LICENSE.txt',
    description='A package for solving simple Wordament problems.',
    long_description=open('README.md').read(),
    install_requires=[
    ],
)
