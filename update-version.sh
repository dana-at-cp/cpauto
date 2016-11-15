#!/bin/bash

sed -i -e "s/__version__ = '.*'/__version__ = '$1'/g" cpauto/__init__.py

sed -i -e "s/__build__ = 0x[0-9]\+/__build__ = $2/g" cpauto/__init__.py

sed -i -e "s/'cpauto-CoreClient\/.*'/'cpauto-CoreClient\/$1'/g" cpauto/core/sessions.py

exit 0
