#!/bin/bash
set -e

if [ "$ENV" = 'UNIT' ]; then 
  echo "Running Unit Tests"
  exec python "tests.py"
else
  echo "Running Production Server"
  exec python "app.py"
fi
