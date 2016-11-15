# -*- coding: utf-8 -*-

import pytest
import responses
import cpauto

def prepare_core_client():
    core_client = cpauto.CoreClient('admin', 'vpn123', '10.11.12.13', verify=False)
    with responses.RequestsMock(assert_all_requests_are_fired=True) as rsps:
        body = {}
        body["sid"] = "97BVpRfN4j81ogN-V2XqGYmw3DDwIhoSn0og8PiKDiM"
        body["url"] = "https://10.11.12.13:443/web_api"
        body["uid"] = "7a13a360-9b24-40d7-acd3-5b50247be33e"
        rsps.add(responses.POST, 'https://10.11.12.13:443/web_api/login',
            json=body, status=200, content_type='application/json')

        r = core_client.login()
        assert r.status_code == 200
        assert r.json() == body
    return core_client

@pytest.fixture
def core_client():
    return prepare_core_client()

@pytest.fixture
def mgmt_server_base_uri():
    return 'https://10.11.12.13:443/web_api/'
