#!/usr/bin/python

# Tests for snotrocket_sync

# These tests are functions so we can import them in the pysnot
# tests and integrate them there

import time

import requests

"""
>>> r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
>>> r.status_code
200
>>> r.headers['content-type']
'application/json; charset=utf8'
>>> r.encoding
'utf-8'
>>> r.text
u'{"type":"User"...'
>>> r.json()
{u'private_gists': 419, u'total_private_repos': 77, ...}
"""

def validate_assigned(ticket_number, assigned_to):
    time.sleep(1)
    r = requests.get('http://localhost:9200/snotrocket/snot-ticket/{0}'.format(ticket_number))
    actually_assigned_to = r.json()['_source'].get('assigned_to')
    #print "debug"
    #print actually_assigned_to, assigned_to
    assert(actually_assigned_to == assigned_to)
