#!/usr/bin/python

from elasticsearch import Elasticsearch

es = Elasticsearch()

es_index = 'snotrocket'


from pysnotrocket import *


assert(get_ticket_by_number(247)['flags'] == 'WINTEL,HISS')
# Note that the following test fails if you ever reset the ES store
# From the snot files(db)
# This is because the uuids are generated on the fly and only ever
# written down in ES. This is okay because they are only short lived
# pointers that boogerd hands out to refer to tickets until their
# ticket number is assigned by snot
uuid_tic = get_ticket_by_uuid('db9e0124-840f-47c0-92e4-6dfb8cdf8969')

assert(uuid_tic['from_line'] == 'nibz@cat.pdx.edu')
num_tickets, tickets = get_open_tickets()
assert(len(tickets) == 20)
assert(num_tickets > 100)


