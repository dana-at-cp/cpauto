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

# cpauto.objects.access
# ~~~~~~~~~~~~~~~~~~~~~

"""This module contains the classes needed to manage access control and NAT objects."""

class AccessRule:
    """Manage access rules."""

    def __init__(self, core_client):
        self.__core_client = core_client

    def add(self, layer="", position="", params={}):
        """Adds an access rule.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-access-rule

        :param layer: Layer that the rule belongs to identified by name or UID.
        :param position: Position in the rulebase. Can be specified in various ways.
        :type position: integer, string or dict (e.g. 1, 'top', 'bottom', or "{ 'above': 'Section One' }")
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        payload = { 'layer': layer, 'position': position }
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('add-access-rule', payload=payload)
