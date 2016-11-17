# -*- coding: utf-8 -*-

"""Tests for cpauto.objects.access module."""

import pytest
import responses
import cpauto

# AccessRule

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

@pytest.mark.parametrize("layer,name,uid,params", [
    ("MyPolicy Network", "somerulename", "", {}),
    ("MyPolicy Threat", "", "someruleuid", {}),
    ("MyPolicy Network", "", "", {"rule-number": 1}),
])
def test_show_access_rule(core_client, mgmt_server_base_uri, layer, name, uid, params):
    endpoint = mgmt_server_base_uri + 'show-access-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        ar = cpauto.AccessRule(core_client)
        r = ar.show(layer=layer, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("layer,name,uid,params", [
    ("MyPolicy Network", "somerulename", "", {"enabled": False}),
    ("MyPolicy Threat", "", "someruleuid", {"action": "Drop"}),
    ("MyPolicy Network", "", "", {"rule-number": 1, "new-name": "first rule"}),
])
def test_set_access_rule(core_client, mgmt_server_base_uri, layer, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-access-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        ar = cpauto.AccessRule(core_client)
        r = ar.set(layer=layer, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("layer,name,uid,params", [
    ("MyPolicy Network", "somerulename", "", {}),
    ("MyPolicy Threat", "", "someruleuid", {}),
    ("MyPolicy Network", "", "", {"rule-number": 1, "details-level": "full"}),
])
def test_delete_access_rule(core_client, mgmt_server_base_uri, layer, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-access-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        ar = cpauto.AccessRule(core_client)
        r = ar.delete(layer=layer, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,params", [
    ("MyPolicy Network", {}),
    ("MyPolicy Threat", {"limit": 1}),
    ("MyPolicy Network", {"hits-settings": "gw-2200"}),
])
def test_show_all_access_rules(core_client, mgmt_server_base_uri, name, params):
    endpoint = mgmt_server_base_uri + 'show-access-rulebase'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        ar = cpauto.AccessRule(core_client)
        r = ar.show_all(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

# AccessSection

@pytest.mark.parametrize("layer,position,params", [
    ("MyPolicy Network", "top", {'enabled': False}),
    ("MyPolicy Threat", 1, {}),
    ("MyPolicy Network", {"bottom": "section1"}, {"time": "any"}),
])
def test_add_access_section(core_client, mgmt_server_base_uri, layer, position, params):
    endpoint = mgmt_server_base_uri + 'add-access-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.AccessSection(core_client)
        r = a.add(layer=layer, position=position, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("layer,name,uid,params", [
    ("MyPolicy Network", "somerulename", "", {}),
    ("MyPolicy Threat", "", "someruleuid", {}),
    ("MyPolicy Network", "", "", {"rule-number": 1}),
])
def test_show_access_section(core_client, mgmt_server_base_uri, layer, name, uid, params):
    endpoint = mgmt_server_base_uri + 'show-access-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.AccessSection(core_client)
        r = a.show(layer=layer, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("layer,name,uid,params", [
    ("MyPolicy Network", "somerulename", "", {"enabled": False}),
    ("MyPolicy Threat", "", "someruleuid", {"action": "Drop"}),
    ("MyPolicy Network", "", "", {"rule-number": 1, "new-name": "first rule"}),
])
def test_set_access_section(core_client, mgmt_server_base_uri, layer, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-access-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.AccessSection(core_client)
        r = a.set(layer=layer, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("layer,name,uid,params", [
    ("MyPolicy Network", "somerulename", "", {}),
    ("MyPolicy Threat", "", "someruleuid", {}),
    ("MyPolicy Network", "", "", {"rule-number": 1, "details-level": "full"}),
])
def test_delete_access_section(core_client, mgmt_server_base_uri, layer, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-access-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.AccessSection(core_client)
        r = a.delete(layer=layer, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

# AccessLayer

@pytest.mark.parametrize("name,params", [
    ("somelayername", {}),
    ("somelayername", {"firewall": True}),
    ("somelayername", {"tags": ["fw", "app"]}),
])
def test_add_access_layer(core_client, mgmt_server_base_uri, name, params):
    endpoint = mgmt_server_base_uri + 'add-access-layer'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.AccessLayer(core_client)
        r = a.add(name=name, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,details_level", [
    ("somelayername", "", ""),
    ("", "somelayeruid", ""),
    ("somelayername", "", "uid"),
    ("", "somelayeruid", "full"),
])
def test_show_access_layer(core_client, mgmt_server_base_uri, name, uid, details_level):
    endpoint = mgmt_server_base_uri + 'show-access-layer'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.AccessLayer(core_client)
        r = c.show(name=name, uid=uid, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("somelayername", "", {"new-name": "somenewlayername"}),
    ("", "somelayeruid", {"firewall": False, "ignore-errors": True}),
])
def test_set_access_layer(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-access-layer'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.AccessLayer(core_client)
        r = c.set(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("name,uid,params", [
    ("somelayername", "", {}),
    ("", "somelayeruid", {}),
    ("somelayername", "", {'details-level': 'full'}),
    ("", "somelayeruid", {'ignore-errors': True}),
])
def test_delete_access_layer(core_client, mgmt_server_base_uri, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-access-layer'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.AccessLayer(core_client)
        r = c.delete(name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("limit,offset,order,details_level", [
    (50, 0, [], ''),
    (50, 0, [{'ASC': 'foo'}], ''),
    (64, 32, [{'DESC': 'bar'}], 'uid'),
])
def test_show_all_access_layers(core_client, mgmt_server_base_uri,
    limit, offset, order, details_level):
    endpoint = mgmt_server_base_uri + 'show-access-layers'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.AccessLayer(core_client)
        r = c.show_all(limit=limit, offset=offset,
            order=order, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

# NATRule

@pytest.mark.parametrize("package,position,params", [
    ("standard", 1, {}),
    ("standard", "bottom", {}),
    ("standard", "top", {"enabled": True, "method": "hide"}),
])
def test_add_nat_rule(core_client, mgmt_server_base_uri, package, position, params):
    endpoint = mgmt_server_base_uri + 'add-nat-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.NATRule(core_client)
        r = c.add(package=package, position=position, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("package,uid,params", [
    ("standard", "natruleuid", {}),
    ("standard", "", {"rule-number": 1, "details-level": "full"}),
])
def test_show_nat_rule(core_client, mgmt_server_base_uri, package, uid, params):
    endpoint = mgmt_server_base_uri + 'show-nat-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.NATRule(core_client)
        r = c.show(package=package, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("package,uid,params", [
    ("standard", "natruleuid", {}),
    ("standard", "", {"rule-number": 1, "enabled": False, "details-level": "full"}),
])
def test_set_nat_rule(core_client, mgmt_server_base_uri, package, uid, params):
    endpoint = mgmt_server_base_uri + 'set-nat-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.NATRule(core_client)
        r = c.set(package=package, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("package,uid,params", [
    ("standard", "natruleuid", {}),
    ("standard", "", {"rule-number": 1, "details-level": "full"}),
])
def test_delete_nat_rule(core_client, mgmt_server_base_uri, package, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-nat-rule'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.NATRule(core_client)
        r = c.delete(package=package, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("package,params", [
    ("standard", {}),
    ("standard", {"limit": 100}),
])
def test_show_all(core_client, mgmt_server_base_uri, package, params):
    endpoint = mgmt_server_base_uri + 'show-nat-rulebase'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        c = cpauto.NATRule(core_client)
        r = c.show_all(package=package, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

# NATSection

@pytest.mark.parametrize("package,position,params", [
    ("standard", "top", {}),
    ("standard", 1, {"name": "mynatsection"}),
    ("standard", "bottom", {"details-level": "full"}),
])
def test_add_nat_section(core_client, mgmt_server_base_uri, package, position, params):
    endpoint = mgmt_server_base_uri + 'add-nat-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.NATSection(core_client)
        r = a.add(package=package, position=position, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("package,name,uid,params", [
    ("standard", "natsectionname", "", {}),
    ("standard", "", "natsectionuid", {}),
    ("standard", "", "", {"details-level": "full"}),
])
def test_show_nat_section(core_client, mgmt_server_base_uri, package, name, uid, params):
    endpoint = mgmt_server_base_uri + 'show-nat-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.NATSection(core_client)
        r = a.show(package=package, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("package,name,uid,params", [
    ("standard", "natsectionname", "", {"new-name": "newnatsectionname"}),
    ("standard", "", "natsectionuid", {}),
    ("standard", "", "", {"details-level": "full"}),
])
def test_set_nat_section(core_client, mgmt_server_base_uri, package, name, uid, params):
    endpoint = mgmt_server_base_uri + 'set-nat-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.NATSection(core_client)
        r = a.set(package=package, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("package,name,uid,params", [
    ("standard", "natsectionname", "", {}),
    ("standard", "", "natsectionuid", {}),
    ("standard", "", "", {"details-level": "full"}),
])
def test_delete_nat_section(core_client, mgmt_server_base_uri, package, name, uid, params):
    endpoint = mgmt_server_base_uri + 'delete-nat-section'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        a = cpauto.NATSection(core_client)
        r = a.delete(package=package, name=name, uid=uid, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body
