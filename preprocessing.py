import pandas as pd
import numpy as np

df_reviews = pd.read_csv("dataset/rotten_tomatoes_critic_reviews.csv")
df_movies = pd.read_csv("dataset/rotten_tomatoes_movies.csv")


# Drops nan values
df_movies.dropna(subset=["tomatometer_status"], inplace=True) # filmes com poucas reviews 

df_reviews.dropna(subset=["review_score", "critic_name"], inplace=True) # reviews apagadas do site

all_movies = df_movies["rotten_tomatoes_link"].to_numpy()
df_reviews = df_reviews[df_reviews["rotten_tomatoes_link"].isin(all_movies)]

# Writes refined data to new csv
df_movies.to_csv("dataset/refined_movies.csv")
df_reviews.to_csv("dataset/refined_reviews.csv")

# merge dataframes (?) nem deve ser preciso
# merged = pd.merge(df_reviews, df_movies, on= "rotten_tomatoes_link")


