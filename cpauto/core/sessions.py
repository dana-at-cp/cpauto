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

"""
cpauto.core.sessions
~~~~~~~~~~~~~~~~~~~~

This module contains the primary objects needed to manage R80 Web API sessions.

"""

from .exceptions import SessionsClientError

import requests

class SessionsClient:
    USER_AGENT = "cpauto-SessionsClient/0.0.1"
    BASE_URI_PATH = "/web_api/"

    def __init__(self, user, password, mgmt_server, port='443', verify=True):
        self.last_login_code = None
        self.last_login_json = None
        self.user = user
        self.password = password
        self.mgmt_server = mgmt_server
        self.port = port
        self.verify = verify

    def build_uri(self, endpoint):
        uri = 'https://' + self.mgmt_server + ':' + self.port + SessionsClient.BASE_URI_PATH + endpoint
        return uri

    def build_headers(self, send_sid=True):
        headers = { 'content-type': 'application/json', 'user-agent': SessionsClient.USER_AGENT }
        if send_sid and self.last_login_json is not None:
            headers['x-chkp-sid'] = self.last_login_json['sid']
        return headers

    def login(self):
        uri = self.build_uri('login')
        headers = self.build_headers(send_sid=False)
        payload = { 'user': self.user,
                    'password': self.password }
        r = requests.post(uri, headers=headers, json=payload, verify=self.verify)
        self.last_login_code = r.status_code
        if r.status_code != 200:
            raise SessionsClientError("Failed to login", r.status_code)
        resp_json = r.json()
        self.last_login_json = resp_json
        return resp_json
