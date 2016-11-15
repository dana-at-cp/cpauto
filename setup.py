"""Setup script for cpauto."""

from setuptools import setup
from setuptools.command.test import test as TestCommand

from codecs import open

import re
import sys

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

with open('cpauto/__init__.py', 'r') as fd:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
                        fd.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Failed to find version number')

with open('README.rst', 'r', 'utf-8') as f:
    readme = f.read()

with open('HISTORY.rst', 'r', 'utf-8') as f:
    history = f.read()

long_description = readme + '\n\n' + history

setup(
    name='cpauto',
    version=version,
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
    long_description=long_description,
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
