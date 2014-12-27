#!/usr/bin/python

# snotrocket_populate

# script to do a one time population of snot tickets into elasticsearch

# core imports
from datetime import datetime
import os

# pip imports
from elasticsearch import Elasticsearch

# custom imports
import snotparser.snotparser as sp

# by default we connect to localhost:9200
es = Elasticsearch()



def import_ticket(ticket, es_index):
    t = int(ticket)
    parsed_data = sp.parseTicket(t, 'testsnot')
    b = es.index(index=es_index, doc_type="snot-ticket", id=ticket, body=parsed_data)


def initial_import(active_dir, es_index):
    """
    import every snot ticket in active_dir into a snot index
    called es_index
    """
    tickets = os.listdir(active_dir)
    tickets.remove('bounds')
    tickets.remove('index')
    for ticket in tickets:
        t = int(ticket)
        import_ticket(t, es_index)
        print ticket, parsed_data['status']


if __name__ == "__main__":
    #initial_import('/u/snot/test/spool/active', 'snotrocket')
    import_ticket(264, 'snotrocket')
