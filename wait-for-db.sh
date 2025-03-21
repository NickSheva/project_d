#!/bin/sh

until pg_isready -h db -U railway -d railway; do
  echo "Waiting for PostgreSQL to start..."
  sleep 2
done