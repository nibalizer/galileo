#!/bin/bash



uuid_test=`curl -s http://localhost:5001/v1/tickets/uuid/db9e0124-840f-47c0-92e4-6dfb8cdf8969`
if echo $uuid_test | grep "db9e0124-840f-47c0-92e4-6dfb8cdf8969" >/dev/null; then
  echo -n .
else
  echo "TEST 1.1 failed"
  exit 1
fi

if echo $uuid_test | grep "printer is busted" >/dev/null; then
  echo -n .
else
  echo "TEST 1.2 failed"
  exit 1
fi

echo
echo "All tests passed!"
