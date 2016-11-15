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

# cpauto.objects.policy
# ~~~~~~~~~~~~~~~~~~~~~

"""This module contains the classes needed to manage policy objects."""

from ._common import _CommonClient

class Policy:
    """Manage policy."""

    def __init__(self, core_client):
        self.__core_client = core_client

    def install(self, access=True, threat=True, policy_package='', targets=''):
        """Installs the specified policy package or the standard policy package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/install-policy

        :param access: (optional) Install access policy. Default is true.
        :param threat: (optional) Install threat prevention policy. Default is true.
        :param policy_package: (optional) Install specific policy package. Default is standard.
        :type policy_package: string
        :param targets: (optional) Policy install targets.
        :type targets: string or list of strings
        :rtype: CoreClientResult
        """
        payload = { 'access': access, 'threat-prevention': threat }
        if policy_package:
            payload['policy-package'] = policy_package
        if targets:
            payload['targets'] = targets
        return self.__core_client.http_post('install-policy', payload=payload)

class PolicyPackage:
    """Manage policy packages."""

    def __init__(self, core_client):
        self.__core_client = core_client
        self.__common_client = _CommonClient(core_client)

    def add(self, name='', params={}):
        """Adds a new policy package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-package

        :param name: The name of the new policy package.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        payload = { 'name': name }
        if params:
            payload = self.__core_client.merge_payloads(payload, params)
        return self.__core_client.http_post('add-package', payload=payload)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a policy package with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-package

        :param name: (optional) The name of an existing policy package.
        :param uid: (optional) The unique identifier of an existing policy package.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-package', name=name, uid=uid, details_level=details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing policy package with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-package

        :param name: (optional) The name of an existing policy package.
        :param uid: (optional) The unique identifier of an existing policy package.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-package', name=name, uid=uid, params=params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing policy package with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-package

        :param name: (optional) The name of an existing policy package.
        :param uid: (optional) The unique identifier of an existing policy package.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-package', name=name, uid=uid, params=params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all policy packages with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-packages

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
        return self.__common_client._show_all('show-packages', limit=limit,
            offset=offset, order=order, details_level=details_level)
