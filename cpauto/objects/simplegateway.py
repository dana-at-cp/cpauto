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

# cpauto.objects.simplegateway
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""This module contains the classes needed to manage simple gateway objects."""

class SimpleGatewayClient:
    def __init__(self, core_client):
        self.__core_client = core_client

    def add(self, name, ip_address=None, ipv4_address=None, ipv6_address=None, params={}):
        """Adds a simple gateway. Returns CoreClientResult object.

        :param name: A name for the new simple gateway.
        :param ip_address: IPv4 or IPv6 address. If both addresses are required use ipv4_address and ipv6_address fields explicitly.
        :param ipv4_address: (optional) IPv4 address.
        :param ipv6_address: (optional) IPv6 address.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: cpauto.core.sessions.CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/add-simple-gateway
        payload = { 'name': name }
        if ip_address is not None:
            payload['ip-address'] = ip_address
        if ipv4_address is not None:
            payload['ipv4-address'] = ipv4_address
        if ipv6_address is not None:
            payload['ipv6-address'] = ipv6_address
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('add-simple-gateway', payload=payload)

    def delete(self, name=None, uid=None):
        """Deletes a simple gateway. Returns CoreClientResult object.

        :param name: A simple gateway name.
        :param uid: (optional) A simple gateway unique identifier instead of name.
        :rtype: cpauto.core.sessions.CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-simple-gateway
        payload = {}
        if uid is not None:
            payload = { 'uid': uid }
        if name is not None:
            payload = { 'name': name }
        return self.__core_client.http_post('delete-simple-gateway', payload=payload)
