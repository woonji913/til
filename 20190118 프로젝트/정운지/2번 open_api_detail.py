import requests
from bs4 import BeautifulSoup
import csv, datetime, os

key = os.environ['KEY']
with open('boxoffice.csv', encoding='utf-8', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # for row in reader:
    #     print(row['movie_code'])



    movies_info = []
    for row in reader:
        url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={key}&movieCd='
        url += row['movie_code']
        res_json = requests.get(url).json()
        j = res_json["movieInfoResult"]["movieInfo"]
        save_data = {
            'code': j['movieCd'],
            'name_Kr': j['movieNm'],
            'name_En': j['movieNmEn'],
            'name_Ori': j['movieNmOg'],
            'year': j['prdtYear'],
            'showtime': j['showTm'],
            'genre': j['genres'][0]['genreNm'],
            'director': j['directors'][0]['peopleNm']
        }
        actor1 = actor2 = actor3 = ''
        for k in range(len(j['actors'])):
            if k == 0:
                actor1 = j['actors'][k]['peopleNm']
            if k == 1:
                actor2 = j['actors'][k]['peopleNm']
            if k == 2:
                actor3 = j['actors'][k]['peopleNm']
        
        movies_info.append({'movie_code': save_data['code'], 'title_Kr': save_data['name_Kr'], 
        'title_En': save_data['name_En'], 'title_Ori': save_data['name_Ori'], 
        'prdtYear': save_data['year'], 'Running_Time': save_data['showtime'], 'Genres': save_data['genre'],
        'Directors': save_data['director'], 'Actor1': actor1, 'Actor2': actor2, 'Actor3': actor3})


with open('movies.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', 'title_Kr', 'title_En', 'title_Ori','prdtYear', 'Running_Time', 'Genres', 'Directors', 'Actor1', 'Actor2', 'Actor3')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for movie_info in movies_info:
        writer.writerow(movie_info)
        

