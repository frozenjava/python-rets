import os
from setuptools import setup

# Set external files
try:
    from pypandoc import convert
    README = convert('README.md', 'rst')
except ImportError:
    README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

with open(os.path.join(os.path.dirname(__file__), 'requirements.txt')) as f:
    required = f.read().splitlines()

with open(os.path.join(os.path.dirname(__file__), 'test_requirements.txt')) as f:
    test_required = f.read().splitlines()

version = {}
with open("rets/_version.py") as fp:
    exec(fp.read(), version)

setup(
    name='rets',
    version=version['__version__'],
    packages=['rets'],
    install_requires=required,
    tests_require=test_required,
    test_suite='nose.collector',
    include_package_data=True,
    license='MIT License',
    description='RETS Client for Real Estate Data',
    long_description=README,
    url='https://github.com/refindlyllc/python-rets',
    author='REfindly',
    author_email='info@refindly.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
