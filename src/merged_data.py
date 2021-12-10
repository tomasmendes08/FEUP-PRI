# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 00:30:51 2021

@author: tomas
"""

import pandas as pd
import json

reviews_df = pd.read_csv("../dataset/Refined/rt_reviews.csv")
final_movies_df = pd.read_csv("../dataset/Refined/final_movies.csv")

reviews = reviews_df.to_dict(orient='records')
final_movies = final_movies_df.to_dict(orient='records')

for x in final_movies:    
    x['reviews'] = []
    for y in reviews:
        if y['rotten_tomatoes_link'] == x['rotten_tomatoes_link']:
            x['reviews'].append(y)
            

with open("../dataset/Refined/data.json", 'w+') as file:
    file.write(json.dumps(final_movies, indent=4))
    file.close()
    