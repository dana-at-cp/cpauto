# cpauto
[![Build Status](https://travis-ci.org/dana-at-cp/cpauto.svg?branch=master)](https://travis-ci.org/dana-at-cp/cpauto)

cpauto is a client library, written in Python, for the web APIs exposed via Check Point R80 management server software. The Check Point R80 management APIs provide automation and integration capabilities that were not available in previous versions of Check Point management server software.

https://sc1.checkpoint.com/documents/R80/APIs/#introduction

Behold, the power of cpauto:

```
>>> import cpauto
>>> cc = cpauto.CoreClient('admin', 'vpn123', '10.6.9.81', verify=False)
>>> r = cc.login()
>>> print(r.status_code)
200
>>> print(r.json())
{u'last-login-was-at': {u'posix': 1478636363481, u'iso-8601': u'2016-11-08T15:19-0500'}, u'uid': ...}
>>> n = cpauto.Network(cc)
>>> r = n.add('net_mgmt', { 'subnet': '10.6.9.0', 'subnet-mask': '255.255.255.0' })
>>> print(r.status_code)
200
>>> print(r.json())
{u'domain': {u'domain-type': u'domain', u'name': u'SMC User', u'uid': u'41e821a0-3720-11e3-aa6e-0800200c9fde'}, ...}
>>> r = cc.publish()
>>> print(r.status_code)
200
>>> print(r.json())
{u'task-id': u'01234567-89ab-cdef-8b0a-92e9635a47d3'}
>>> r = cc.logout()
>>> print(r.status_code)
200
>>> print(r.json())
{u'message': u'OK'}
```

# Installation
To install cpauto, simply:
```
$ pip install cpauto
```
Enjoy.
