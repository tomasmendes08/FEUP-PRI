"""
    COMPUTE STATISTICS
    
    mostly plots information on dataset
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import textwrap
from wordcloud import WordCloud

movies = pd.read_csv("dataset/Refined/final_movies.csv")
reviews = pd.read_csv("dataset/Refined/rt_reviews.csv")
ratings = pd.read_csv("dataset/Refined/imdb_ratings.csv")

# q25, q75 = np.percentile(movies["content_rating"], [0.25, 0.75])
# bin_width = 2 * (q75 - q25) * len(movies) ** (-1/3)
# bins = round((x.max() - x.min()) / bin_width)
# plt.hist(movies["content_rating"], align="left", rwidth=0.8)

# plt.legend(prop= {"size": 10})
# plt.show()

# sb.set_theme(style="darkgrid")
# sb.set(rc={'figure.figsize':(14,8)})
# fig = sb.histplot(movies["content_rating"], shrink = 0.5)
# plt.title("Distribution of Movie Ratings")
# plt.xlabel("Content Rating")
# plt.savefig("statistics/content_rating_hist.png")
# plt.show()


""" 
    PIE GRAPH ON CONTENT RATINGS
"""

# labels = movies["content_rating"].value_counts().to_dict().keys()
# sizes = list(map(lambda x: x/sum(movies["content_rating"].value_counts().to_dict().values()), movies["content_rating"].value_counts().to_dict().values()))
# fig1, ax1 = plt.subplots()

# ax1.pie(sizes, labels=labels, autopct="%.2f%%", radius = 1, textprops={"fontsize": 14, "fontweight": "medium"},
#         pctdistance=1.2, labeldistance=0.6 )
#   # Equal aspect ratio ensures that pie is drawn as a circle.

# ax1.set_title("Distribution of Movie Ratings", fontdict={'fontsize': 20, 'fontweight': 'bold'})
# plt.savefig("statistics/content_rating_graph.png")
# plt.show()


"""
    YEAR HISTOGRAPH
"""

# fig1, ax1 = plt.subplots()
# plt.title("Year distribution of movies")
# ax1 = sb.histplot(movies["year"])
# ax1.set_title("Distribution of Movie's release years", fontdict={'fontsize': 20, 'fontweight': 'bold'})
# plt.savefig("statistics/year_graph.png")
# plt.show()


"""
    COUNTRY HISTOGRAPH
"""

# single_list = []

# for country in movies["country"]:
#     countries = country.split(",")
#     single_list += countries

# occurrences = {x: single_list.count(x) for x in list(set(single_list))}



# countries = sorted(list(occurrences.keys()), key=lambda x: occurrences[x], reverse = True)[:20]
# nums = [occurrences[x] for x in countries]    

# fig1, ax1 = plt.subplots()

# sb.set_theme(style="darkgrid")
# sb.set(rc={'figure.figsize':(20,8)})
# fig = plt.bar(countries, nums)

# cnt = -1.2
# for country in countries:
#     cnt += 1
#     ax1.text(x=cnt, y=min(occurrences[country] * 1.1, 7200), s=str(occurrences[country]), fontdict={'fontsize': 11, 'fontweight': 'bold'})
    
    
# plt.title("Distribution of Movie Ratings")
# plt.xlabel("Country")
# plt.savefig("statistics/content_rating_year.png")
# plt.show()


"""
    IMDB RATINGS DISTRIBUTION
"""

# fig1, ax1 = plt.subplots()
# plt.title("IMDB Ratings distribution")
# plt.xlabel("Average vote", fontdict={'fontsize': 15, 'fontweight': 'bold'})
# ax1 = sb.histplot(movies["avg_vote"], kde=True, legend=False)
# ax1.set_title("Distribution of Movie's IMDB ratings", fontdict={'fontsize': 20, 'fontweight': 'bold'})
# plt.savefig("statistics/ratings.png")
# plt.show()


"""
    REVIEWS PER MOVIE
"""

# reviews_count = reviews["rotten_tomatoes_link"].value_counts().to_dict()

# reviews_count = movies["votes"].value_counts()


# fig1, ax1 = plt.subplots()
# plt.title("IMDB Ratings per Movie")
# plt.xlabel("Reviews", fontdict={'fontsize': 15, 'fontweight': 'bold'})
# ax1 = sb.histplot(movies["votes"])
# ax1.set_title("Distribution of Movie's Ratings", fontdict={'fontsize': 20, 'fontweight': 'bold'})
# # plt.savefig("statistics/ratings.png")
# plt.show()




"""
    AVERAGE RATINGS PER YEAR
"""

# anual_scores = {}

# for year in movies["year"].unique():
#     df = movies.loc[movies["year"] == year]
#     average_score_per_year = df["avg_vote"].mean()
#     anual_scores[int(year)] = average_score_per_year
    
# fig1, ax1 = plt.subplots()
# ax1.set_title("Average scores per year", fontdict={'fontsize': 20, 'fontweight': 'bold'})
# plt.xlabel("Year", fontdict={'fontsize': 15, 'fontweight': 'bold'})
# plt.ylabel("Average ratings", fontdict={'fontsize': 15, 'fontweight': 'bold'})
# fig = plt.bar(anual_scores.keys(), anual_scores.values())
# plt.savefig("statistics/anual_ratings.png")
# plt.show()


"""
    MOVIE GENRES DISTRIBUTION
"""

# all_genres = []

# for genre in movies["genres"]:
#     list_genres = genre.split(",")
#     list_genres = list(map(lambda x: textwrap.shorten(x.strip(), width=20), list_genres))
#     all_genres += list_genres
    
# fig1, ax1 = plt.subplots()

# # sb.set_theme(style="whitegrid")
# # sb.set(rc={'figure.figsize':(80,65)})
# plt.xlabel("Genres", fontdict={'fontsize': 80, 'fontweight': 'bold'})
# plt.ylabel("Count", fontdict={'fontsize': 80, 'fontweight': 'bold'})


# genre_count = {x: all_genres.count(x) for x in list(set(all_genres))}


# plt.barh(list(genre_count.keys()), list(genre_count.values()))
# # ax1 = plt.hist(all_genres, orientation="horizontal")


# plt.title("Genre Distribution", fontdict={'fontsize': 80, 'fontweight': 'bold'})
# plt.xticks(fontsize=50)
# plt.yticks(fontsize=50)


# # ax1.set_title("Genre distribution", fontdict={'fontsize': 50, 'fontweight': 'bold'})

# plt.savefig("statistics/genre_dist2.png")
# plt.show()


"""
    GENERATE WORDCLOUD
"""

# text = " ".join(movies["movie_info"])
# wordcloud = WordCloud(max_font_size=50, max_words=100, background_color="white").generate(text)
# plt.imshow(wordcloud, interpolation="bilinear")
# plt.title("Description Wordcloud", fontdict={'fontsize': 100, 'fontweight': 'bold'})
# plt.axis("off")
# plt.savefig("statistics/description_wordcloud.png")
# plt.show()

