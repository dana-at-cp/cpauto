# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.simplegateway module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("name,ip_address,ipv4_address,ipv6_address,params", [
    ("gw-2200", "192.168.1.1", "", "", {}),
    ("gw-61K", '', "10.11.12.13", '2002:0a0b:0c0d::0a0b:0c0d', {}),
    ("gw-vmware", "192.168.1.4", "", "", {"one-time-password": "password1"}),
])
def test_add(core_client, mgmt_server_base_uri, name, ip_address, ipv4_address, ipv6_address, params):
    endpoint = mgmt_server_base_uri + 'add-simple-gateway'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.SimpleGateway(core_client)
        r = c.add(name=name, ip_address=ip_address,
                  ipv4_address=ipv4_address, ipv6_address=ipv6_address,
                  params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("gw-2200", "", ""),
    ("", "somelonguid", ""),
    ("gw-2200", "", "uid"),
    ("", "somelonguid", "full"),
])
def test_show(core_client, mgmt_server_base_uri, name, uid, details_level):
    endpoint = mgmt_server_base_uri + 'show-simple-gateway'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.SimpleGateway(core_client)
        r = c.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("gw-2200", "", {'ip-address': '192.168.1.1', 'one-time-password': 'password1'}),
    ("", "somelonguid", {'threat-emulation': 'True'}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-simple-gateway'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.SimpleGateway(core_client)
        r = c.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("gw-2200", "", {}),
    ("", "somelonguid", {}),
    ("gw-2200", "", {'details-level': 'full'}),
    ("", "somelonguid", {'ignore-errors': 'True'}),
])
def test_delete(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-simple-gateway'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.SimpleGateway(core_client)
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
    endpoint = mgmt_server_base_uri + 'show-simple-gateways'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.SimpleGateway(core_client)
        r = c.show_all(limit=limit, offset=offset,
                       order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
