20190130 수요일

# D15 Flask

## flask 기초1

* 프로그래밍 폰트
* web 프로젝트 정리
* gitlab
* flask c9 setting
* flask datetime
* flask variable routing
* render templete
* flask 조건 반복
* 참고 사이트

http://flask.pocoo.org/docs/1.0/quickstart/#rendering-templates

http://flask.pocoo.org/docs/0.12/tutorial/templates/

http://jinja.pocoo.org/docs/2.10/templates/#for

### 1. c9 setting

```py
# install pyenv
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
source ~/.bashrc
pyenv install 3.6.7
pyenv global 3.6.7
pyenv rehash


# install pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc


# etc
python -V
pip install -U pip
pip install flask
pip install requests
pip freeze > req.txt
```



### 2. flask

```jinja2
from flask import Flask, render_template
import os
import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello there!'
    
# 5월 20일부터 d-day카운트 출력
@app.route('/dday')
def dday():
    time_now = datetime.datetime.now()
    time_dday = datetime.datetime(2019, 5, 20)
    d_day = time_dday - time_now
    return f'{d_day.days}일 남았습니다.'

# variable routing
@app.route('/hi/<string:name>')
# def hi(name):
#     return f'안녕, {name}'
def greeting(name):
    return render_template('greeting.html', name=name)
    
    
    
@app.route('/cube/<int:num>')
def cube(num):
    return f'{num}의 세제곱은 {num**3}입니다~'
    
# 반복문
@app.route('/movie')
def movie():
    movies = ['극한직업', '정글북', '캡틴마블', '보헤미안랩소디', '완벽한 타인']
    return render_template('movie.html', movies=movies)



if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

### 3. html

```html
{% if name == '운지' %}
    <h1>안녕 {{ name }} 왔니?</h1>
{% else %}
    <h1>{{ name }} 너 누구야?</h1>
{% endif %}
<!--이름이 내 이름으로 들어오면 누구누구 왔니?
다른 이름으로 값이 넘어오면 누구누구 너 누구야?-->
```

```html
<!--ul 리스트에 있던 영화를 출력해주세요. (for문으로)-->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS"
        crossorigin="anonymous">
</head>


<body>
<div class="container">
    <h1>영화 목록</h1>
    
    <div class="row">

        {% for movie in movies %}
        <div class="card" style="width: 18rem;">
            <img src="..." class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{{ movie }}</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
            </div>
        </div>


        {% endfor%}

    </div>
</div>
</body>
```

