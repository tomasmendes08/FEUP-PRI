import requests
import json

# dataset parsing

f = open('../dataset/data.json', "r")
data = json.loads(f.read())
f.close()
newdata = []

url = "http://www.omdbapi.com/"

for movie in data[8990:]:
    imdb_id = movie['imdb_title_id']
    payload = {'i':imdb_id, 'apikey':"f5f315e8"}
    response = requests.get(url, params=payload)
    count = 0
    while(response.status_code != 200 or count == 5):
        print(response.status_code)
        response = requests.get(url, params=payload)
        count+=1
    if(response.status_code == 200):
        moviejson = response.json()
        movieposter = moviejson['Poster']
        movie['Poster'] = movieposter
        print(movie['Poster'])
    newdata.append(movie)

#params = dict(i='')


file = open("../dataset/data.json", 'w')
json.dump(fulldata, file)
