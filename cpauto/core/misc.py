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

# cpauto.core.misc
# ~~~~~~~~~~~~~~~~

"""This module contains the primary objects needed to leverage other, powerful R80 Web API features."""

class Misc:
    """Leverages other powerful misc. R80 Web API features."""

    def __init__(self, core_client):
        self.__cc = core_client

    def show_task(self, task_id="", details_level=""):
        """Shows details of specified task or set of tasks.

        https://sc1.checkpoint.com/documents/R80/APIs/index.html#web/show-task

        :param task_id: A unique identifier for one or more tasks.
        :type task_id: A string or list of strings.
        :param details_level: (optional) The level of detail to show. Default
            value is 'standard' and the other options are: 'uid' or 'full'
        :rtype: CoreClientResult
        """
        payload = { "task-id": task_id }
        if details_level:
            payload['details-level'] = details_level
        return self.__cc.http_post('show-task', payload=payload)

    def run_script(self, script="", name="", targets="", params={}):
        """Runs a script on a gateway or set of gateways.

        https://sc1.checkpoint.com/documents/R80/APIs/index.html#web/run-script

        :param script: The script to execute on the gateway or set of gateways.
        :param name: A name for the script.
        :param targets: The gateway or set of gateways to receive the script to execute.
        :type targets: A string or list of strings.
        :param params: A dictionary of additional, supported parameter names and values.
        :rtype: CoreClientResult
        """
        payload = { "script": script, "script-name": name, "targets": targets }
        if params:
            payload = self.__cc.merge_payloads(payload, params)
        return self.__cc.http_post('run-script', payload=payload)

    def put_file(self, content="", name="", path="", targets="", comments=""):
        """Puts file content on a gateway or set of gateways.

        https://sc1.checkpoint.com/documents/R80/APIs/index.html#web/put-file

        :param content: The file content.
        :param name: The file name.
        :param path: The file path.
        :param targets: The gateway or set of gateways to receive the file.
        :type targets: A string or list of strings.
        :param comments: Any comments regarding the file.
        :rtype: CoreClientResult
        """
        payload = { "file-content": content }
        if name:
            payload["file-name"] = name
        if path:
            payload["file-path"] = path
        if targets:
            payload["targets"] = targets
        if comments:
            payload["comments"] = comments
        return self.__cc.http_post("put-file", payload=payload)
