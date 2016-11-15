# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.host module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("name,ip_address,ipv4_address,ipv6_address,params", [
    ("srv_cams", "192.168.1.91", "", "", {}),
    ("srv_dns", '', "10.11.12.13", '2002:0a0b:0c0d::0a0b:0c0d', {}),
    ("srv_web", "192.168.1.4", "", "", {"host-servers": {"web-server": True}}),
])
def test_add(core_client, mgmt_server_base_uri, name, ip_address, ipv4_address, ipv6_address, params):
    endpoint = mgmt_server_base_uri + 'add-host'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.HostClient(core_client)
        r = c.add(name=name, ip_address=ip_address,
                  ipv4_address=ipv4_address, ipv6_address=ipv6_address,
                  params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("srv_web", "", ""),
    ("", "srvuid", ""),
    ("srv_dns", "", "uid"),
    ("", "srvuid", "full"),
])
def test_show(core_client, mgmt_server_base_uri, name, uid, details_level):
    endpoint = mgmt_server_base_uri + 'show-host'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.HostClient(core_client)
        r = c.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("srv_web", "", {"host-servers": {"web-server": True}}),
    ("", "srvuid", {"ignore-errors": True}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-host'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.HostClient(core_client)
        r = c.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("srv_web", "", {}),
    ("", "srvuid", {}),
    ("srv_dns", "", {'details-level': 'full'}),
    ("", "srvuid", {'ignore-errors': True}),
])
def test_delete(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-host'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.HostClient(core_client)
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
    endpoint = mgmt_server_base_uri + 'show-hosts'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.HostClient(core_client)
        r = c.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
