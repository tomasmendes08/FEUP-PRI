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

QRELS_FILE = "queries/query4.txt"

QUERY_URL_NORMAL = "http://localhost:8983/solr/movies/select?defType=dismax&indent=true&q.op=AND&q=true%20crime%20story&qf=review_content%20movie_info&rows=54"
QUERY_URL_BOOSTED = "http://localhost:8983/solr/movies/select?defType=dismax&indent=true&pf=review_content%5E50&ps=3&q.op=AND&q=true%20crime%20story&qf=review_content%20movie_info%5E30&rows=54"


# Read qrels to extract relevant documents
relevant_list = [x.split(" ")[0] for x in open(QRELS_FILE).readlines()]
relevant = list(map(lambda el: el.strip(), relevant_list))

# Get query results from Solr instance

results_noschema = json.load(open('queries/query4/noschema.json', encoding="utf8"))['response']['docs']
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
            if doc['imdb_title_id'] in relevant
        ]) / idx 
        for idx, _ in enumerate(results, start=1)
    ]

    recall_values = [
        len([
            doc for doc in results[:idx]
            if doc['imdb_title_id'] in relevant
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

ax.set_ylim([0, 1])
ax.set_xlim([0, 1])

# set the legend and the axes
ax.legend(handles=handles, labels=labels, loc="best")
ax.set_title("Precision-Recall curve to Query 4")

plt.savefig('queries/query4/precision_recall4.png')


