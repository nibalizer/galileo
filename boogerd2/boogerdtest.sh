#!/bin/bash


#set -e # abort program after the first test fails


failed=false
boogerd_url='localhost:5000'

if netstat -antlp 2>/dev/null | grep 5000 >/dev/null 2>&1 ; then
  :
else
  echo "Are you running a boogerd instance?"
  exit 1
fi

if curl -s $boogerd_url/v1/ticket/247 | grep 'NUMBER:        247' >/dev/null
then
  echo -n .
else
  echo "TEST #1 failed"
  exit 1
fi

if curl -s $boogerd_url/v1/ticket/247/flags | grep 'WINTEL,HISS' >/dev/null
then
  echo -n .
else
  echo "TEST #2 failed"
  exit 1
fi

if curl -s $boogerd_url/v1/all_flags | grep CHRONICLE >/dev/null
then
  echo -n .
else
  echo "TEST #3 failed"
  exit 1
fi


echo ""
echo "All tests pass!"

