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
    CoreClientError,
    WaitOnTaskError,
    ConnectionError,
    HTTPError,
    SSLError,
    Timeout,
    TooManyRedirects,
    InvalidURL
)

from ..objects._common import _CommonClient

import time

import requests

class CoreClientResult:
    """Stores the status code and JSON body
    received in an HTTP response to an API request.

    """
    def __init__(self, status_code, json):
        self.status_code = status_code
        self.success = status_code == 200
        self.message = ""
        self.__json = json

    def set_success(self, value=True):
        self.success = value

    def set_message(self, value=""):
        self.message = value

    def json(self):
        return dict(self.__json)

class CoreClient:
    """The cpauto core client.

    Provides basic configuration and persistence.

    Basic Usage::
      >>> import cpauto
      >>> cc = cpauto.CoreClient('admin', 'vpn123', '10.11.12.13')
      >>> r = cc.login()
      >>> r.status_code
      200
    """

    def __init__(self, user='', password='', mgmt_server='', port=443, verify=True, wait_for_tasks=True):
        self.__last_login_result = None
        self.__user = user
        self.__password = password
        self.__mgmt_server = mgmt_server
        self.__port = port
        self.__verify = verify
        self.__wait_for_tasks = wait_for_tasks

    def __build_uri(self, endpoint):
        uri = 'https://' + self.__mgmt_server + ':' + str(self.__port) + '/web_api/' + endpoint
        return uri

    def __build_headers(self, send_sid=True):
        headers = { 'content-type': 'application/json', 'user-agent': 'cpauto-CoreClient/0.0.4' }
        if send_sid and self.__last_login_result is not None:
            last_login_json = self.__last_login_result.json()
            headers['x-chkp-sid'] = last_login_json['sid']
        return headers

    def __wait_on_task(self, task_id):
        task_complete = False
        task_r = None

        while not task_complete:
            task_r = self.http_post(endpoint="show-task", payload={"task-id": task_id, "details-level": "full"})

            if task_r.status_code != 200:
                raise WaitOnTaskError("Failed to handle asynchronous task as synchronous")

            data = task_r.json()
            completed_tasks = sum(1 for task in data["tasks"] if task["status"] != "in progress")
            total_tasks = len(data["tasks"])

            if completed_tasks == total_tasks:
                task_complete = True
            else:
                time.sleep(2)

        self.__check_task_result(task_r)
        return task_r

    def __wait_on_tasks(self, task_objects):
        tasks = []
        for task_object in task_objects:
            task_id = task_object["task-id"]
            tasks.append(task_id)
            self.__wait_on_task(task_id)

        task_r = self.http_post(endpoint="show-task", payload={"task-id": tasks, "details-level": "full"})

        self.__check_task_result(task_r)
        return task_r

    def __check_task_result(self, task_result):
        data = task_result.json()
        for task in data["tasks"]:
            if task["status"] == "failed" or task["status"] == "partially succeeded":
                task_result.set_success(False)
                task_result.set_message("There was at least one task that failed or partially succeeded")
                break

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
            # wait for tasks if needed
            if self.__wait_for_tasks and r.status_code == 200 and endpoint != "show-task":
                data = r.json()
                if "task-id" in data:
                    return self.__wait_on_task(data["task-id"])
                elif "tasks" in data:
                    return self.__wait_on_tasks(data["tasks"])
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

class Session:
    """Manage sessions."""

    def __init__(self, core_client):
        self.__core_client = core_client
        self.__common_client = _CommonClient(core_client)

    def switch(self, uid=""):
        """Switch sessions.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/switch-session

        :param uid: A session unique identifier.
        :rtype: CoreClientResult
        """
        payload = { 'uid': uid }
        return self.__core_client.http_post('switch-session', payload=payload)

    def show(self, uid=""):
        """Shows details of current session or a session with
        the specified uid.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-session

        :param uid: (optional) The unique identifier of an existing session.
        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-session', name="", uid=uid, details_level="")

    def set(self, params={}):
        """Sets new values for certain parameters of the current session.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-session

        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-session', name="", uid="", params=params)

    def continue_in_sc(self, uid=""):
        """Logout from existing session. The session will be continued next time your open
        SmartConsole. In case 'uid' is not provided, use current session. In order for the
        session to pass successfully to SmartConsole, make sure you don't have any other
        active GUI sessions.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/continue-session-in-smartconsole

        :param uid: (optional) The unique identifier of an existing session.
        :rtype: CoreClientResult
        """
        payload = {}
        if uid:
            payload['uid'] = uid
        return self.__core_client.http_post('continue-session-in-smartconsole', payload=payload)

    def show_all(self, limit=50, offset=0, order=[], details_level=''):
        """Shows all sessions with some reasonable limitations.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-sessions

        :param limit: (optional) Limit the total number of sessions shown.
            The default value is 50 and allowed values are in the range 1 to 500.
        :param offset: (optional) Skip a number of sessions in the results
            before they are shown. Default value is 0.
        :param order: (optional) Sort the results by the specified field. The
            default is a random order.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        return self.__common_client._show_all('show-sessions', limit=limit,
            offset=offset, order=order, details_level=details_level)

class LoginMessage:
    """Manage login message."""

    def __init__(self, core_client):
        self.__core_client = core_client
        self.__common_client = _CommonClient(core_client)

    def show(self):
        """Shows details of current login message.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/show-login-message

        :rtype: CoreClientResult
        """
        return self.__common_client._show('show-login-message', name="", uid="", details_level="")

    def set(self, params={}):
        """Sets new values for current login message.

        https://sc1.checkpoint.com/documents/R80/APIs/#web/set-login-message

        :param params: (optional) A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        return self.__common_client._set('set-login-message', name="", uid="", params=params)
