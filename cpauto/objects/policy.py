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

"""
cpauto.objects.policy
~~~~~~~~~~~~~~~~~~~~~

This module contains the classes needed to manage policy objects.

"""

from .exceptions import PolicyClientError

import json

class PolicyClient:
    def __init__(self, core_client):
        self.__core_client = core_client

    def install(self, access=True, threat=True, policy_package=None, targets=None):
        payload = {}
        if access:
            payload['access'] = 'True'
        if threat:
            payload['threat-prevention'] = 'True'
        if policy_package is not None:
            payload['policy-package'] = policy_package
        if targets is not None:
            payload['targets'] = json.dumps(targets)
        return self.__core_client.http_post('install-policy', payload=payload)

    def add_package(self, name, params={}):
        payload = { 'name': name }
        payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('add-package', payload=payload)
