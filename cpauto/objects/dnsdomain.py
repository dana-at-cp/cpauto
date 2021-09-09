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

# cpauto.objects.dnsdomain
# ~~~~~~~~~~~~~~~~~~~

"""This module contains the classes needed to manage dns-domain objects."""

from ._common import _CommonClient


class DNSDomain:
    """Manage dns-domains."""

    def __init__(self, core_client):
        self.__core_client = core_client
        self.__common_client = _CommonClient(core_client)

    def add(self, name='', is_sub_domain=False, params={}):
        """Adds a dns-domain.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-dns-domain

        :param name: DNS domain name. Should always start with a '.' character. Should be unique in the domain.
        :param is_sub_domain: Whether to match sub-domains in addition to the domain itself.
        :param params: (optional) A dictionary of additional, supported
            parameter names and values.
        :rtype: CoreClientResult
        """
        payload = {
            'name': name,
            'is-sub-domain': is_sub_domain
        }

        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('add-dns-domain', payload=payload)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a dns-domain with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-dns-domain

        :param name: (optional) The name of an existing dns-domain.
        :param uid: (optional) The unique identifier of an existing dns-domain.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-dns-domain', name=name, uid=uid, details_level=details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing dns-domain with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-dns-domain

        :param name: (optional) The name of an existing dns-domain.
        :param uid: (optional) The unique identifier of an existing dns-domain.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-dns-domain', name=name, uid=uid, params=params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing dns-domain with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-dns-domain

        :param name: (optional) The name of an existing dns-domain.
        :param uid: (optional) The unique identifier of an existing dns-domain.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-dns-domain', name=name, uid=uid, params=params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all dns-domains with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-dns-domains

        :param limit: (optional) Limit the total number of dns-domains shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of dns-domains in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-dns-domains', limit=limit,
            offset=offset, order=order, details_level=details_level)
