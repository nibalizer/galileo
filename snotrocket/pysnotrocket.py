#!/usr/bin/python


# pip imports
from elasticsearch import Elasticsearch

es = Elasticsearch()

es_index = 'snotrocket'

def get_ticket_by_uuid(uuid):
    res = es.search(index=es_index, body={"query": {"match": {"boogerd_uuid": uuid }}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
            print hit['_source']['number']
    return res['hits']['hits'][0]['_source']


def get_ticket_by_number(ticket_number):
    res = es.search(index=es_index, body={"query": {"match": {"number": ticket_number}}})
    print("Got %d Hits:" % res['hits']['total'])
    for hit in res['hits']['hits']:
            print hit['_source']['number']
    return res['hits']['hits'][0]['_source']


def get_open_tickets(index_from=0, size=20):
    res = es.search(index=es_index, body={"sort": [ {"number": "asc" }], "from": index_from, "size": size, "query": {"match": {"status": "open"}}})
    #print("Got %d Hits:" % res['hits']['total'])
    tickets = [i['_source'] for i in res['hits']['hits'] ]
    number_responses = res['hits']['total']
    return number_responses, tickets


if __name__ == "__main__":
    #print get_ticket_by_uuid('8449fae6-f97d-43b1-8c51-cb6c87990b11')
    #print get_ticket_by_number(247)
    print get_open_tickets()
