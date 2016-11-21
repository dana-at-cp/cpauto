# -*- coding: utf-8 -*-

"""Tests for cpauto.core.misc module."""

import pytest
import responses
import cpauto

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
    endpoint = mgmt_server_base_uri + 'run-script'
    with responses.RequestsMock() as rsps:
        resp_body = {'foo': 'bar', 'message': 'OK'}
        rsps.add(responses.POST, endpoint,
                 json=resp_body, status=200,
                 content_type='application/json')

        m = cpauto.Misc(core_client)
        r = m.run_script(script=script, name=name, targets=targets, params=params)

        assert r.status_code == 200
        assert r.json() == resp_body

@pytest.mark.parametrize("content,name,path,targets,comments", [
    ("This is only a test.", "test.txt", "/home/admin/", "gw-2200", "Test file."),
])
def test_set(core_client, mgmt_server_base_uri, content, name, path, targets, comments):
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
