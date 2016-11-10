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

# cpauto.objects.network
# ~~~~~~~~~~~~~~~~~~~~~~

"""This module contains the classes needed to manage network objects."""

class NetworkClient:
    def __init__(self, core_client):
        self.__core_client = core_client

    def add(self, name, params={}):
        """Adds a network. Returns CoreClientResult object.

        :param name: A name for the new network.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/add-network
        payload = { 'name': name }
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('add-network', payload=payload)

    def show(self, name=None, uid=None, details_level=None):
        """Shows details of a network with the specified name
        or uid. Returns a CoreClientResult object.

        :param name: (optional) The name of an existing network.
        :param uid: (optional) The unique identifier of an existing network.
        :param details_level: (optional) The level of detail to show. Default
        value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/show-network
        payload = {}
        if name is not None:
            payload['name'] = name
        if uid is not None:
            payload['uid'] = uid
        if details_level is not None:
            payload['details-level'] = details_level
        return self.__core_client.http_post('show-network', payload=payload)

    def set(self, name=None, uid=None, params={}):
        """Sets new values for an existing network with the specified
        name or uid. Returns a CoreClientResult object.

        :param name: (optional) The name of an existing network.
        :param uid: (optional) The unique identifier of an existing network.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/set-network
        payload = {}
        if name is not None:
            payload['name'] = name
        if uid is not None:
            payload['uid'] = uid
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('set-network', payload=payload)

    def delete(self, name=None, uid=None, params={}):
        """Deletes an existing network with the specified
        name or uid. Returns a CoreClientResult object.

        :param name: (optional) The name of an existing network.
        :param uid: (optional) The unique identifier of an existing network.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-network
        payload = {}
        if name is not None:
            payload['name'] = name
        if uid is not None:
            payload['uid'] = uid
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('delete-network', payload=payload)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all networks with some reasonable limitations. Returns
        a CoreClientResult object.

        :param limit: (optional) Limit the total number of networks shown.
        The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of networks in the results
        before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
        default is a random order.
        :param details_level: (optional) The level of detail to show. Default
        value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/show-networks
        payload = { 'limit': limit, 'offset': offset }
        if order:
            payload['order'] = order
        if details_level:
            payload['details-level'] = details_level
        return self.__core_client.http_post('show-networks', payload=payload)
