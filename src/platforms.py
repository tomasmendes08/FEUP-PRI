from cleaning import movies as movies
import pandas as pd
import os


def handle_platforms(file, col_name):

    plat_movies = pd.read_csv(file)
    
    plat_movies = plat_movies.loc[plat_movies["type"] == "Movie"]
    
    plat_movies = plat_movies[["show_id", "title"]]
    plat_movies = pd.merge(movies, plat_movies, left_on =["original_title"], right_on = ["title"], how="left")
    
    # platform_movies.drop(columns=["title"], inplace=True)
    
    available_list = []
    for id in plat_movies["show_id"].values:
        available_list.append( id == id)

    movies[col_name] = available_list
    # return platform_movies

handle_platforms("../dataset/platforms/netflix_titles.csv", "available_netflix")
handle_platforms("../dataset/platforms/amazon_prime_titles.csv", "available_prime_video")
handle_platforms("../dataset/platforms/disney_plus_titles.csv", "available_disney+")


os.remove("../dataset/Refined/final_movies.csv")
movies.to_csv("../dataset/Refined/final_movies.csv")

movies.to_json("../dataset/Refined/movies.json", orient = "records")