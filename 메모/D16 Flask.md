20190131 목요일

# D16 Flask

## flask 기초2

### 1. fake google

```python
# fake google
@app.route('/google')
def google():
    return render_template('google.html')
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <form action="https://www.google.com/search" target="_blank">
        <input type="text" name="q">
        <input type="submit" value="search">
    </form>
</body>

</html>
```



### 2. ping pong

```python
# ping pong
@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    # request.args 딕셔너리
    name = request.args.get('name')
    msg = request.args.get('msg') 
    return render_template('pong.html', name=name, msg=msg)
```

```html
<!-- ping -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <form action="/pong" target="_blank">
        <input type="text" name="name"> 
        <input type="text" name="msg">
        <input type="submit" value="ping">
        
</body>

</from>
```

```html
<!-- pong -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <h2> {{ name }}이 {{ msg }}를 보냈습니다.</h2>
</body>

</from>
```

### 3. new 핑퐁

```py
# ping new, pong new
@app.route('/ping_new')
def ping_new():
    return render_template('ping_new.html')
    
@app.route('/pong_new', methods=['POST'])
def pong_new():
    # name = request.form['name']
    name = request.form.get('name')
    msg = request.form.get('msg')
    return render_template('pong_new.html', name=name, msg=msg)
```

```html
<!-- ping -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <form action="/pong_new" method="POST">
        <input type="text" name="name"> 
        <input type="text" name="msg"> 
        <input type="submit" value="ping">
        
</body>

</from>
```

```html
<!-- pong -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <h2> {{ name }}이 {{ msg }}를 보냈습니다. </h2>
</body>

</from>
```

### 4. opgg 전적

```python
import requests
from bs4 import BeautifulSoup
url = 'http://www.op.gg/summoner/userName='
username = 'hide on bush'
response = requests.get(url+username).text
soup = BeautifulSoup(response, 'html.parser')

wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
print(wins.text)
print(loses.text)
```

```python
from flask import Flask, render_template, request
import os
import datetime
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'

# opgg
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    loses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    return render_template('opgg_result.html', username=username, wins=wins.text, loses=loses.text)

if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    <style type="text/css">
        .nav {
            max-width: 100%;
            margin: 0 auto;
            background: #1d2e51;
        }

        body {
            background-color: #00b2ff;
        }

        .container {
            justify-content: center;
        }
    </style>
</head>


<body>
    <a href="/">
        <img src="//opgg-static.akamaized.net/images/logo/logo-lol.png" alt="" class="site__logo"><span class="site__name"><img src="//opgg-static.akamaized.net/images/logo/l_logo.png"></span></a>


    <ul class="nav">
        <li class="nav-item">
            <a class="nav-link active" href="http://op.gg/">홈</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/champion/statistics">챔피언 분석</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/statistics/">통계</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/ranking/">랭킹</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="/spectate">프로관전</a>
        </li>
        <li class="nav-item">
            <a class="nav-link" href="http://talk.op.gg/s/lol" target='_blank'>커뮤니티</a>
        </li>

    </ul>

    <div class="container">
        <div class="index-logo">
            <img src="https://attach.s.op.gg/logo/20190128090241.bcb4fa0f06c3a9deea6dc1798ce6ee5a.PNG" title="Awaken" alt="OP.GG Logo (Awaken)" class="Image">
        </div>
    </div>

    <div class="container">
        <form action="/opgg_result" target='_blank'>
            <input type="text" name="username">
            <button type="submit" class="btn btn-primary">GG</button>
            <!--<input type="submit" value="search">-->
    </div>


    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</from>

```

### 5. cvs

```python
import csv

# csv
@app.route('/timeline')
def timeline():
    # username / message
    return render_template('timeline.html')

@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    # DictWriter / timeline.csv / encoding / fieldnames
    with open('timeline.csv', 'a', newline='') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'username': request.args.get('username'), 'message': request.args.get('message')})
    
    return render_template('timeline_create.html', username=username, message=message)
```

```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <form action="/timeline/create" target="_blank">
        <input type="text" name="username"> 
        <input type="text" name="message"> 
        <input type="submit" value="Go">
    </form>    
</body>

</from>
```

```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <ul>
        <li>{{ username }} : {{ message }}</li>
    </ul>
        
</body>

</from>
```

#### * csv 추가, redirect 사용

```python
from flask import redirect
# csv
@app.route('/timeline')
def timeline():
    # 지금까지 기록되어있는 방명록들을 보여주자!
    with open('timeline.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        a= dict()
        for row in reader:
            a.update({row['username'] : row['message']})
    return render_template('timeline.html', a=a)

@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    # DictWriter / timeline.csv / encoding / fieldnames
    with open('timeline.csv', 'a', newline='', encoding='utf-8') as f:
        fieldnames = ('username', 'message')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writerow({'username': request.args.get('username'), 'message': request.args.get('message')})
    
    # return render_template('timeline_create.html', username=username, message=message)
    return redirect('/timeline')
```

```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <form action="/timeline/create">
        <input type="text" name="username">
        <input type="text" name="message">
        <input type="submit" value="Go">
    </form>

    <!--flask에서 받은 객체(딕셔너리 형태)를 받아서 반복문으로 출력-->
    <ul>
    
        {% for key, value in a.items() %}
        <li>{{ key }} : {{ value }} </li>
        {% endfor %}
        
    </ul>

</body>

</from>
```

```html
<!DOCTYPE html>
<html lang="ko">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>

</head>


<body>
    <ul>
        <li>{{ username }} : {{ message }}</li>
    </ul>
        
</body>

</from>
```

