#!/bin/bash

precreate-core movies

precreate-core reviews

# Start Solr in background mode so we can use the API to upload the schema

sed -i $'/<\/config>/{e cat config.xml\n}' /var/solr/data/movies/conf/solrconfig.xml

solr start -Dsolr.ltr.enabled=true

cp /data/synonyms.txt /var/solr/data/movies/conf

cp /models/en-ner-person.bin /var/solr/data/movies/conf/en-ner-person.bin

cp /models/en-sent.bin /var/solr/data/movies/conf/en-sent.bin

cp /models/en-token.bin /var/solr/data/movies/conf/en-token.bin

cp /models/en-chunker.bin /var/solr/data/movies/conf/en-chunker.bin

cp /models/en-pos-maxent.bin /var/solr/data/movies/conf/en-pos-maxent.bin

cp /models/en-lemmatizer-dict.txt /var/solr/data/movies/conf/en-lemmatizer-dict.txt

cp /models/stop.pos.txt /var/solr/data/movies/conf/stop.pos.txt

cp /models/en-ner-person.bin /var/solr/data/movies/conf/en-ner-person.bin

sleep 15
# Schema definition via API

# curl -X POST -H 'Content-type:application/json' \
#     --data-binary @/data/config.json \
#     http://localhost:8983/solr/movies/config

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema_movies.json \
    http://localhost:8983/solr/movies/schema

curl -X POST -H 'Content-type:application/json' \
    --data-binary @/data/schema_reviews.json \
    http://localhost:8983/solr/reviews/schema

curl -XPUT -H 'Content-type:application/json' \
    --data-binary @/ltr/ltr_features.json \
    http://localhost:8983/solr/movies/schema/feature-store

curl -XPUT -H 'Content-type:application/json' \
    --data-binary @/ltr/ltr_model.json \
    http://localhost:8983/solr/movies/schema/model-store
	

# Populate collection
bin/post -c movies /data/data.json

bin/post -c reviews /data/reviews.csv


# Restart in foreground mode so we can access the interface
solr restart -f

