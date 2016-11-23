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

# cpauto.objects.service
# ~~~~~~~~~~~~~~~~~~~~~~

"""This module contains the classes needed to manage service objects."""

from ._common import _CommonClient

class ServiceTCP:
    """Manage TCP services."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", params={}):
        """Adds a TCP service.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-service-tcp

        :param name: A name for the new TCP service.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-service-tcp', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a TCP service with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-tcp

        :param name: (optional) The name of an existing TCP service.
        :param uid: (optional) The unique identifier of an existing TCP service.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-service-tcp', name, uid, details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing TCP service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-service-tcp

        :param name: (optional) The name of an existing TCP service.
        :param uid: (optional) The unique identifier of an existing TCP service.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-service-tcp', name, uid, params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing TCP service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-service-tcp

        :param name: (optional) The name of an existing TCP service.
        :param uid: (optional) The unique identifier of an existing TCP service.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-service-tcp', name, uid, params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all TCP services with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-services-tcp

        :param limit: (optional) Limit the total number of TCP services shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of TCP services in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-services-tcp', limit=limit,
            offset=offset, order=order, details_level=details_level)

class ServiceUDP:
    """Manage UDP services."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", params={}):
        """Adds a UDP service.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-service-udp

        :param name: A name for the new UDP service.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-service-udp', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a UDP service with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-udp

        :param name: (optional) The name of an existing UDP service.
        :param uid: (optional) The unique identifier of an existing UDP service.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-service-udp', name, uid, details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing UDP service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-service-udp

        :param name: (optional) The name of an existing UDP service.
        :param uid: (optional) The unique identifier of an existing UDP service.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-service-udp', name, uid, params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing UDP service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-service-udp

        :param name: (optional) The name of an existing UDP service.
        :param uid: (optional) The unique identifier of an existing UDP service.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-service-udp', name, uid, params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all UDP services with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-services-udp

        :param limit: (optional) Limit the total number of UDP services shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of UDP services in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-services-udp', limit=limit,
            offset=offset, order=order, details_level=details_level)

class ServiceSCTP:
    """Manage SCTP services."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", port="", params={}):
        """Adds a SCTP service.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-service-sctp

        :param name: A name for the new SCTP service.
        :param port: Port number or range (e.g. "443" or "80-81").
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        params["port"] = port
        return self.__common_client._add('add-service-sctp', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a SCTP service with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-sctp

        :param name: (optional) The name of an existing SCTP service.
        :param uid: (optional) The unique identifier of an existing SCTP service.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-service-sctp', name, uid, details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing SCTP service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-service-sctp

        :param name: (optional) The name of an existing SCTP service.
        :param uid: (optional) The unique identifier of an existing SCTP service.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-service-sctp', name, uid, params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing SCTP service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-service-sctp

        :param name: (optional) The name of an existing SCTP service.
        :param uid: (optional) The unique identifier of an existing SCTP service.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-service-sctp', name, uid, params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all SCTP services with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-services-sctp

        :param limit: (optional) Limit the total number of SCTP services shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of SCTP services in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-services-sctp', limit=limit,
            offset=offset, order=order, details_level=details_level)

class ServiceOther:
    """Manage generic services."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", params={}):
        """Adds a generic service.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-service-other

        :param name: A name for the new generic service.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-service-other', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a generic service with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-other

        :param name: (optional) The name of an existing generic service.
        :param uid: (optional) The unique identifier of an existing generic service.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-service-other', name, uid, details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing generic service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-service-other

        :param name: (optional) The name of an existing generic service.
        :param uid: (optional) The unique identifier of an existing generic service.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-service-other', name, uid, params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing generic service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-service-other

        :param name: (optional) The name of an existing generic service.
        :param uid: (optional) The unique identifier of an existing generic service.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-service-other', name, uid, params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all generic services with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-services-other

        :param limit: (optional) Limit the total number of generic services shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of generic services in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-services-other', limit=limit,
            offset=offset, order=order, details_level=details_level)

class ServiceGroup:
    """Manage service groups."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", params={}):
        """Adds a service group.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-service-group

        :param name: A name for the new service group.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-service-group', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a service group with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-group

        :param name: (optional) The name of an existing service group.
        :param uid: (optional) The unique identifier of an existing service group.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-service-group', name, uid, details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing service group with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-service-group

        :param name: (optional) The name of an existing service group.
        :param uid: (optional) The unique identifier of an existing service group.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-service-group', name, uid, params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing service group with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-service-group

        :param name: (optional) The name of an existing service group.
        :param uid: (optional) The unique identifier of an existing service group.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-service-group', name, uid, params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all service groups with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-groups

        :param limit: (optional) Limit the total number of service groups shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of service groups in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-service-groups', limit=limit,
            offset=offset, order=order, details_level=details_level)

class ServiceDCERPC:
    """Manage DCE-RPC services."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", params={}):
        """Adds a DCE-RPC service.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-service-dce-rpc

        :param name: A name for the new DCE-RPC service.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-service-dce-rpc', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a DCE-RPC service with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-dce-rpc

        :param name: (optional) The name of an existing DCE-RPC service.
        :param uid: (optional) The unique identifier of an existing DCE-RPC service.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-service-dce-rpc', name, uid, details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing DCE-RPC service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-service-dce-rpc

        :param name: (optional) The name of an existing DCE-RPC service.
        :param uid: (optional) The unique identifier of an existing DCE-RPC service.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-service-dce-rpc', name, uid, params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing DCE-RPC service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-service-dce-rpc

        :param name: (optional) The name of an existing DCE-RPC service.
        :param uid: (optional) The unique identifier of an existing DCE-RPC service.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-service-dce-rpc', name, uid, params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all DCE-RPC services with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-services-dce-rpc

        :param limit: (optional) Limit the total number of DCE-RPC services shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of DCE-RPC services in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-services-dce-rpc', limit=limit,
            offset=offset, order=order, details_level=details_level)

class ServiceRPC:
    """Manage RPC services."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name="", params={}):
        """Adds a RPC service.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-service-rpc

        :param name: A name for the new RPC service.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-service-rpc', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of a RPC service with the specified name
        or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-service-rpc

        :param name: (optional) The name of an existing RPC service.
        :param uid: (optional) The unique identifier of an existing RPC service.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-service-rpc', name, uid, details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing RPC service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-service-rpc

        :param name: (optional) The name of an existing RPC service.
        :param uid: (optional) The unique identifier of an existing RPC service.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-service-rpc', name, uid, params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing RPC service with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-service-rpc

        :param name: (optional) The name of an existing RPC service.
        :param uid: (optional) The unique identifier of an existing RPC service.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-service-rpc', name, uid, params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all RPC services with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-services-rpc

        :param limit: (optional) Limit the total number of RPC services shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of RPC services in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-services-rpc', limit=limit,
            offset=offset, order=order, details_level=details_level)
