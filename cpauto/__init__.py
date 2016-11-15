# -*- coding: utf-8 -*-

# Copyright 2016 Dana James Traversie and Check Point Software Technologies, Ltd. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#
#  __   __   __        _|_
# (___ |__) (__( (__(_  |_, (__)
#      |
#

# cpauto library
# ~~~~~~~~~~~~~~

"""cpauto is a client library, written in Python, for the web APIs exposed
via Check Point R80 management server software. The Check Point R80 management
APIs provide automation and integration capabilities that were not available
in previous versions of Check Point management server software.

https://sc1.checkpoint.com/documents/R80/APIs/#introduction

usage:

>>> import cpauto
>>> cc = cpauto.CoreClient('admin', 'vpn123', '10.6.9.81', verify=False)
>>> r = cc.login()
>>> print(r.status_code)
200
>>> print(r.json())
{u'last-login-was-at': {u'posix': 1478636363481, u'iso-8601': u'2016-11-08T15:19-0500'}, u'uid': ...}
>>> n = cpauto.Network(cc)
>>> r = n.add('net_mgmt', { 'subnet': '10.6.9.0', 'subnet-mask': '255.255.255.0' })
>>> print(r.status_code)
200
>>> print(r.json())
{u'domain': {u'domain-type': u'domain', u'name': u'SMC User', u'uid': u'41e821a0-3720-11e3-aa6e-0800200c9fde'}, ...}
>>> r = cc.publish()
>>> print(r.status_code)
200
>>> print(r.json())
{u'task-id': u'01234567-89ab-cdef-8b0a-92e9635a47d3'}
>>> r = cc.logout()
>>> print(r.status_code)
200
>>> print(r.json())
{u'message': u'OK'}

:copyright: (c) 2016 by Dana James Traversie and Check Point Software Technologies, Ltd.
:license: Apache 2.0, see LICENSE for more details.
"""

__title__ = 'cpauto'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'Dana James Traversie'
__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2016 Dana James Traversie and Check Point Software Technologies, Ltd.'

from .core.sessions import CoreClientResult, CoreClient
from .core.exceptions import (
    CoreClientError,
    ConnectionError,
    HTTPError,
    SSLError,
    Timeout,
    TooManyRedirects,
    InvalidURL
)

from .objects.access import AccessRule
from .objects.group import Group
from .objects.host import Host
from .objects.network import Network
from .objects.policy import Policy, PolicyPackage
from .objects.simplegateway import SimpleGateway
