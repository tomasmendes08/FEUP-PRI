FROM solr:8.10

ADD models /models

ADD ltr /ltr

COPY dataset/data.json /data/data.json

COPY dataset/Refined/rt_reviews.csv /data/reviews.csv

COPY schema_movies.json /data/schema_movies.json

COPY schema_reviews.json /data/schema_reviews.json

COPY config.json /data/config.json

COPY config.xml config.xml

COPY startup.sh /scripts/startup.sh

COPY synonyms/synonyms_fix.txt /data/synonyms.txt

ENTRYPOINT ["/scripts/startup.sh"]
