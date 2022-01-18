import itertools
import numpy as np
import sklearn as sk
import pandas as pd
import requests
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import classification_report, plot_confusion_matrix
from sklearn import svm, linear_model
from pairwiseSVM import RankSVM
from sklearn.model_selection import KFold
import pairwiseSVM


import simplejson

qrels_prefix = "../../src/queries/query"
qrels_sufix = ".txt"

queries_urls = [
    "http://localhost:8983/solr/movies/select?bq=genres%3A%22Science%20Fiction%20%26%20Fantasy%22%5E3&defType=dismax&fl=*%2Cid%2Cscore%2C%5Bfeatures%5D&fq=available_netflix%3A%20%22True%22&indent=true&q.op=OR&q=space%20sci-fi&qf=genres%20original_title%5E1%20movie_info%5E5%20review_content%5E2&rows=50&rq=%7B!ltr%20model%3Dmy_efi_model%20efi.text%3D%22space%20sci-fi%22%20reRankDocs%3D50%7D",
    "http://localhost:8983/solr/movies/select?defType=dismax&fl=*%2Cid%2Cscore%2C%5Bfeatures%5D&indent=true&q.op=OR&q=slavery%20slave&qf=original_title%5E1%20movie_info%5E5%20review_content%5E3&rows=50&rq=%7B!ltr%20model%3Dmy_efi_model%20efi.text%3D%22slavery%20slave%22%20reRankDocs%3D50%7D",
    "http://localhost:8983/solr/movies/select?defType=dismax&fl=*%2Cid%2Cscore%2C%5Bfeatures%5D&fq=mean_vote_imdb%3A%20%5B8.0%20TO%2010.0%5D&indent=true&q.op=OR&q=%22World%20war%20II%22%20emotional&qf=movie_info%5E2%20review_content%5E4&rows=36&rq=%7B!ltr%20model%3Dmy_efi_model%20efi.text%3D%22%27world%20war%202%27%20emotive%22%20reRankDocs%3D50%7D",
    "http://localhost:8983/solr/movies/select?defType=dismax&fl=*%2Cid%2Cscore%2C%5Bfeatures%5D&indent=true&pf=review_content%5E5&ps=3&q.op=AND&q=true%20crime%20story&qf=review_content%5E2%20movie_info%5E3&rows=54&rq=%7B!ltr%20model%3Dmy_efi_model%20efi.text%3D%22true%20crime%20story%22%20reRankDocs%3D50%7D",
    "http://localhost:8983/solr/movies/select?defType=dismax&fl=*%2Cid%2Cscore%2C%5Bfeatures%5D&fq=genres%3A%22Kids%20%26%20Family%22&indent=true&pf=review_content%5E5&ps=5&q.op=OR&q=Christmas&qf=original_title%5E4%20movie_info%5E3%20review_content%5E2%20ner_dest_date%5E8&rq=%7B!ltr%20model%3Dmy_efi_model%20efi.text%3D%22Christmas%22%20reRankDocs%3D50%7D"
    ]

total_features = []
def extract_features(url, qid):
    response = requests.request("GET", url)
    json = simplejson.loads(response.text)
    
    file = qrels_prefix + str(qid) + qrels_sufix
    relevant_docs = [x.split(" ")[0] for x in open(file).readlines()]
    
    documents = json["response"]["docs"]
    for idx, doc in enumerate(documents):
        features = doc["[features]"].split(",")
        features_numerical = list(map(lambda x: float(x.split("=")[1]), features))
        if doc["imdb_title_id"] in relevant_docs:
            features_numerical.append(1)
        else: features_numerical.append(-1)
        features_numerical.append(qid)
        total_features.append(features_numerical)

        
for idx, url in enumerate(queries_urls):
    extract_features(url, idx+1)

df = pd.DataFrame(total_features, columns=["maximize_votes", "maximize_rating", "review_bm25", "description_bm25", "original_score", "status", "qid"])

df_X = df.drop(columns = ["status", "qid"])
df_y = df[["status", "qid"]]

X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size = 0.20)


"""
    POINTWISE APPROACH
"""
# param_grid = {'C': [0.1, 1, 10, 100, 1000],
#               'gamma': [1, 0.1, 0.01, 0.001, 0.0001],
#               'kernel': ["linear"]}

# grid = GridSearchCV(SVC(), param_grid, scoring="recall")

# grid.fit(X_train, y_train)

# prediction = grid.predict(X_test)

# print(classification_report(y_test, prediction))
# plot_confusion_matrix(grid.best_estimator_, X_test, y_test)  

"""
    PAIRWISE APPROACH
"""

rank_svm = RankSVM().fit(X_train.to_numpy(), y_train.to_numpy())
print('Performance of SVM ranking ', rank_svm.score(X_test.to_numpy(),y_test.to_numpy()))


# # and that of linear regression
# ridge = linear_model.RidgeCV(fit_intercept=True)
# ridge.fit(X_train.to_numpy(), y_train.to_numpy())
# X_test_trans, y_test_trans = pairwiseSVM.transform_pairwise(X_test.to_numpy(), y_test.to_numpy())
# score = np.mean(np.sign(np.dot(X_test_trans, ridge.coef_)) == y_test_trans)
# print('Performance of linear regression ', score)
