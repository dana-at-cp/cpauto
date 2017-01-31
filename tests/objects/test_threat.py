# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.threat module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("name,params", [
    ("thisisaname", {}),
    ("thisisaname", {"tags": ["foo", "bar"]}),
])
def test_add(core_client, mgmt_server_base_uri, name, params):
    resources = [ "add-threat-profile" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        a = cpauto.ThreatProfile(core_client)
        r = a.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("somename", "", ""),
    ("", "someuid", ""),
    ("somename", "", "uid"),
    ("", "someuid", "full"),
])
def test_show(core_client, mgmt_server_base_uri, name, uid, details_level):
    resources = [ "show-threat-profile" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ThreatProfile(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("somename", "", {"tags": ["foo", "bar"]}),
    ("", "someuid", {"ignore-errors": True}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    resources = [ "set-threat-profile" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ThreatProfile(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("somename", "", {}),
    ("", "someuid", {}),
    ("somename", "", {'details-level': 'full'}),
    ("", "someuid", {'ignore-errors': True}),
])
def test_delete(core_client, mgmt_server_base_uri, name, uid, params):
    resources = [ "delete-threat-profile" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ThreatProfile(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("limit,offset,order,details_level", [
    (50, 0, [], ''),
    (50, 0, [{'ASC': 'foo'}], ''),
    (64, 32, [{'DESC': 'bar'}], 'uid'),
])
def test_show_all(core_client, mgmt_server_base_uri,
    limit, offset, order, details_level):
    resources = [ "show-threat-profiles" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ThreatProfile(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
