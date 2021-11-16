import os
import pandas as pd
import numpy as np
from load_data import df_reviews as reviews, final_movies as movies


#movies
movies.drop(columns=["title", "authors", "year", "avg_vote", "votes", "metascore", "usa_gross_income", "reviews_from_users", "reviews_from_critics", "audience_count", "critics_consensus", "date_published", "tomatometer_status", "audience_status", "tomatometer_count", "tomatometer_top_critics_count", "tomatometer_fresh_critics_count", "tomatometer_rotten_critics_count", "votes_10", "votes_9", "votes_8", "votes_7", "votes_6", "votes_5", "votes_4", "votes_3", "votes_2", "votes_1", "allgenders_0age_votes", "allgenders_0age_avg_vote", "allgenders_18age_avg_vote", "allgenders_18age_votes", "allgenders_30age_avg_vote", "allgenders_30age_votes", "allgenders_45age_avg_vote", "allgenders_45age_votes", "males_0age_avg_vote", "males_0age_votes", "males_18age_avg_vote", "males_18age_votes", "males_30age_avg_vote", "males_30age_votes", "males_45age_avg_vote", "males_45age_votes", "females_0age_avg_vote", "females_0age_votes", "females_18age_avg_vote", "females_18age_votes", "females_30age_avg_vote", "females_30age_votes", "females_45age_avg_vote", "females_45age_votes", "top1000_voters_rating", "top1000_voters_votes"], inplace=True)

#fill null values
movies["country"] = movies["country"].fillna("None")
movies["genres"] = movies["genres"].fillna("Not defined")
movies["movie_info"] = movies["movie_info"].fillna(" ")

movies["directors"] = movies["directors"].fillna("Unknown")
movies["budget"] = movies["budget"].fillna("Unknown")
movies["worlwide_gross_income"] = movies["worlwide_gross_income"].fillna("Unknown")
movies["streaming_release_date"] = movies["streaming_release_date"].fillna("Unknown")
movies["production_company"] = movies["production_company"].fillna("Unknown")
movies["writer"] = movies["writer"].fillna("Unknown")
movies["actors"] = movies["actors"].fillna("Unknown")
movies["runtime"] = movies["runtime"].fillna("Not defined")

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

#update males_allages_votes
movies["males_allages_votes"] = movies["males_allages_votes"].apply(np.int64)

movies["country"] = movies["country"].map(lambda x: x.strip())

#adjusting movies columns order
movies = movies[["imdb_title_id", "rotten_tomatoes_link", "original_title", "original_release_date", "streaming_release_date", "country", "language", "production_company", "directors", "writer", "actors", "budget", "worlwide_gross_income", "genres", "content_rating", "runtime", "movie_info", "total_votes", "weighted_average_vote", "mean_vote", "median_vote", "males_allages_votes", "males_allages_avg_vote", "females_allages_votes", "females_allages_avg_vote", "us_voters_votes", "us_voters_rating", "non_us_voters_votes", "non_us_voters_rating", "audience_rating", "tomatometer_rating"]]

#comparar colunas
#movies['is_score_chased'] = np.where(movies['date_published']==movies['original_release_date'], 
#                                            'yes', 'no')


#reviews
reviews.dropna(subset=["review_content"], inplace=True, how="all")
reviews.drop(columns=["review_type"], inplace=True)

#keep only 20 reviews (max) for each movie
reviews = reviews.groupby("rotten_tomatoes_link").tail(20)

os.remove("../dataset/Refined/final_movies.csv")
movies.to_csv("../dataset/Refined/final_movies.csv")

os.remove("../dataset/Refined/rt_reviews.csv")
reviews.to_csv("../dataset/Refined/rt_reviews.csv")

