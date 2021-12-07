FROM solr:8.10

COPY dataset/Refined/data.json /data/data.json

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
