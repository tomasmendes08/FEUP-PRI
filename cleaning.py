"""
    CLEANING DATA
    
    joins 'writer' with 'authors'
"""
import pandas as pd


movies = pd.read_csv("dataset/Refined/final_movies.csv")
# reviews = pd.read_csv("dataset/Refined/rt_reviews.csv")
# ratings = pd.read_csv("dataset/Refined/imdb_ratings.csv")

movies["writer"] = movies["writer"].fillna("")
movies["authors"] = movies["authors"].fillna("")

for idx in range(len(movies)):
    # print("CURRENT INDEX: ", idx)
    movie = movies.iloc[[idx]]
    writers = (movie["writer"].values[0]).split(",")
    authors = (movie["authors"].values[0]).split(",")
    all_authors = [x.strip() for x in writers + authors]
    all_authors = list(set(all_authors))
    new_authors = ", ".join(all_authors)
    movies.iloc[idx, movies.columns.get_loc("authors")] = new_authors
    
movies.drop(columns=["writer"])

