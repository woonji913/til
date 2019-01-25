import requests
from bs4 import BeautifulSoup
import csv, datetime, os

date = datetime.date(2019, 1, 13)
weeks = datetime.timedelta(7)

movies = []
check = set()
key = os.environ['KEY']

for i in range(10):
    current = date - weeks * i
    url = f'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={key}&weekGb=0&targetDt='
    url += str(current.strftime('%Y%m%d'))
    res_json = requests.get(url).json()
    for j in res_json['boxOfficeResult']['weeklyBoxOfficeList']:
        code = j['movieCd']
        name = j['movieNm']
        total_aud = j['audiAcc']
        if code not in check:
            print(name)
            movies.append({'movie_code': code, 'title': name, 'audience': total_aud, 'recorded_at': current})
            check.add(code)
# movieIDDF = pd.DataFrame()
# movieIDDF = movieIDDF.append({"movieCd":" ", "movieNM": " ", "audiCnt": " ", "openDt": " "}, ignore_index = True)
# # pprint(movieIDDF)
with open('boxoffice.csv', 'w', encoding='utf-8', newline='') as f:
    fieldnames = ('movie_code', 'title', 'audience', 'recorded_at')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    for movie in movies:
        writer.writerow(movie)