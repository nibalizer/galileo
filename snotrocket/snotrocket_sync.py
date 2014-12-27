#!/usr/bin/python

# application to follow the snot log and refresh the snotrocket
# cache as necessary

# doesn't return, must be run as a daemon

from elasticsearch import Elasticsearch
import tailer

from snotrocket_populate import import_ticket
import snotparser.snotparser as sp

snot_log = '/u/snot/test/logs/log'
#snot_log = 'test_log' # for testing
es_index = 'snotrocket'

es = Elasticsearch()


# Follow the snot log file
for line in tailer.follow(open(snot_log)):
    print line
    ticket_number = int(line.split()[9])
    print "processing updates to ticket {0}".format(ticket_number)
    import_ticket(ticket_number, es_index)


