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

from ._common import _CommonClient

class SimpleGateway:
    """Manage simple gateways."""

    def __init__(self, core_client):
        self.__core_client = core_client
        self.__common_client = _CommonClient(core_client)

    def add(self, name='', ip_address='', ipv4_address='', ipv6_address='', params={}):
        """Adds a simple gateway.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-simple-gateway

        :param name: A name for the new simple gateway.
        :param ip_address: (optional) IPv4 or IPv6 address. If both addresses are
            required use ipv4_address and ipv6_address fields explicitly.
        :param ipv4_address: (optional) IPv4 address.
        :param ipv6_address: (optional) IPv6 address.
        :param params: (optional) A dictionary of additional, supported
            parameter names and values.
        :rtype: CoreClientResult
        """
        payload = { 'name': name }
        if ip_address:
            payload['ip-address'] = ip_address
        if ipv4_address:
            payload['ipv4-address'] = ipv4_address
        if ipv6_address:
            payload['ipv6-address'] = ipv6_address
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('add-simple-gateway', payload=payload)

    def delete(self, name='', uid='', params={}):
        """Deletes a simple gateway.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-simple-gateway

        :param name: (optional) A simple gateway name.
        :param uid: (optional) A simple gateway unique identifier instead of name.
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-simple-gateway', name=name, uid=uid, params=params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a simple gateway with the specified name or unique
        identifier.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-simple-gateway

        :param name: (optional) A simple gateway name.
        :param uid: (optional) A simple gateway unique identifier instead of name.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-simple-gateway', name=name, uid=uid, details_level=details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing simple gateway with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-simple-gateway

        :param name: (optional) The name of an existing simple gateway.
        :param uid: (optional) The unique identifier of an existing simple gateway.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-simple-gateway', name=name, uid=uid, params=params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all simple gateways with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-simple-gateways

        :param limit: (optional) Limit the total number of simple gateways shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of simple gateways in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-simple-gateways', limit=limit,
            offset=offset, order=order, details_level=details_level)
