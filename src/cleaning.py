import os

from load_data import df_reviews as reviews, final_movies as movies
import numpy as np

#movies
# movies.drop(columns=["title", "authors", "year", "avg_vote", "votes", "metascore", "usa_gross_income", "reviews_from_users", "reviews_from_critics", "audience_count", "critics_consensus", "date_published", "tomatometer_status", "audience_status", "tomatometer_count", "weighted_average_vote", "median_vote", "tomatometer_top_critics_count", "tomatometer_fresh_critics_count", "tomatometer_rotten_critics_count", "top1000_voters_rating", "top1000_voters_votes","males_0age_avg_vote", "males_0age_votes", "males_18age_avg_vote", "males_18age_votes", "males_30age_avg_vote", "males_30age_votes", "males_45age_avg_vote", "males_45age_votes", "females_0age_avg_vote", "females_0age_votes", "females_18age_avg_vote", "females_18age_votes", "females_30age_avg_vote", "females_30age_votes", "females_45age_avg_vote", "females_45age_votes", "males_allages_avg_vote", "males_allages_votes", "females_allages_avg_vote", "females_allages_votes"], inplace=True)

# drop_cols = "allgenders_0age_votes", "allgenders_0age_avg_vote", "allgenders_18age_avg_vote", "allgenders_18age_votes", "allgenders_30age_avg_vote", "allgenders_30age_votes", "allgenders_45age_avg_vote", "allgenders_45age_votes", "males_0age_avg_vote", "males_0age_votes", "males_18age_avg_vote", "males_18age_votes", "males_30age_avg_vote", "males_30age_votes", "males_45age_avg_vote", "males_45age_votes", "females_0age_avg_vote", "females_0age_votes", "females_18age_avg_vote", "females_18age_votes", "females_30age_avg_vote", "females_30age_votes", "females_45age_avg_vote", "females_45age_votes"
#fill null values
# movies["country"] = movies["country"].fillna("None")
movies["genres"] = movies["genres"].fillna("Not defined")
movies["movie_info"] = movies["movie_info"].fillna("Not defined")
# movies["audience_rating"] = movies["audience_rating"].fillna("Insuficient votes")
# movies["allgenders_0age_avg_vote"] = movies["allgenders_0age_avg_vote"].fillna("No votes")
# movies["allgenders_0age_votes"] = movies["allgenders_0age_votes"].fillna("No votes")
# movies["allgenders_18age_avg_vote"] = movies["allgenders_18age_avg_vote"].fillna("No votes")
# movies["allgenders_18age_votes"] = movies["allgenders_18age_votes"].fillna("No votes")

movies["directors"] = movies["directors"].fillna("Unknown") #falta corrigir
movies["budget"] = movies["budget"].fillna("Unknown")
movies["worlwide_gross_income"] = movies["worlwide_gross_income"].fillna("Unknown")
# movies["streaming_release_date"] = movies["streaming_release_date"].fillna("Unknown")
movies["production_company"] = movies["production_company"].fillna("Unknown")
movies["actors"] = movies["actors"].fillna("No actors")
movies = movies.rename(columns={'mean_vote': 'mean_vote_imdb'})

movies["runtime"] = movies["runtime"].fillna(0)
movies['runtime'] = movies['runtime'].astype('int64')
movies["audience_rating"] = movies["audience_rating"].fillna(0)
movies['audience_rating'] = movies["audience_rating"].astype('int64')
movies["tomatometer_rating"] = movies["tomatometer_rating"].fillna(0)
movies['tomatometer_rating'] = movies["tomatometer_rating"].astype('int64')

movies["original_release_date"] = movies["original_release_date"].fillna("0000-01-01")
movies['original_release_date'] = movies['original_release_date'].map(lambda x: str(x) + "T00:00:00Z")
movies["streaming_release_date"] = movies["streaming_release_date"].fillna("0000-01-01")
movies['streaming_release_date'] = movies['streaming_release_date'].map(lambda x: str(x) + "T00:00:00Z")

#updated movie writer
movies.at[138,"writer"] = "H.G. Wells"
movies.at[339,"writer"] = "Noël Coward, Anthony Havelock-Allan, David Lean"
movies.at[3538,"writer"] = "Steven Soderbergh"
movies.at[4220,"writer"] = "Unknown"
movies.at[6399,"writer"] = "Unknown"
movies.at[7256,"writer"] = "Unknown"
movies.at[8344,"writer"] = "Unknown"
movies.at[8781,"writer"] = "Unknown"

#updated movie country
movies.at[6389, 'country'] = 'USA'
movies.at[7236, 'country'] = 'UK'

#updating movie language
movies.at[3, 'language'] = 'English'
movies.at[4, 'language'] = 'None'
movies.at[5, 'language'] = 'English'
movies.at[8, 'language'] = 'None'
movies.at[10, 'language'] = 'English'
movies.at[14, 'language'] = 'English'
movies.at[15, 'language'] = 'English'
movies.at[16, 'language'] = 'None'
movies.at[18, 'language'] = 'English'
movies.at[19, 'language'] = 'None'
movies.at[20, 'language'] = 'English'
movies.at[23, 'language'] = 'English'
movies.at[24, 'language'] = 'None'
movies.at[25, 'language'] = 'None'
movies.at[28, 'language'] = 'None'
movies.at[2696, 'language'] = 'Dutch'
movies.at[2878, 'language'] = 'English'
movies.at[4777, 'language'] = 'English'
movies.at[5750, 'language'] = 'English'
movies.at[6050, 'language'] = 'None'
movies.at[6389, 'language'] = 'English'
movies.at[6481, 'language'] = 'English'
movies.at[6532, 'language'] = 'English'
movies.at[7236, 'language'] = 'English'
movies.at[7289, 'language'] = 'English'
movies.at[7362, 'language'] = 'English'
movies.at[7997, 'language'] = 'English'
movies.at[8081, 'language'] = 'English'
movies.at[8235, 'language'] = 'English'
movies.at[8324, 'language'] = 'English'
movies.at[8387, 'language'] = 'English'
movies.at[8405, 'language'] = 'English'
movies.at[8488, 'language'] = 'English'
movies.at[8921, 'language'] = 'English'
movies.at[9005, 'language'] = 'English'

#adjusting movies columns order
movies = movies[["imdb_title_id", "rotten_tomatoes_link", "original_title", "original_release_date", "streaming_release_date", "country", "language", "production_company", "directors", "writer", "actors", "budget", "worlwide_gross_income", "genres", "content_rating", "runtime", "movie_info", "audience_rating", "tomatometer_rating", "total_votes", "mean_vote_imdb", "votes_10", "votes_9", "votes_8", "votes_7", "votes_6", "votes_5", "votes_4", "votes_3", "votes_2", "votes_1", "release_year"]]

#comparar colunas
#movies['is_score_chased'] = np.where(movies['date_published']==movies['original_release_date'], 
#                                            'yes', 'no')

#check which columns have null values
# nan_values = movies.isna()
# nan_columns = nan_values.any()
# columns_with_nan = movies.columns[nan_columns].tolist()

#reviews
reviews.dropna(subset=["review_content"], inplace=True, how="all")
reviews["review_date"] = reviews["review_date"].fillna("0000-01-01")
reviews['review_date'] = reviews['review_date'].map(lambda x: str(x) + "T00:00:00Z")


# keep only 20 reviews (max) for each movie
# def choose_critics(x):
reviews_len = [len(x) for x in reviews["review_content"]]
reviews["tmp_len"] = reviews_len

# reviews = reviews.groupby("rotten_tomatoes_link").tail(20)
reviews = reviews.sort_values(by=["rotten_tomatoes_link", "top_critic", "tmp_len"], ascending=False).groupby("rotten_tomatoes_link").tail(20)
reviews.drop(columns=["tmp_len", "review_type"], inplace=True)


lista = []
letters_dict = {'A+':9.5, 'A':9.0, 'A-':8.5, 'B+':8.0, 'B':7.5, 'B-':7.0, 'C+':6.5, 'C':6.0, 'C-':5.5, 'C  -':5.5, 'D+': 5.0, 'D': 4.5, 'D-':4.0, 'E':3.0, 'F':2.0}
for x in reviews["review_score"]:
    aux = x.split('/')
    if len(aux) == 2:
        if float(aux[1]) == 0.0: aux[1] = 10
        score = 10.0*float(aux[0])/float(aux[1]) 
        lista.append(score)
    elif aux[0].isnumeric():
        if float(aux[0]) > 5:
            lista.append(float(aux[0]))
        else:
            score = 2.0*float(aux[0])
            lista.append(score)
    else:
        lista.append(letters_dict[aux[0]])
    
movies["type"] = "movie"
reviews["type"] = "review"



all_years = []
all_titles = []

for review in reviews["rotten_tomatoes_link"]:
    movie = movies.loc[movies["rotten_tomatoes_link"] == review]
    all_years.append(movie["release_year"].values[0])
    all_titles.append(movie["original_title"].values[0])


reviews["movie_title"] = all_titles
reviews["release_year"] = all_years

reviews["review_score_normalized"] = lista
reviews.drop(columns=["review_score", "rotten_tomatoes_link"], inplace = True)


os.remove("../dataset/Refined/final_movies.csv")
movies.to_csv("../dataset/Refined/final_movies.csv")

os.remove("../dataset/Refined/rt_reviews.csv")
reviews.to_csv("../dataset/Refined/rt_reviews.csv")
