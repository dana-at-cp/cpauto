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

# cpcauto.core.exceptions
# ~~~~~~~~~~~~~~~~~~~~~~~

"""This module contains the set of cpauto core exceptions."""

class Error(IOError):
    """Base class for exceptions in this module."""
    pass

class WebClientError(Error):
    """Exception raised when a web client runs into trouble."""
    def __init__(self, message, http_status_code=None):
        super(WebClientError, self).__init__(message)
        self.http_status_code = http_status_code

class CoreClientError(WebClientError):
    """Exception raised when an core web client runs into trouble."""
    pass

class ConnectionError(CoreClientError):
    """A connection error occurred."""
    pass

class HTTPError(CoreClientError):
    """An HTTP error occurred."""
    pass

class SSLError(CoreClientError):
    """An SSL error occurred."""
    pass

class Timeout(CoreClientError):
    """The request timed out."""
    pass

class TooManyRedirects(CoreClientError):
    """Too many redirects."""
    pass

class InvalidURL(CoreClientError, ValueError):
    """The URL provided was invalid."""
    pass
