# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.network module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("name", ['net_test_a', 'net_test_b'])
@pytest.mark.parametrize("params", [{},
    { 'subnet': '192.168.1.0', 'subnet-mask': '255.255.255.0'},
    { 'subnet': '10.0.0.0', 'subnet-mask': '255.255.255.0' }])
def test_add(core_client, mgmt_server_base_uri, name, params):
    endpoint = mgmt_server_base_uri + 'add-network'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        nc = cpauto.NetworkClient(core_client)
        r = nc.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("net_test", None, None),
    (None, "netuid", None),
    ("net_test", None, "uid"),
    (None, "netuid", "full"),
])
def test_show(core_client, mgmt_server_base_uri, name, uid, details_level):
    endpoint = mgmt_server_base_uri + 'show-network'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        nc = cpauto.NetworkClient(core_client)
        r = nc.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("net_test", None, {'subnet': '192.168.1.0', 'subnet-mask': '255.255.255.0'}),
    (None, "netuid", {'subnet': '10.0.0.0', 'subnet-mask': '255.255.255.0'}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-network'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        nc = cpauto.NetworkClient(core_client)
        r = nc.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("net_test", None, {}),
    (None, "netuid", {}),
    ("net_test", None, {'details-level': 'full'}),
    (None, "netuid", {'ignore-errors': 'True'}),
])
def test_delete(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-network'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        nc = cpauto.NetworkClient(core_client)
        r = nc.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("limit,offset,order,details_level", [
    (50, 0, [], ''),
    (50, 0, [{'ASC': 'foo'}], ''),
    (64, 32, [{'DESC': 'bar'}], 'uid'),
])
def test_show_all(core_client, mgmt_server_base_uri,
    limit, offset, order, details_level):
    endpoint = mgmt_server_base_uri + 'show-networks'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        nc = cpauto.NetworkClient(core_client)
        r = nc.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
