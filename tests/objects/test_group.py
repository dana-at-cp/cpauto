# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.group module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("name,params", [
    ("grp_basic", {}),
    ("grp_with_comment", {"comments": "ow now brown cow"}),
    ("grp_with_tags", {"tags": ["servers", "web", "dns"]}),
])
def test_add(core_client, mgmt_server_base_uri, name, params):
    endpoint = mgmt_server_base_uri + 'add-group'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.GroupClient(core_client)
        r = c.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("grp_name", "", ""),
    ("", "grpuid", ""),
    ("grp_name", "", "uid"),
    ("", "grpuid", "full"),
])
def test_show(core_client, mgmt_server_base_uri, name, uid, details_level):
    endpoint = mgmt_server_base_uri + 'show-group'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.GroupClient(core_client)
        r = c.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("grp_name", "", {"new-name": "grp_name_new"}),
    ("", "srvuid", {"ignore-errors": True}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-group'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.GroupClient(core_client)
        r = c.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("grp_name", "", {}),
    ("", "grpuid", {}),
    ("grp_some_other", "", {'details-level': 'full'}),
    ("", "srvuid", {'ignore-errors': True}),
])
def test_delete(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-group'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.GroupClient(core_client)
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
    endpoint = mgmt_server_base_uri + 'show-groups'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.GroupClient(core_client)
        r = c.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
