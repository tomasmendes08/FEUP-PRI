import pandas as pd
import json


def fix_encoding(text):
    if isinstance(text, str):
        return text.encode('latin-1', 'ignore').decode('utf-8', 'ignore')

movies_df = pd.read_csv('../../dataset/Refined/final_movies.csv')
reviews_df = pd.read_csv('../../dataset/Refined/rt_reviews.csv')

reviews_df["review_content"] = reviews_df["review_content"].map(lambda x: fix_encoding(x))

reviews_df = reviews_df[["rotten_tomatoes_link", "review_content"]]

movies = movies_df.to_dict(orient='records')

for movie in movies:
    link = movie["rotten_tomatoes_link"]
    movie['review_content'] = reviews_df[reviews_df['rotten_tomatoes_link'] == link]['review_content'].tolist()

# Save merged data
with open("data.json", "w+") as f:
    f.write(json.dumps(movies, indent=4))
    f.close()