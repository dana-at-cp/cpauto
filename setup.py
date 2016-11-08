"""Setup script for cpauto."""

from __future__ import print_function
from setuptools import setup
from setuptools.command.test import test as TestCommand
import codecs
import os
import sys
import re

HERE = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """Return multiple read calls to different readable objects as a single
    string."""
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(HERE, *parts), 'r').read()

LONG_DESCRIPTION = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = [
            '--strict',
            '--verbose',
            '--tb=long',
            'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='cpauto',
    version='0.0.1',
    url='https://github.com/dana-at-cp/cpauto',
    license='Apache Software License',
    author='Dana James Traversie',
    tests_require=['pytest', 'pytest-cov'],
    install_requires=[
        'requests>=2.11.1',
        ],
    cmdclass={'test': PyTest},
    author_email='dtravers@checkpoint.com',
    description='Python client for Check Point R80 management server web APIs',
    long_description=LONG_DESCRIPTION,
    packages=['cpauto', 'cpauto.core', 'cpauto.objects' ],
    package_dir={'cpauto': 'cpauto'},
    include_package_data=True,
    platforms='any',
    test_suite='tests.test_cpauto',
    zip_safe=False,
    package_data={'': ['LICENSE', 'NOTICE']},
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)
