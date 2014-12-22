#!/bin/bash


set -e # abort program after the first test fails


boogerd_url='localhost:5000'

#curl -XGET -H 'Content-Type: application/json' -d '{ "ticket_number": "249" }' localhost:5000/v1/ticket/get
curl -s $boogerd_url/v1/ticket/247 | grep 'NUMBER:        247' >/dev/null
echo -n .

curl -s $boogerd_url/v1/ticket/247/flags | grep 'WINTEL,HISS' >/dev/null
echo -n .

curl -s $boogerd_url/v1/all_flags | grep CHRONICLE >/dev/null
echo -n .


echo ""
echo "All tests pass!"

