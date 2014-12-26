# core imports
from datetime import datetime
import os

# pip imports
from elasticsearch import Elasticsearch

# custom imports
import snotparser.snotparser as sp

# by default we connect to localhost:9200
es = Elasticsearch()


# datetimes will be serialized
#es.index(index="my-index", doc_type="test-type", id=42, body={"any": "data", "timestamp": datetime.now()})

# but not deserialized
#print es.get(index="my-index", doc_type="test-type", id=42)['_source']

def import_ticket(ticket, es_index):
    t = int(ticket)
    parsed_data = sp.parseTicket(t, 'testsnot')
    es.index(index=es_index, doc_type="snot-ticket", id=ticket, body=parsed_data)


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




def random_crap():
    ticket_number=100023
    parsed_data = sp.parseTicket(100023, 'testsnot')
    #print parsed_data
    #print es.get(index="snotrocket", doc_type="snot-ticket", id=ticket_number)
    a = datetime.now()
    print es.get(index="snotrocket", doc_type="snot-ticket", id=ticket_number)
    b = datetime.now()
    parsed_data = sp.parseTicket(100023)
    print parsed_data
    c = datetime.now()

    print b - a
    print c - b



if __name__ == "__main__":
    #initial_import('/u/snot/test/spool/active', 'snotrocket')
    import_ticket(261, 'snotrocket')
    #random_crap()
