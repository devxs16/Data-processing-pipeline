#!/bin/bash

echo "Checking if Django server is running..."

curl http://127.0.0.1:8000/

echo ""
echo "Health check completed."