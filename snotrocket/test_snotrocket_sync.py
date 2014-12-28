#!/usr/bin/python

# Tests for snotrocket_sync

# These tests are functions so we can import them in the pysnot
# tests and integrate them there

import time

import requests


def validate_assigned(ticket_number, assigned_to):
    time.sleep(1)
    url = 'http://localhost:9200/snotrocket/snot-ticket/'
    r = requests.get(url + ticket_number)
    actually_assigned_to = r.json()['_source'].get('assigned_to')
    #print "debug"
    #print actually_assigned_to, assigned_to
    assert(actually_assigned_to == assigned_to)
