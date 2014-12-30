
# Testing code for pysnot
# tested with snot database
# assumes ticket 11440 doesn't exist
# makes some assumptions about initial states of tickets 137, 250 - 260


import datetime
import os
import time

import pysnot
from test_snotrocket_sync import *

class ShitsFucked(Exception):
    pass

# if the enviornment variable TEST_SNOTROCKET is set to 'true'
# then validate the changes done here are reflected in the snot
# rocket cache (elasticsearch)
# make sure you are actually running snotrocket_sync :P
# TODO: make elasticsearch url setable
# TODO: create, use, and clean a unique elasticsearch index


run_snotrocket_tests = False
if os.environ.get('TEST_SNOTROCKET') == 'true':
    run_snotrocket_tests = True


#test stat_ticket

assert(True == pysnot.stat_ticket(252))
assert(False == pysnot.stat_ticket(11440))


# test get assigned
assert('monkc' == pysnot.get_assigned(20))
assert(None == pysnot.get_assigned(117))
try:
    a = pysnot.get_assigned(11440)
except pysnot.TicketNotFoundException:
    pass
else:
    raise ShitsFucked('Expected exception not thrown')


# 255
# Should start assigned to nibz (testsnot -R nibz 255)
# Then get assigned to cawil
# Then get assigned back to nibz
assert('nibz' == pysnot.get_assigned(255))
assert(True == pysnot.assign_ticket_with_validation(255, 'cawil'))
run_snotrocket_tests and validate_assigned(255, 'cawil')
assert('cawil' == pysnot.get_assigned(255))
assert(True == pysnot.assign_ticket(255, 'nibz'))
assert('nibz' == pysnot.get_assigned(255))
run_snotrocket_tests and validate_assigned(255, 'nibz')

# 256
# Should start unassigned (testsnot -R nobody 256)
# Assign to nibz
# Reassign to nibz (should succeed)
# Reassign to nibz with validation (should succeed)
# Unsassign
assert(None == pysnot.get_assigned(256))
assert(True == pysnot.assign_ticket(256, 'nibz'))
run_snotrocket_tests and validate_assigned(256, 'nibz')
assert('nibz' == pysnot.get_assigned(256))
assert(True == pysnot.assign_ticket(256, 'nibz'))
assert('nibz' == pysnot.get_assigned(256))
assert(True == pysnot.assign_ticket_with_validation(256, 'nibz'))
assert('nibz' == pysnot.get_assigned(256))
assert(True == pysnot.unassign_ticket(256))
assert(None == pysnot.get_assigned(256))
run_snotrocket_tests and validate_assigned(256, None)

# 257 Reserved for future use

tic = pysnot.get_metadata(255)
assert(tic['summary_email'] == 'nibz@cat.pdx.edu')
assert(tic['number'] == 255)

# Ticket 137

tic_history = pysnot.get_history(137)
assert(tic_history[0] == 'Wed Oct 22 04:23:46 PM 2014 CMD: RECV TKT: 137 BY: finnre@cat.pdx.edu')
assert(tic_history[1] == 'Wed Oct 22 04:31:13 PM 2014 CMD: UPDATE TKT: 137 BY: rubins@cat.pdx.edu')

tic_267_involved = pysnot.get_emails_involved(267)
assert(tic_267_involved == ['blkperl@cat.pdx.edu',
    'nibz@cat.pdx.edu',
    'cmurphy@cat.pdx.edu',
    'testtrouble@cat.pdx.edu',
    'bucknerb@cat.pdx.edu'])


# ticket 268
# keep sending messages to it and evaluate
now = str(datetime.datetime.now())
pysnot.update_ticket(268, message="Testing pysnot: {0}".format(now))
time.sleep(5)
ticket_268 = pysnot.get_ticket(268)
assert(now in str(ticket_268))

