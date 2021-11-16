import bs4 as bs
import pandas as pd
import concurrent
import urllib.request
import sys
import requests

movies = pd.read_csv("../dataset/Refined/final_movies.csv")

data = {}
cnt = 0
# executor = concurrent.futures.ThreadPoolExecutor(max_workers = 50)

def get_status(url):

    status = urllib.request.urlopen(url).getcode()
    print(url)
    if status != 200:
        return None
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')
    
    icons = [x["name"] for x in soup.find_all("affiliate-icon")]
    data[url] = ", ".join(icons)
    # executor.shutdown()
    return status



for movie_link in movies["rotten_tomatoes_link"]:
    threads = []
    url = "https://www.rottentomatoes.com/" + movie_link
    get_status(url)
    print(f"{url} {cnt}")
    cnt += 1