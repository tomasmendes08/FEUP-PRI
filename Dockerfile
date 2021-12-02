FROM solr:8.10

COPY dataset/Refined/final_movies.csv /data/movies.csv

COPY dataset/Refined/imdb_ratings.csv /data/imdb_ratings.csv

COPY dataset/Refined/rt_reviews.csv /data/rt_reviews.csv

COPY schema.json /data/schema.json

COPY startup.sh /scripts/startup.sh

ENTRYPOINT ["/scripts/startup.sh"]
