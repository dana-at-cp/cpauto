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

# cpauto.objects.common
# ~~~~~~~~~~~~~~~~~~~~~

"""This module provides common bits needed to manage objects."""

class _CommonClient:
    def __init__(self, core_client):
        self.__core_client = core_client

    def _show(self, endpoint, name='', uid='', details_level=''):
        payload = {}
        if name:
            payload['name'] = name
        if uid:
            payload['uid'] = uid
        if details_level:
            payload['details-level'] = details_level
        return self.__core_client.http_post(endpoint, payload=payload)

    def _set(self, endpoint, name='', uid='', params={}):
        payload = {}
        if name:
            payload['name'] = name
        if uid:
            payload['uid'] = uid
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post(endpoint, payload=payload)

    def _delete(self, endpoint, name='', uid='', params={}):
        payload = {}
        if name:
            payload['name'] = name
        if uid:
            payload['uid'] = uid
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post(endpoint, payload=payload)

    def _show_all(self, endpoint, limit=50, offset=0, order=[], details_level=''):
        payload = { 'limit': limit, 'offset': offset }
        if order:
            payload['order'] = order
        if details_level:
            payload['details-level'] = details_level
        return self.__core_client.http_post(endpoint, payload=payload)
