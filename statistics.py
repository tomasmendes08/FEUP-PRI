"""
    COMPUTE STATISTICS
    
    mostly plots information on dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

movies = pd.read_csv("dataset/Refined/final_movies.csv")
reviews = pd.read_csv("dataset/Refined/rt_reviews.csv")
ratings = pd.read_csv("dataset/Refined/imdb_ratings.csv")

# q25, q75 = np.percentile(movies["content_rating"], [0.25, 0.75])
# bin_width = 2 * (q75 - q25) * len(movies) ** (-1/3)
# bins = round((x.max() - x.min()) / bin_width)
# plt.hist(movies["content_rating"], align="left", rwidth=0.8)

# plt.legend(prop= {"size": 10})
# plt.show()

sb.set_theme(style="darkgrid")
sb.histplot(movies["content_rating"])
