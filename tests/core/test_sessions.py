# -*- coding: utf-8 -*-

"""Tests for cpauto.core.sessions module."""

import pytest
import responses
import cpauto

from requests.exceptions import SSLError
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError
from requests.exceptions import Timeout
from requests.exceptions import TooManyRedirects
from requests.exceptions import InvalidURL

@pytest.mark.parametrize("payload_a,payload_b,expected", [
    ({ "foo": "bar"}, { "one": "two" }, { "foo": "bar", "one": "two" }),
])
def test_merge_payloads(core_client, payload_a, payload_b, expected):
    merged = core_client.merge_payloads(payload_a, payload_b)
    assert merged == expected

@pytest.mark.parametrize("resource,caught,raised", [
    ("foo", SSLError(), cpauto.SSLError),
    ("foo", ConnectionError(), cpauto.ConnectionError),
    ("foo", HTTPError(), cpauto.HTTPError),
    ("foo", Timeout(), cpauto.Timeout),
    ("foo", TooManyRedirects(), cpauto.TooManyRedirects),
    ("foo", InvalidURL(), cpauto.InvalidURL),
])
def test_http_post_exceptions(core_client, mgmt_server_base_uri, resource, caught, raised):
    endpoint = mgmt_server_base_uri + resource
    with responses.RequestsMock(assert_all_requests_are_fired=False) as rsps:
        rsps.add(responses.POST, endpoint,
                 body=caught, status=200,
                 content_type='application/json')

        with pytest.raises(raised):
            r = core_client.http_post(endpoint=resource, payload={})

@pytest.mark.parametrize("params", [
    ({}),
    ({ "continue-last-session": "True"}),
    ({ "session-name": "mysessionname", "session-timeout": 900}),
])
def test_login(core_client, mgmt_server_base_uri, params):
    endpoint = mgmt_server_base_uri + 'login'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        r = core_client.login(params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("uid", [
    (None),
    ("someuid"),
])
def test_publish(core_client, mgmt_server_base_uri, uid):
    endpoint = mgmt_server_base_uri + 'publish'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        r = core_client.publish(uid=uid)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("uid", [
    (None),
    ("someuid"),
])
def test_discard(core_client, mgmt_server_base_uri, uid):
    endpoint = mgmt_server_base_uri + 'discard'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        r = core_client.discard(uid=uid)

        assert r.status_code == 200
        assert r.json() == resp_body

def test_logout(core_client, mgmt_server_base_uri):
    endpoint = mgmt_server_base_uri + 'logout'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        r = core_client.logout()

        assert r.status_code == 200
        assert r.json() == resp_body

def test_keepalive(core_client, mgmt_server_base_uri):
    endpoint = mgmt_server_base_uri + 'keepalive'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        r = core_client.keepalive()

        assert r.status_code == 200
        assert r.json() == resp_body
