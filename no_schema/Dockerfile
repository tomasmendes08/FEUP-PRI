FROM solr:8.10

COPY data.json /data/data.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
