# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.application module."""

import pytest
import responses
import cpauto

@pytest.mark.parametrize("name,url_list,app_sig,params", [
    ("thisisaname", "https://www.google.com", "", {}),
    ("thisisaname", "", "thisisanappsig", {"tags": ["foo", "bar"]}),
])
def test_add(core_client, mgmt_server_base_uri, name, url_list, app_sig, params):
    resources = [ "add-application-site", "add-application-site-category",
                  "add-application-site-group"]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        a = cpauto.App(core_client)
        r = a.add(name=name, url_list=url_list, app_sig=app_sig, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        a = cpauto.AppCategory(core_client)
        r = a.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        a = cpauto.AppGroup(core_client)
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
    resources = [ "show-application-site", "show-application-site-category",
                  "show-application-site-group"]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.App(core_client)
        if details_level:
            r = s.show(name="", uid="", app_id="someappid", details_level=details_level)
        else:
            r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppCategory(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppGroup(core_client)
        r = s.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("somename", "", {"tags": ["foo", "bar"]}),
    ("", "someuid", {"ignore-errors": True}),
])
def test_set(core_client, mgmt_server_base_uri, name, uid, params):
    resources = [ "set-application-site", "set-application-site-category",
                  "set-application-site-group"]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.App(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppCategory(core_client)
        r = s.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppGroup(core_client)
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
    resources = [ "delete-application-site", "delete-application-site-category",
                  "delete-application-site-group"]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.App(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppCategory(core_client)
        r = s.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppGroup(core_client)
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
    resources = [ "show-application-sites", "show-application-site-categories",
                  "show-application-site-groups"]
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        for resource in resources:
            endpoint = mgmt_server_base_uri + resource
            rsps.add(responses.POST, endpoint,
                     json=resp_body, status=200,
                     content_type='application/json')

        s = cpauto.App(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppCategory(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

        s = cpauto.AppGroup(core_client)
        r = s.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body
