# -*- coding: utf-8 -*-

"""Tests for cpauto.core.misc module."""

import pytest
import responses
import cpauto

slow = pytest.mark.skipif(
    not pytest.config.getoption("--slow"),
    reason="Use the --slow option to run"
)

@pytest.mark.parametrize("task_id,details_level", [
    ("sometaskid", ""),
    ("sometaskid", "full"),
])
def test_show_task(core_client, mgmt_server_base_uri, task_id, details_level):
    endpoint = mgmt_server_base_uri + 'show-task'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        m = cpauto.Misc(core_client)
        r = m.show_task(task_id=task_id, details_level=details_level)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("script,name,targets,params", [
    ("ls -al / > /home/admin/script.txt", "List Files in Root Dir", "gw-2200", {}),
    ("ls -al / > /home/admin/script.txt", "List Files in Root Dir", "gw-2200", {"comments": "This is a comment."}),
])
def test_run_script(core_client, mgmt_server_base_uri, script, name, targets, params):
    # positive test
    endpoint_0 = mgmt_server_base_uri + 'run-script'
    resp_body_0 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'target': 'gw-2200'}]}
    endpoint_1 = mgmt_server_base_uri + 'show-task'
    resp_body_1 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'succeeded'}]}
    endpoint_2 = mgmt_server_base_uri + 'show-task'
    resp_body_2 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'succeeded'}]}
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST, endpoint_0,
                 json=resp_body_0, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_1,
                 json=resp_body_1, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_2,
                 json=resp_body_2, status=200,
                 content_type='application/json')

        m = cpauto.Misc(core_client)
        r = m.run_script(script=script, name=name, targets=targets, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body_2

    # negative test
    endpoint_0 = mgmt_server_base_uri + 'run-script'
    resp_body_0 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'target': 'gw-2200'}]}
    endpoint_1 = mgmt_server_base_uri + 'show-task'
    resp_body_1 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'failed'}]}
    endpoint_2 = mgmt_server_base_uri + 'show-task'
    resp_body_2 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'failed'}]}
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST, endpoint_0,
                 json=resp_body_0, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_1,
                 json=resp_body_1, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_2,
                 json=resp_body_2, status=200,
                 content_type='application/json')

        m = cpauto.Misc(core_client)
        r = m.run_script(script=script, name=name, targets=targets, params=params)

        assert r.status_code == 200
        assert r.success == False
        assert r.message == "There was at least one task that failed or partially succeeded"
        assert r.json() == resp_body_2

@slow
@pytest.mark.parametrize("script,name,targets,params", [
    ("ls -al / > /home/admin/script.txt", "List Files in Root Dir", "gw-2200", {}),
])
def test_run_script_slow(core_client, mgmt_server_base_uri, script, name, targets, params):
    endpoint_0 = mgmt_server_base_uri + 'run-script'
    resp_body_0 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'target': 'gw-2200'}]}
    endpoint_1 = mgmt_server_base_uri + 'show-task'
    resp_body_1 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'in progress', 'progress-percentage': 0}]}
    endpoint_2 = mgmt_server_base_uri + 'show-task'
    resp_body_2 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'in progress', 'progress-percentage': 25}]}
    endpoint_3 = mgmt_server_base_uri + 'show-task'
    resp_body_3 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'in progress', 'progress-percentage': 50}]}
    endpoint_4 = mgmt_server_base_uri + 'show-task'
    resp_body_4 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'in progress', 'progress-percentage': 75}]}
    endpoint_5 = mgmt_server_base_uri + 'show-task'
    resp_body_5 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'succeeded', 'progress-percentage': 100}]}
    endpoint_6 = mgmt_server_base_uri + 'show-task'
    resp_body_6 = {'tasks': [{'task-id': 'ef71cf6c-0066-48ca-85be-4d661802fe80', 'status': 'succeeded', 'progress-percentage': 100}]}
    with responses.RequestsMock() as rsps:
        rsps.add(responses.POST, endpoint_0,
                 json=resp_body_0, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_1,
                 json=resp_body_1, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_2,
                 json=resp_body_2, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_3,
                 json=resp_body_3, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_4,
                 json=resp_body_4, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_5,
                 json=resp_body_5, status=200,
                 content_type='application/json')
        rsps.add(responses.POST, endpoint_6,
                 json=resp_body_6, status=200,
                 content_type='application/json')

        m = cpauto.Misc(core_client)
        r = m.run_script(script=script, name=name, targets=targets, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body_6

@pytest.mark.parametrize("content,name,path,targets,comments", [
    ("This is only a test.", "test.txt", "/home/admin/", "gw-2200", "Test file."),
])
def test_put_file(core_client, mgmt_server_base_uri, content, name, path, targets, comments):
    endpoint = mgmt_server_base_uri + 'put-file'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        m = cpauto.Misc(core_client)
        r = m.put_file(content=content, name=name, path=path,
                       targets=targets, comments=comments)

        assert r.status_code == 200
        assert r.json() == resp_body
