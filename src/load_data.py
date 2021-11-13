import pandas as pd

df_reviews = pd.read_csv("../dataset/RT/rotten_tomatoes_critic_reviews.csv")
df_movies = pd.read_csv("../dataset/RT/rotten_tomatoes_movies.csv")


def handle_year(x):
    try:
        return int(x)
    except ValueError:
        return 2019 # erro numa das linhas 

# Drops nan values
df_movies.dropna(subset=["tomatometer_status", "original_release_date"], inplace=True) # filmes com poucas reviews 

df_reviews.dropna(subset=["review_score", "critic_name"], inplace=True) # reviews apagadas do site

# Read imdb dataset

imdb_movies = pd.read_csv("../dataset/IMDB/IMDb_movies.csv")
imdb_ratings = pd.read_csv("../dataset/IMDB/IMDb_ratings.csv")


release_dates = df_movies["original_release_date"]
release_year = []

for date in release_dates:
    year = int(date.split("-")[0])
    release_year.append(year)

df_movies = df_movies.assign(release_year = release_year)
df_movies.drop(columns=["actors", "production_company"], inplace=True)
imdb_movies["year"] = imdb_movies["year"].map(lambda x: handle_year(x))

final_movies = pd.merge(imdb_movies, df_movies, left_on =["original_title", "year"], right_on = ["movie_title" ,"release_year"])

# dispose redundant data
final_movies.drop(columns=["movie_title", "release_year", "genre", "description", "duration", "director"], inplace=True)

all_rt_movies = final_movies["rotten_tomatoes_link"].to_numpy()
all_imdb_movies = final_movies["imdb_title_id"].to_numpy()

df_reviews = df_reviews[df_reviews["rotten_tomatoes_link"].isin(all_rt_movies)]
imdb_ratings = imdb_ratings[imdb_ratings["imdb_title_id"].isin(all_imdb_movies)]

final_movies = pd.merge(final_movies, imdb_ratings, how="inner", on="imdb_title_id")

# Writes clean data to csv

imdb_ratings.to_csv("../dataset/Refined/imdb_ratings.csv")
df_reviews.to_csv("../dataset/Refined/rt_reviews.csv")
final_movies.to_csv("../dataset/Refined/final_movies.csv")

