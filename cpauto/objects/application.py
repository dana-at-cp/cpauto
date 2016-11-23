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

# cpauto.objects.application
# ~~~~~~~~~~~~~~~~~~~~~~~~~~

"""This module contains the classes needed to manage application objects."""

from ._common import _CommonClient

class App:
    """Manage application sites."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name='', url_list='', app_sig='', params={}):
        """Adds an application site.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-application-site

        :param name: A name for the new application site.
        :param url_list: (optional) A URL or set of URLs that comprises the application.
        :type url_list: string or list of strings
        :param app_sig: (optional) A signature or set of signatures generated via the signature tool.
        :type app_sig: string or list of strings
        :param params: (optional) A dictionary of additional, supported
            parameter names and values.
        :rtype: CoreClientResult
        """
        if url_list:
            params['url-list'] = url_list
        if app_sig:
            params['application-signature'] = app_sig
        return self.__common_client._add('add-application-site', name, params)

    def show(self, name='', uid='', app_id='', details_level=''):
        """Shows details of an application site with the specified name,
        uid, or application ID.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-application-site

        :param name: (optional) The name of an existing application site.
        :param uid: (optional) The unique identifier of an existing application site.
        :param app_id: (optional) The application ID of an existing application site.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        params = {}
        if app_id:
            params['application-id'] = app_id
        return self.__common_client._show('show-application-site', name=name, uid=uid, details_level=details_level, params=params)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing application site with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-application-site

        :param name: (optional) The name of an existing application site.
        :param uid: (optional) The unique identifier of an existing application site.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-application-site', name=name, uid=uid, params=params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing application site with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-application-site

        :param name: (optional) The name of an existing application site.
        :param uid: (optional) The unique identifier of an existing application site.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-application-site', name=name, uid=uid, params=params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all application sites with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-application-sites

        :param limit: (optional) Limit the total number of results shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of items in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-application-sites', limit=limit,
            offset=offset, order=order, details_level=details_level)

class AppCategory:
    """Manage application site categories."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name='', params={}):
        """Adds an application site category.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-application-site-category

        :param name: A name for the new application site category.
        :param params: (optional) A dictionary of additional, supported
            parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-application-site-category', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of an application site category with the specified name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-application-site-category

        :param name: (optional) The name of an existing application site category.
        :param uid: (optional) The unique identifier of an existing application site category.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-application-site-category', name=name, uid=uid, details_level=details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing application site category with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-application-site-category

        :param name: (optional) The name of an existing application site category.
        :param uid: (optional) The unique identifier of an existing application site category.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-application-site-category', name=name, uid=uid, params=params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing application site category with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-application-site-category

        :param name: (optional) The name of an existing application site category.
        :param uid: (optional) The unique identifier of an existing application site category.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-application-site-category', name=name, uid=uid, params=params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all application site categories with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-application-site-categories

        :param limit: (optional) Limit the total number of results shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of items in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-application-site-categories', limit=limit,
            offset=offset, order=order, details_level=details_level)

class AppGroup:
    """Manage application site groups."""

    def __init__(self, core_client):
        self.__common_client = _CommonClient(core_client)

    def add(self, name='', params={}):
        """Adds an application site group.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/add-application-site-group

        :param name: A name for the new application site group.
        :param params: (optional) A dictionary of additional, supported
            parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._add('add-application-site-group', name, params)

    def show(self, name='', uid='', details_level=''):
        """Shows details of an application site group with the specified name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-application-site-group

        :param name: (optional) The name of an existing application site group.
        :param uid: (optional) The unique identifier of an existing application site group.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-application-site-group', name=name, uid=uid, details_level=details_level)

    def set(self, name='', uid='', params={}):
        """Sets new values for an existing application site group with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-application-site-group

        :param name: (optional) The name of an existing application site group.
        :param uid: (optional) The unique identifier of an existing application site group.
        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-application-site-group', name=name, uid=uid, params=params)

    def delete(self, name='', uid='', params={}):
        """Deletes an existing application site group with the specified
        name or uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/delete-application-site-group

        :param name: (optional) The name of an existing application site group.
        :param uid: (optional) The unique identifier of an existing application site group.
        :param params: (optional) A dictionary of additional, supported parameter name$
        :rtype: CoreClientResult
        """
        return self.__common_client._delete('delete-application-site-group', name=name, uid=uid, params=params)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all application site groups with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-application-site-groups

        :param limit: (optional) Limit the total number of results shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of items in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-application-site-groups', limit=limit,
            offset=offset, order=order, details_level=details_level)
