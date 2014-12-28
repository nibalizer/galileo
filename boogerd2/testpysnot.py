
# Testing code for pysnot
# tested with snot database
# assumes ticket 11440 doesn't exist
# makes some assumptions about initial states of tickets 250 - 260


import datetime
import os

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




