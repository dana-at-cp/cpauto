# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.access module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("layer,position,params", [
    ("MyPolicy Network", "top", {'enabled': False}),
    ("MyPolicy Threat", 1, {}),
    ("MyPolicy Network", {"bottom": "section1"}, {"time": "any"}),
])
def test_add_access_rule(core_client, mgmt_server_base_uri, layer, position, params):
    endpoint = mgmt_server_base_uri + 'add-access-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        ar = cpauto.AccessRule(core_client)
        r = ar.add(layer=layer, position=position, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body
