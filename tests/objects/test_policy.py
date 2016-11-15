# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.policy module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("access,threat,policy_package,targets", [
    (True, True, "", ""),
    (True, True, "", []),
    (True, False, "FWOnly", "FW-1"),
    (False, True, "Threatz", ["GW-0", "GW-1A", "GW-1B"]),
])
def test_install(core_client, mgmt_server_base_uri, access, threat, policy_package, targets):
    endpoint = mgmt_server_base_uri + 'install-policy'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.PolicyClient(core_client)
        r = c.install(access=access, threat=threat, policy_package=policy_package, targets=targets)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,params", [
    ("empty", {}),
    ("fwonly", {'access': True, 'threat-prevention': False}),
    ("fullpolicy", {'access': True, 'threat-prevention': True}),
])
def test_add(core_client, mgmt_server_base_uri, name, params):
    endpoint = mgmt_server_base_uri + 'add-package'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.PolicyClient(core_client)
        r = c.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("somepolicyname", "", ""),
    ("", "somepolicyuid", ""),
    ("somepolicyname", "", "uid"),
    ("", "somepolicyuid", "full"),
])
def test_show(core_client, mgmt_server_base_uri, name, uid, details_level):
    endpoint = mgmt_server_base_uri + 'show-package'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.PolicyClient(core_client)
        r = c.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("somepolicyname", "", {'new-name': 'somenewpolicyname'}),
    ("", "somepolicyuid", {'access': False}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-package'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.PolicyClient(core_client)
        r = c.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("somepolicyname", "", {}),
    ("", "somepolicyuid", {}),
    ("somepolicyname", "", {'details-level': 'full'}),
    ("", "somepolicyuid", {'ignore-errors': True}),
])
def test_delete(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-package'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.PolicyClient(core_client)
        r = c.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("limit,offset,order,details_level", [
    (50, 0, [], ''),
    (50, 0, [{'ASC': 'foo'}], ''),
    (64, 32, [{'DESC': 'bar'}], 'uid'),
])
def test_show_all(core_client, mgmt_server_base_uri,
    limit, offset, order, details_level):
    endpoint = mgmt_server_base_uri + 'show-packages'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.PolicyClient(core_client)
        r = c.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
