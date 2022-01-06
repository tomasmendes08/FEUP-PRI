#!/bin/bash

precreate-core movies

precreate-core reviews

# Start Solr in background mode so we can use the API to upload the schema
solr start

sleep 7

cp /data/synonyms.txt /var/solr/data/movies/conf

# Schema definition via API
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema_movies.json \
    http://localhost:8983/solr/movies/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema_reviews.json \
    http://localhost:8983/solr/reviews/schema
	
curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/config.json \
    http://localhost:8983/solr/movies/config

# Populate collection
bin/post -c movies /data/data.json

bin/post -c reviews /data/reviews.csv


# Restart in foreground mode so we can access the interface
solr restart -f

