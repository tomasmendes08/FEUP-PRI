# SETUP
import matplotlib.pyplot as plt
from sklearn.metrics import PrecisionRecallDisplay
import numpy as np
import json
import requests
import pandas as pd
from itertools import cycle

# setup plot details
colors = cycle(["navy", "turquoise", "darkorange", "cornflowerblue", "teal"])

QRELS_FILE = "queries/query1.txt"

QUERY_URL_NORMAL = "http://localhost:8983/solr/movies/select?bq=genres%3A%22Science%20Fiction%20%26%20Fantasy%22&defType=dismax&fq=available_netflix%3A%20%22True%22&indent=true&q.op=OR&q=space%20sci-fi&qf=original_title%20movie_info%20review_content&rows=88"
QUERY_URL_BOOSTED = "http://localhost:8983/solr/movies/select?bq=genres%3A%22Science%20Fiction%20%26%20Fantasy%22%5E30&defType=dismax&fq=available_netflix%3A%20%22True%22&indent=true&q.op=OR&q=space%20sci-fi&qf=genres%20original_title%5E10%20movie_info%5E50%20review_content%5E20&rows=88"

relevant_list = [x.split(" ")[0] for x in open(QRELS_FILE).readlines()]

relevant = list(map(lambda el: el.strip(), relevant_list))

# Read qrels to extract relevant documents
# relevant = list(map(lambda el: el.strip(), open(QRELS_FILE).readlines()))
# Get query results from Solr instance

results_noschema = json.load(open('queries/query1/noschema.json', encoding="utf8"))['response']['docs']
results_normal = requests.get(QUERY_URL_NORMAL).json()['response']['docs']
results_boosted = requests.get(QUERY_URL_BOOSTED).json()['response']['docs']

results_list = [results_noschema, results_normal, results_boosted]

_, ax = plt.subplots(figsize=(7, 8))

i=0
for results, color in zip(results_list, colors):
    # PRECISION-RECALL CURVE
    # Calculate precision and recall values as we move down the ranked list
    precision_values = [
        len([
            doc 
            for doc in results[:idx]
            if doc['id'] in relevant
        ]) / idx 
        for idx, _ in enumerate(results, start=1)
    ]

    recall_values = [
        len([
            doc for doc in results[:idx]
            if doc['id'] in relevant
        ]) / len(relevant)
        for idx, _ in enumerate(results, start=1)
    ]

    precision_recall_match = {k: v for k,v in zip(recall_values, precision_values)}

    # Extend recall_values to include traditional steps for a better curve (0.1, 0.2 ...)
    recall_values.extend([step for step in np.arange(0.1, 1.1, 0.1) if step not in recall_values])
    recall_values = sorted(set(recall_values))

    # Extend matching dict to include these new intermediate steps
    for idx, step in enumerate(recall_values):
        if step not in precision_recall_match:
            if recall_values[idx-1] in precision_recall_match:
                precision_recall_match[step] = precision_recall_match[recall_values[idx-1]]
            else:
                precision_recall_match[step] = precision_recall_match[recall_values[idx+1]]

    disp = PrecisionRecallDisplay([precision_recall_match.get(r) for r in recall_values], recall_values)
    if(i==0):
        disp.plot(ax=ax, name=f"Precision-recall without schema", color=color, linewidth=1)
    elif(i==1):
        disp.plot(ax=ax, name=f"Precision-recall without boost", color=color, linewidth=1)
    elif(i==2):
        disp.plot(ax=ax, name=f"Precision-recall with boost", color=color, linewidth=1.5)
    i+=1

# add the legend for the iso-f1 curves
handles, labels = disp.ax_.get_legend_handles_labels()

# set the legend and the axes
ax.legend(handles=handles, labels=labels, loc="best")
ax.set_title("Precision-Recall curve to Query 1")

plt.savefig('precision_recall.png')