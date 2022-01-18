import numpy as np
import requests
import simplejson

# Number of documents to be re-ranked.
RERANK = 40
with open("RERANK.int", "w") as f:
    f.write(str(RERANK))

QRELS_FILE = "../src/queries/query4.txt"

relevant_docs = [x.split(" ")[0] for x in open(QRELS_FILE).readlines()]

# Build query URL.
q_id = "q4"
# text_a = "Christmas"
# text_b = "Christmas time"
# text = "Christmas time"

# url = "http://localhost:8983/solr/movies/query"
# url += "?q={0}&df=movie_info&rq={{!ltr model=my_efi_model ".format(text)
# url += "efi.text='{0}' efi.text_a='{1}' efi.text_b='{2}'}}".format(text,text_a, text_b)
# url += "&qf=original_title^1 movie_info^5 review_content^2&q.op=AND&defType=dismax&ps=5&pf=review_content^4&fq=genres:%22Kids%20%26%20Family%22"
# url += "&fl=id,original_title,imdb_title_id,score,[features]&rows={0}".format( RERANK)

url = "http://localhost:8983/solr/movies/query?q=space%20sci-fi&q.op=OR&defType=dismax&indent=true&qf=genres%20original_title%5E1%20movie_info%5E5%20review_content%5E2&bq=genres:%22Science%20Fiction%20%26%20Fantasy%22%5E3&rows=50&fl=*,id,score,%5Bfeatures%5D&rq=%7B!ltr%20model%3Dmy_efi_model%20efi.text%3D%22space%20sci-fi%22%7D&fq=available_netflix:%20%22True%22"

# Get response and check for errors.
response = requests.request("GET", url)
try:
    json = simplejson.loads(response.text)
except simplejson.JSONDecodeError:
    print(q_id)

if "error" in json:
    print(q_id)

# Extract the features.
results_features = []
results_targets = []
results_ranks = []
add_data = False

for (rank, document) in enumerate(json["response"]["docs"]):

    features = document["[features]"].split(",")
    feature_array = []
    for feature in features:
        feature_array.append(feature.split("=")[1])

    feature_array = np.array(feature_array, dtype = "float32")
    results_features.append(feature_array)

    doc_id = document["imdb_title_id"]
    # Check if document is relevant to query.
    # if q_id in relevant.get(doc_id, {}):
    if doc_id in relevant_docs:
        results_ranks.append(rank + 1)
        results_targets.append(1)
        add_data = True
    else:
        results_targets.append(0)

if add_data:
    np.save("ranking_results/{0}_X.npy".format(q_id), np.array(results_features))
    np.save("ranking_results/{0}_y.npy".format(q_id), np.array(results_targets))
    np.save("ranking_results/{0}_rank.npy".format(q_id), np.array(results_ranks))