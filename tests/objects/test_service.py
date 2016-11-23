# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.service module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("name,params", [
    ("servicename", {}),
    ("servicename", {"tags": ["foo", "bar"]}),
])
def test_add(core_client, mgmt_server_base_uri, name, params):
    resources = [ "add-service-tcp", "add-service-udp",
                  "add-service-sctp", "add-service-other",
                  "add-service-group", "add-service-dce-rpc",
                  "add-service-rpc" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ServiceTCP(core_client)
        r = s.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceUDP(core_client)
        r = s.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceSCTP(core_client)
        r = s.add(name=name, port='3000', params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceOther(core_client)
        r = s.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceGroup(core_client)
        r = s.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceDCERPC(core_client)
        r = s.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceRPC(core_client)
        r = s.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("servicename", "", ""),
    ("", "serviceuid", ""),
    ("servicename", "", "uid"),
    ("", "serviceuid", "full"),
])
def test_show(core_client, mgmt_server_base_uri, name, uid, details_level):
    resources = [ "show-service-tcp", "show-service-udp",
                  "show-service-sctp", "show-service-other",
                  "show-service-group", "show-service-dce-rpc",
                  "show-service-rpc" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ServiceTCP(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceUDP(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceSCTP(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceOther(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceGroup(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceDCERPC(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceRPC(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("servicename", "", {"tags": ["foo", "bar"]}),
    ("", "serviceuid", {"ignore-errors": True}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    resources = [ "set-service-tcp", "set-service-udp",
                  "set-service-sctp", "set-service-other",
                  "set-service-group", "set-service-dce-rpc",
                  "set-service-rpc" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ServiceTCP(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceUDP(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceSCTP(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceOther(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceGroup(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceDCERPC(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceRPC(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("servicename", "", {}),
    ("", "serviceuid", {}),
    ("servicename", "", {'details-level': 'full'}),
    ("", "serviceuid", {'ignore-errors': True}),
])
def test_delete(core_client, mgmt_server_base_uri, name, uid, params):
    resources = [ "delete-service-tcp", "delete-service-udp",
                  "delete-service-sctp", "delete-service-other",
                  "delete-service-group", "delete-service-dce-rpc",
                  "delete-service-rpc" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ServiceTCP(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceUDP(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceSCTP(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceOther(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceGroup(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceDCERPC(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceRPC(core_client)
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
    resources = [ "show-services-tcp", "show-services-udp",
                  "show-services-sctp", "show-services-other",
                  "show-service-groups", "show-services-dce-rpc",
                  "show-services-rpc" ]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.ServiceTCP(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceUDP(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceSCTP(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceOther(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceGroup(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceDCERPC(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.ServiceRPC(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
