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

from . exceptions import CoreClientError

import requests

class CoreClientResult:
    def __init__(self, status_code, json):
        self.status_code = status_code
        self.__json = json

    def json(self):
        return dict(self.__json)

class CoreClient:
    USER_AGENT = "cpauto-CoreClient/0.0.1"
    BASE_URI_PATH = "/web_api/"

    def __init__(self, user, password, mgmt_server, port='443', verify=True):
        self.__last_login_result = None
        self.__user = user
        self.__password = password
        self.__mgmt_server = mgmt_server
        self.__port = port
        self.__verify = verify

    def __build_uri(self, endpoint):
        uri = 'https://' + self.__mgmt_server + ':' + self.__port + CoreClient.BASE_URI_PATH + endpoint
        return uri

    def __build_headers(self, send_sid=True):
        headers = { 'content-type': 'application/json', 'user-agent': CoreClient.USER_AGENT }
        if send_sid and self.__last_login_result is not None:
            last_login_json = self.__last_login_result.json()
            headers['x-chkp-sid'] = last_login_json['sid']
        return headers

    def http_post(self, endpoint, send_sid=True, payload={}):
        """Makes an HTTP post to the specified API endpoint using user supplied data.
        Returns :class:`CoreClientResult <CoreClientResult>` object.

        :param endpoint: The API endpoint (e.g. /login).
        :param send_sid: Send the session ID as a header when true.
        :param payload: The payload (dictionary) that will be included
            as JSON in the body of the request.
        :rtype: CoreClientResult
        """
        uri = self.__build_uri(endpoint)
        headers = self.__build_headers(send_sid)
        r = requests.post(uri, headers=headers, json=payload, verify=self.__verify)
        return CoreClientResult(r.status_code, r.json())

    def merge_payloads(self, payload_a, payload_b):
        """Merges the contents of two payloads (dictionaries). Returns the
        contents of the two original payloads as a single payload.

        :param payload_a: A payload to merge
        :param payload_b: Another payload to merge
        :rtype: A single payload (dictionary) with the contents of the two original payloads
        """
        payload_c = payload_a.copy()
        payload_c.update(payload_b)
        return payload_c

    def login(self, params={}):
        """Login to the R80 Web API server and store the results
        of the request as a class attribute. Returns a
        :class:`CoreClientResult <CoreClientResult>` object.

        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/login
        payload = { 'user': self.__user,
                    'password': self.__password }
        if params:
            payload = self.merge_payloads(payload, params)
        r = self.http_post('login', send_sid=False, payload=payload)
        self.__last_login_result = r
        return r

    def logout(self):
        """Logout of the R80 Web API server and invalidate the session.
        Returns a :class:`CoreClientResult <CoreClientResult>` object.

        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/logout
        return self.http_post('logout')

    def publish(self, uid=None):
        """Makes all changes made visible to other users. Returns a
        :class:`CoreClientResult <CoreClientResult>` object.

        :param uid: (optional) Specify a different session unique
            identifier to publish.
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/publish
        payload = {}
        if uid is not None:
            payload['uid'] = uid
        return self.http_post('publish', payload=payload)

    def discard(self, uid=None):
        """Discards all changes made and removes them from the database.
        Returns a :class:`CoreClientResult <CoreClientResult>` object.

        :param uid: (optional) Specify a different sessions unique
            identifier to discard.
        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/discard
        payload = {}
        if uid is not None:
            payload['uid'] = uid
        return self.http_post('discard', payload=payload)

    def keepalive(self):
        """Keeps the session alive and valid. Returns a
        :class:`CoreClientResult <CoreClientResult>` object.

        :rtype: CoreClientResult
        """
        # https://sc1.checkpoint.com/documents/R80/APIs/#web/keepalive
        return self.http_post('keepalive')
