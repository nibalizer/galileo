#!/bin/bash


#set -e # abort program after the first test fails


failed=false
boogerd_url='localhost:5000'

if netstat -antlp 2>/dev/null | grep 5000 >/dev/null 2>&1 ; then
  echo -n .
else
  echo "TEST 0 failed"
  echo "Are you running a boogerd instance?"
  exit 1
fi

if which jq >/dev/null
then
  echo -n .
else
  echo "TEST 0.1 failed"
  echo "jq not in path, required for testing"
  exit 1
fi

if curl -s $boogerd_url/v1/ticket/281 | grep 'Sun, 11 Jan 2015' >/dev/null
then
  echo -n .
else
  echo "TEST 1 failed"
  exit 1
fi


# The following test assumes that 247 has been flagged wintel and hiss
flags_247_output=`curl -s $boogerd_url/v1/ticket/247/flags`
if echo $flags_247_output | jq '.flags[0]' | grep 'WINTEL' >/dev/null
then
  echo -n .
else
  echo "TEST 2.1 failed"
  exit 1
fi

if echo $flags_247_output | jq '.flags[1]' | grep 'HISS' >/dev/null
then
  echo -n .
else
  echo "TEST 2.2 failed"
  exit 1
fi

if echo $flags_247_output | jq '.flags[2]' | grep 'null' >/dev/null
then
  echo -n .
else
  echo "TEST 2.3 failed"
  exit 1
fi

if curl -s $boogerd_url/v1/all_flags | grep CHRONICLE >/dev/null
then
  echo -n .
else
  echo "TEST 3 failed"
  exit 1
fi

if curl -s $boogerd_url/v1/ticket/247/assigned | grep 'nibz' >/dev/null
then
  echo -n .
else
  echo "TEST 4 failed"
  exit 1
fi

output=`curl -s $boogerd_url/v1/ticket/247/metadata`
if echo $output | grep '"assigned_to": "nibz@cat.pdx.edu",' >/dev/null
then
  echo -n .
else
  echo "TEST 5 failed"
  exit 1
fi

if echo $output | grep '"summary_email": "andywood@cat.pdx.edu",' >/dev/null
then
  echo -n .
else
  echo "TEST 6 failed"
  exit 1
fi

if echo $output | grep '"subject": "Your linux session has been terminated.",' >/dev/null
then
  echo -n .
else
  echo "TEST 7 failed"
  exit 1
fi


if curl -s -XPOST -d '{ "user": "blkperl@cat.pdx.edu" }' $boogerd_url/v1/ticket/247/assign | grep '"assigned": "blkperl@cat.pdx.edu",' >/dev/null
then
  echo -n .
else
  echo "TEST 8 failed"
  exit 1
fi

if curl -s $boogerd_url/v1/ticket/247/assigned | grep '"assigned": "blkperl@cat.pdx.edu",' >/dev/null
then
  echo -n .
else
  echo "TEST 9 failed"
  exit 1
fi

if curl -s -XPOST $boogerd_url/v1/ticket/247/unassign | grep ' "assigned": false,' >/dev/null
then
  echo -n .
else
  echo "TEST 10 failed"
  exit 1
fi

curl -s -XPOST -d '{ "user": "nibz@cat.pdx.edu" }' $boogerd_url/v1/ticket/247/assign >/dev/null

#ticket 259
#post an update
#confirm that it is open
#close it
#confirm that it is closed

if curl -s -XPOST -d '{ "message": "I am groot", "user": "nibz@cat.pdx.edu" }' $boogerd_url/v1/ticket/259/update | grep 'groot'  >/dev/null
then
  echo -n .
else
  echo "TEST 11.1 failed"
  exit 1
fi
sleep 5

if curl -s $boogerd_url/v1/ticket/259/metadata | jq ".status" | grep 'open'  >/dev/null
then
  echo -n .
else
  echo "TEST 11.2 failed"
  exit 1
fi

if curl -s -XPOST $boogerd_url/v1/ticket/259/close | grep 'Completing ticket #259'  >/dev/null
then
  echo -n .
else
  echo "TEST 11.3 failed"
  exit 1
fi

sleep 5
if curl -s $boogerd_url/v1/ticket/259/metadata | jq ".status" | grep 'completed'  >/dev/null
then
  echo -n .
else
  echo "TEST 11.4 failed"
  exit 1
fi


echo ""
echo "All tests pass!"

