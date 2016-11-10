"""Converts README.md to README.rst using pandoc."""

from codecs import open

import pandoc
import sys

pandoc.core.PANDOC_PATH = '/usr/bin/pandoc'

doc = pandoc.Document()

with open('README.md', 'r', 'utf-8') as f:
    doc.markdown = f.read()

with open('README.rst', 'w', 'utf-8') as f:
    f.write(doc.rst)

sys.exit(0)
