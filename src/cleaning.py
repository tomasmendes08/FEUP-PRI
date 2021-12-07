import os

from load_data import df_reviews as reviews, final_movies as movies


#movies
# movies.drop(columns=["title", "authors", "year", "avg_vote", "votes", "metascore", "usa_gross_income", "reviews_from_users", "reviews_from_critics", "audience_count", "critics_consensus", "date_published", "tomatometer_status", "audience_status", "tomatometer_count", "weighted_average_vote", "median_vote", "tomatometer_top_critics_count", "tomatometer_fresh_critics_count", "tomatometer_rotten_critics_count", "top1000_voters_rating", "top1000_voters_votes","males_0age_avg_vote", "males_0age_votes", "males_18age_avg_vote", "males_18age_votes", "males_30age_avg_vote", "males_30age_votes", "males_45age_avg_vote", "males_45age_votes", "females_0age_avg_vote", "females_0age_votes", "females_18age_avg_vote", "females_18age_votes", "females_30age_avg_vote", "females_30age_votes", "females_45age_avg_vote", "females_45age_votes", "males_allages_avg_vote", "males_allages_votes", "females_allages_avg_vote", "females_allages_votes"], inplace=True)

# drop_cols = "allgenders_0age_votes", "allgenders_0age_avg_vote", "allgenders_18age_avg_vote", "allgenders_18age_votes", "allgenders_30age_avg_vote", "allgenders_30age_votes", "allgenders_45age_avg_vote", "allgenders_45age_votes", "males_0age_avg_vote", "males_0age_votes", "males_18age_avg_vote", "males_18age_votes", "males_30age_avg_vote", "males_30age_votes", "males_45age_avg_vote", "males_45age_votes", "females_0age_avg_vote", "females_0age_votes", "females_18age_avg_vote", "females_18age_votes", "females_30age_avg_vote", "females_30age_votes", "females_45age_avg_vote", "females_45age_votes"
#fill null values
# movies["country"] = movies["country"].fillna("None")
# movies["genres"] = movies["genres"].fillna("Not defined")
# movies["movie_info"] = movies["movie_info"].fillna("Not defined")
# movies["audience_rating"] = movies["audience_rating"].fillna("Insuficient votes")
# movies["allgenders_0age_avg_vote"] = movies["allgenders_0age_avg_vote"].fillna("No votes")
# movies["allgenders_0age_votes"] = movies["allgenders_0age_votes"].fillna("No votes")
# movies["allgenders_18age_avg_vote"] = movies["allgenders_18age_avg_vote"].fillna("No votes")
# movies["allgenders_18age_votes"] = movies["allgenders_18age_votes"].fillna("No votes")

# movies["directors"] = movies["directors"].fillna("Unknown")
# movies["budget"] = movies["budget"].fillna("Unknown")
# movies["worlwide_gross_income"] = movies["worlwide_gross_income"].fillna("Unknown")
# movies["streaming_release_date"] = movies["streaming_release_date"].fillna("Unknown")
# movies["production_company"] = movies["production_company"].fillna("Unknown")
# movies["writer"] = movies["writer"].fillna("Unknown")
# movies["actors"] = movies["actors"].fillna("Unknown")
movies["runtime"] = movies["runtime"].fillna(0)
movies['runtime'] = movies['runtime'].astype('int64')
movies["audience_rating"] = movies["audience_rating"].fillna(0)
movies['audience_rating'] = movies["audience_rating"].astype('int64')
movies["tomatometer_rating"] = movies["tomatometer_rating"].fillna(0)
movies['tomatometer_rating'] = movies["tomatometer_rating"].astype('int64')

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
movies = movies[["imdb_title_id", "rotten_tomatoes_link", "original_title", "original_release_date", "streaming_release_date", "country", "language", "production_company", "directors", "writer", "actors", "budget", "worlwide_gross_income", "genres", "content_rating", "runtime", "movie_info", "audience_rating", "tomatometer_rating", "total_votes", "mean_vote", "votes_10", "votes_9", "votes_8", "votes_7", "votes_6", "votes_5", "votes_4", "votes_3", "votes_2", "votes_1"]]

#comparar colunas
#movies['is_score_chased'] = np.where(movies['date_published']==movies['original_release_date'], 
#                                            'yes', 'no')

#check which columns have null values
# nan_values = movies.isna()
# nan_columns = nan_values.any()
# columns_with_nan = movies.columns[nan_columns].tolist()

#reviews
reviews.dropna(subset=["review_content"], inplace=True, how="all")
# reviews.drop(columns=["review_type"], inplace=True)

# keep only 20 reviews (max) for each movie
# def choose_critics(x):
reviews_len = [len(x) for x in reviews["review_content"]]
reviews["tmp_len"] = reviews_len

# reviews = reviews.groupby("rotten_tomatoes_link").tail(20)
reviews = reviews.sort_values(by=["rotten_tomatoes_link", "top_critic", "tmp_len"], ascending=False).groupby("rotten_tomatoes_link").tail(20)
reviews.drop(columns=["tmp_len"], inplace=True)
# reviews = reviews.iloc[::-1]

os.remove("../dataset/Refined/final_movies.csv")
movies.to_csv("../dataset/Refined/final_movies.csv")

os.remove("../dataset/Refined/rt_reviews.csv")
reviews.to_csv("../dataset/Refined/rt_reviews.csv")

