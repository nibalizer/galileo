#!/bin/bash


boogerd_url='localhost:5000'

#curl -XGET -H 'Content-Type: application/json' -d '{ "ticket_number": "249" }' localhost:5000/v1/ticket/get
curl $boogerd_url/v1/ticket/get/249
