FROM solr:8.10

COPY dataset/data.json /data/data.json

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

COPY src/synonyms.txt /data/synonyms.txt

ENTRYPOINT ["/scripts/startup.sh"]
