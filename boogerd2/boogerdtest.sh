#!/bin/bash


#set -e # abort program after the first test fails


failed=false
boogerd_url='localhost:5000'

if netstat -antlp 2>/dev/null | grep 5000 >/dev/null 2>&1 ; then
  echo -n .
else
  echo "TEST #0 failed"
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

if curl -s $boogerd_url/v1/ticket/247/assigned | grep 'nibz' >/dev/null
then
  echo -n .
else
  echo "TEST #4 failed"
  exit 1
fi

output=`curl -s $boogerd_url/v1/ticket/247/metadata`
if echo $output | grep '"assigned_to": "nibz",' >/dev/null
then
  echo -n .
else
  echo "TEST #5 failed"
  exit 1
fi

if echo $output | grep '"summary_email": "andywood@cat.pdx.edu",' >/dev/null
then
  echo -n .
else
  echo "TEST #6 failed"
  exit 1
fi

if echo $output | grep '"subject": "Your linux session has been terminated.",' >/dev/null
then
  echo -n .
else
  echo "TEST #7 failed"
  exit 1
fi


echo ""
echo "All tests pass!"

