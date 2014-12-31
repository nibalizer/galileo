#!/usr/bin/python

from elasticsearch import Elasticsearch

es = Elasticsearch()

es_index = 'snotrocket'


from pysnotrocket import *


assert(get_ticket_by_number(247)['flags'] == 'WINTEL,HISS')
uuid_tic = get_ticket_by_uuid('8449fae6-f97d-43b1-8c51-cb6c87990b11')

assert(uuid_tic['from_line'] == 'nibz@cat.pdx.edu')
num_tickets, tickets = get_open_tickets()
assert(len(tickets) == 20)
assert(num_tickets > 100)


