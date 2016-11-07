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

# cpcauto.objects.exceptions
# ~~~~~~~~~~~~~~~~~~~~~~~

"""This module contains the set of cpauto objects exceptions."""

from .. core.exceptions import WebClientError

class AccessClientError(WebClientError):
    """Exception raised when an access control and NAT web client runs into trouble."""
    pass

class NetworkClientError(WebClientError):
    """Exception raised when a network web client runs into trouble."""
    pass

class PolicyClientError(WebClientError):
    """Exception raised when a policy web client runs into trouble."""
    pass

class SimpleGatewayClientError(WebClientError):
    """Exception raised when a simple gateway web client runs into trouble."""
    pass
