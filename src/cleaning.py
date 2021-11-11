import os
import pandas as pd


movies = pd.read_csv("dataset/Refined/final_movies.csv")
reviews = pd.read_csv("dataset/Refined/rt_reviews.csv")
# ratings = pd.read_csv("dataset/Refined/imdb_ratings.csv")
    
movies.drop(columns=["writer", "authors", "year"], inplace=True)


movies["country"] = movies["country"].fillna(" ")
movies["genres"] = movies["genres"].fillna("Not defined")
movies["movie_info"] = movies["movie_info"].fillna(" ")

movies["directors"] = movies["directors"].fillna("Unknown")


test = movies.loc[movies["country"].isnull()]
reviews.dropna(subset=["review_content"], inplace=True, how="all")


os.remove("dataset/Refined/final_movies.csv")
movies.to_csv("dataset/Refined/final_movies.csv")

os.remove("dataset/Refined/rt_reviews.csv")
reviews.to_csv("dataset/Refined/rt_reviews.csv")