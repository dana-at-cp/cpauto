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

# cpauto.core.sessions
# ~~~~~~~~~~~~~~~~~~~~

"""This module contains the primary objects needed to manage R80 Web API sessions."""

from .exceptions import (
    ConnectionError,
    HTTPError,
    SSLError,
    Timeout,
    TooManyRedirects,
    InvalidURL
)

import requests

class CoreClientResult:
    """Stores the status code and JSON body
    received in an HTTP response to an API request.

    """
    def __init__(self, status_code, json):
        self.status_code = status_code
        self.__json = json

    def json(self):
        return dict(self.__json)

class CoreClient:
    """The cpauto core client.

    Provides basic configuration and persistence.

    Basic Usage::
      >>> import cpauto
      >>> cc = cpauto.CoreClient('admin', 'vpn123', '10.11.12.13')
      >>> r = cc.login()
      >>> print(r.status_code)
      200
    """

    def __init__(self, user='', password='', mgmt_server='', port=443, verify=True):
        self.__last_login_result = None
        self.__user = user
        self.__password = password
        self.__mgmt_server = mgmt_server
        self.__port = port
        self.__verify = verify

    def __build_uri(self, endpoint):
        uri = 'https://' + self.__mgmt_server + ':' + str(self.__port) + '/web_api/' + endpoint
        return uri

    def __build_headers(self, send_sid=True):
        headers = { 'content-type': 'application/json', 'user-agent': 'cpauto-CoreClient/0.0.1' }
        if send_sid and self.__last_login_result is not None:
            last_login_json = self.__last_login_result.json()
            headers['x-chkp-sid'] = last_login_json['sid']
        return headers

    def http_post(self, endpoint, send_sid=True, payload={}):
        """Makes an HTTP post to the specified API endpoint using user supplied data.

        :param endpoint: The API endpoint (e.g. /login).
        :param send_sid: Send the session ID as a header when true.
        :param payload: The payload (dictionary) that will be included
            as JSON in the body of the request.
        :rtype: CoreClientResult
        """
        uri = self.__build_uri(endpoint)
        headers = self.__build_headers(send_sid)
        try:
            r = requests.post(uri, headers=headers, json=payload, verify=self.__verify)
        except requests.exceptions.SSLError as e:
            raise SSLError('SSL error: ' + str(e))
        except requests.exceptions.ConnectionError as e:
            raise ConnectionError('Connection error: ' + str(e))
        except requests.exceptions.HTTPError as e:
            raise HTTPError('HTTP error: ' + str(e))
        except requests.exceptions.Timeout as e:
            raise Timeout(str(e))
        except requests.exceptions.TooManyRedirects as e:
            raise TooManyRedirects(str(e))
        except requests.exceptions.InvalidURL as e:
            raise InvalidURL(str(e))
        return CoreClientResult(r.status_code, r.json())

    def merge_payloads(self, payload_a, payload_b):
        """Merges the contents of two payloads (dictionaries).

        :param payload_a: A payload to merge
        :param payload_b: Another payload to merge
        :returns: A single payload (dictionary) with the contents of the two original payloads
        """
        payload_c = payload_a.copy()
        payload_c.update(payload_b)
        return payload_c

    def login(self, params={}):
        """Login to the R80 Web API server and store the results
        of the request as a class attribute.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/login

        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        payload = { 'user': self.__user,
                    'password': self.__password }
        if params:
            payload = self.merge_payloads(payload, params)
        r = self.http_post('login', send_sid=False, payload=payload)
        self.__last_login_result = r
        return r

    def logout(self):
        """Logout of the R80 Web API server and invalidate the session.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/logout

        :rtype: CoreClientResult
        """
        return self.http_post('logout')

    def publish(self, uid=""):
        """Makes all changes made visible to other users.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/publish

        :param uid: (optional) Specify a different session unique
            identifier to publish.
        :rtype: CoreClientResult
        """
        payload = {}
        if uid:
            payload['uid'] = uid
        return self.http_post('publish', payload=payload)

    def discard(self, uid=""):
        """Discards all changes made and removes them from the database.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/discard

        :param uid: (optional) Specify a different sessions unique
            identifier to discard.
        :rtype: CoreClientResult
        """
        payload = {}
        if uid:
            payload['uid'] = uid
        return self.http_post('discard', payload=payload)

    def keepalive(self):
        """Keeps the session alive and valid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/keepalive

        :rtype: CoreClientResult
        """
        return self.http_post('keepalive')
