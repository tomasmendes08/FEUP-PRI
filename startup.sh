#!/bin/bash

precreate-core movies

# Start Solr in background mode so we can use the API to upload the schema
solr start

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema.json \
    http://localhost:8983/solr/movies/schema

# Populate collection
bin/post -c movies /data/movies.csv


# Restart in foreground mode so we can access the interface
solr restart -f

