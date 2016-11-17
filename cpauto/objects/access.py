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

from ._common import _CommonClient

def _ar_as_add(cc, endpoint="", layer="", position="", params={}):
    payload = { 'layer': layer, 'position': position }
    if params:
        payload = cc.merge_payloads(payload, params)
    return cc.http_post(endpoint, payload=payload)

def _ar_as_post(cc, endpoint='', layer='', name='', uid='', params={}):
    payload = { 'layer': layer }
    if name:
        payload['name'] = name
    if uid:
        payload['uid'] = uid
    if params:
        payload = cc.merge_payloads(payload, params)
    return cc.http_post(endpoint, payload=payload)

class AccessRule:
    """Manage access rules."""

    def __init__(self, core_client):
        self.__cc = core_client

    def add(self, layer="", position="", params={}):
        """Adds an access rule within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-access-rule

        :param layer: Layer that the rule belongs to identified by name or UID.
        :param position: Position in the rulebase. Can be specified in various ways.
        :type position: integer, string or dict (e.g. 1, 'top', 'bottom', or "{ 'above': 'Section One' }")
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return _ar_as_add(self.__cc, 'add-access-rule', layer, position, params)

    def show(self, layer='', name='', uid='', params={}):
        """Shows details of an access rule within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-access-rule

        :param layer: Layer that the rule belongs to identified by name or UID.
        :param name: (optional) The name of an existing access rule.
        :param uid: (optional) The unique identifier of an existing access rule.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return _ar_as_post(self.__cc, 'show-access-rule', layer, name, uid, params)

    def set(self, layer='', name='', uid='', params={}):
        """Sets new values for an access rule within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-access-rule

        :param layer: Layer that the rule belongs to identified by name or UID.
        :param name: (optional) The name of an existing access rule.
        :param uid: (optional) The unique identifier of an existing access rule.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return _ar_as_post(self.__cc, 'set-access-rule', layer, name, uid, params)

    def delete(self, layer='', name='', uid='', params={}):
        """Deletes an existing access rule within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-access-rule

        :param layer: Layer that the rule belongs to identified by name or UID.
        :param name: (optional) The name of an existing access rule.
        :param uid: (optional) The unique identifier of an existing access rule.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return _ar_as_post(self.__cc, 'delete-access-rule', layer, name, uid, params)

    def show_all(self, name='', params={}):
        """Shows all access rules within a layer, section, etc.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-access-rulebase

        :param name: The name of an existing access layer, section, etc.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        payload = { 'name': name }
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post('show-access-rulebase', payload=payload)

class AccessSection:
    """Manage access sections."""

    def __init__(self, core_client):
        self.__cc = core_client

    def add(self, layer="", position="", params={}):
        """Adds an access section within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-access-section

        :param layer: Layer that the section belongs to identified by name or UID.
        :param position: Position in the rulebase. Can be specified in various ways.
        :type position: integer, string or dict (e.g. 1, 'top', 'bottom', or "{ 'above': 'Section One' }")
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return _ar_as_add(self.__cc, 'add-access-section', layer, position, params)

    def show(self, layer='', name='', uid='', params={}):
        """Shows details of an access section within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-access-section

        :param layer: Layer that the section belongs to identified by name or UID.
        :param name: (optional) The name of an existing access section.
        :param uid: (optional) The unique identifier of an existing access section.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return _ar_as_post(self.__cc, 'show-access-section', layer, name, uid, params)

    def set(self, layer='', name='', uid='', params={}):
        """Sets new values for an access section within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-access-section

        :param layer: Layer that the section belongs to identified by name or UID.
        :param name: (optional) The name of an existing access section.
        :param uid: (optional) The unique identifier of an existing access section.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return _ar_as_post(self.__cc, 'set-access-section', layer, name, uid, params)

    def delete(self, layer='', name='', uid='', params={}):
        """Deletes an existing access section within a layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-access-section

        :param layer: Layer that the section belongs to identified by name or UID.
        :param name: (optional) The name of an existing access section.
        :param uid: (optional) The unique identifier of an existing access section.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return _ar_as_post(self.__cc, 'delete-access-section', layer, name, uid, params)

class AccessLayer:
    """Manage access layers."""

    def __init__(self, core_client):
        self.__cc = core_client
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", params={}):
        """Adds an access layer.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-access-layer

        :param name: A name for the new access layer..
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        payload = { 'name': name }
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post('add-access-layer', payload=payload)

    def show(self, name='', uid='', details_level=''):
        """Shows details of an access layer with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-access-layer

        :param name: (optional) The name of an existing host.
        :param uid: (optional) The unique identifier of an existing access layer.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-access-layer', name=name, uid=uid, details_level=details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing access layer with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-access-layer

        :param name: (optional) The name of an existing access layer.
        :param uid: (optional) The unique identifier of an existing access layer.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-access-layer', name=name, uid=uid, params=params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing access layer with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-access-layer

        :param name: (optional) The name of an existing access layer.
        :param uid: (optional) The unique identifier of an existing access layer.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-access-layer', name=name, uid=uid, params=params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all hosts with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-access-layers

        :param limit: (optional) Limit the total number of access layers shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of access layers in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-access-layers', limit=limit,
            offset=offset, order=order, details_level=details_level)

class NATRule:
    """Manage NAT rules."""

    def __init__(self, core_client):
        self.__cc = core_client

    def __post(self, endpoint, package="", uid="", params={}):
        payload = { 'package': package }
        if uid:
            payload['uid'] = uid
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post(endpoint, payload=payload)

    def add(self, package="", position="", params={}):
        """Adds a NAT rule.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-nat-rule

        :param package: Package that the rule belongs to identified by name.
        :param position: Position in the rulebase. Can be specified in various ways.
        :type position: integer, string or dict (e.g. 1, 'top', 'bottom', or "{ 'above': 'Section One' }")
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        payload = { 'package': package, 'position': position }
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post('add-nat-rule', payload=payload)

    def show(self, package="", uid="", params={}):
        """Shows details of a NAT rule within a package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-nat-rule

        :param package: Package that the rule belongs to identified by name.
        :param uid: (optional) The unique identifier of an existing access rule.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__post('show-nat-rule', package, uid, params)

    def set(self, package="", uid="", params={}):
        """Sets new values for a NAT rule within a package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-nat-rule

        :param package: Package that the rule belongs to identified by name.
        :param uid: (optional) The unique identifier of an existing access rule.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__post('set-nat-rule', package, uid, params)

    def delete(self, package="", uid="", params={}):
        """Deletes a NAT rule within a package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-nat-rule

        :param package: Package that the rule belongs to identified by name.
        :param uid: (optional) The unique identifier of an existing access rule.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__post('delete-nat-rule', package, uid, params)

    def show_all(self, package="", params={}):
        """Show all NAT rules within a package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-nat-rulebase

        :param package: The name of an existing package.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        payload = { 'package': package }
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post('show-nat-rulebase', payload=payload)

class NATSection:
    """Manage NAT sections."""

    def __init__(self, core_client):
        self.__cc = core_client

    def __post(self, endpoint, package="", name="", uid="", params={}):
        payload = { 'package': package }
        if name:
            payload['name'] = name
        if uid:
            payload['uid'] = uid
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post(endpoint, payload=payload)

    def add(self, package="", position="", params={}):
        """Adds a NAT section.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-nat-section

        :param package: Package that the section belongs to identified by name.
        :param position: Position in the rulebase. Can be specified in various ways.
        :type position: integer, string or dict (e.g. 1, 'top', 'bottom', or "{ 'above': 'Section One' }")
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        payload = { 'package': package, 'position': position }
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post('add-nat-section', payload=payload)

    def show(self, package='', name='', uid='', params={}):
        """Shows details of a NAT section within a package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-nat-section

        :param package: Package that the section belongs to identified by name.
        :param name: (optional) The name of an existing NAT section.
        :param uid: (optional) The unique identifier of an existing NAT section.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__post('show-nat-section', package, name, uid, params)

    def set(self, package='', name='', uid='', params={}):
        """Sets new values for a NAT section within a package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-nat-section

        :param package: Package that the section belongs to identified by name.
        :param name: (optional) The name of an existing NAT section.
        :param uid: (optional) The unique identifier of an existing NAT section.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__post('set-nat-section', package, name, uid, params)

    def delete(self, package='', name='', uid='', params={}):
        """Deletes a NAT section within a package.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-nat-section

        :param package: Package that the section belongs to identified by name.
        :param name: (optional) The name of an existing NAT section.
        :param uid: (optional) The unique identifier of an existing NAT section.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__post('delete-nat-section', package, name, uid, params)
