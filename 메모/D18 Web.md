# D18 Web

1. app.py

```python
import os
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)

# flask app에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


#sqlalchemy 초기화
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
# 뷰 함수
def index():
    # url_for('index') =>>> '/'
    # return redirect(url_for('index'))
    users = User.query.all()
    return render_template('index.html', users=users)

#create    
@app.route('/users/create')
def create():
    username = request.args.get('username')
    email = request.args.get('email')
    user = User(username=username, email=email)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))

#delete
@app.route('/users/delete/<int:id>')
def delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('index'))

# update
@app.route('/users/edit/<int:id>')
def edit(id):
    user = User.query.get(id)
    return render_template('edit.html', user=user)
    
@app.route('/users/update/<int:id>')
def update(id):
    user = User.query.get(id)
    username = request.args.get('username')
    email = request.args.get('email')
    
    user.username = username
    user.email = email
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```



2. models.py

```python
from flask_sqlalchemy import SQLAlchemy

#  모델 초기화
db = SQLAlchemy()

# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f"<User '{self.username}'>"
```



3. index.html

```html
{% extends  "base.html" %}
{% block title %}Index{% endblock %}
{% block head %}
{{ super() }} <!--부모꺼 그대로 상속된거 유지-->
    <link rel="stylesheet" href="style.css" type="text/css" />
{% endblock %}
{% block body %}
    <form action="/users/create">
        <input type="text"  name="username"/>
        <input type="email"  name="email"/>
        <input type="submit" value="Submit"/>
    </form>
    <ul>
        {% for user in users %}
            <li>
                {{ user.username }} : {{ user.email }}
                <a href="/users/delete/{{user.id}}">[DELETE]</a>
                <a href="/users/edit/{{user.id}}">[EDIT]</a>
            </li>
        {% endfor %}
    </ul>

{% endblock %}
```



4. base.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <!-- block 태그는 파생된 탬플릿이 변경할 수 있는 항목을 정의함.-->
    {% block head %}
    	<link rel='icon' href="{{ url_for('static', filename='favicon.png) }}" type="image/png"/> 
    <!-- 파비콘, static 폴더 알아서 만들어야 한당. -->
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>{% block title %}{% endblock %} - My WebPage</title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/css/bootstrap.min.css" integrity="sha384-GJzZqFGwb1QTTN6wy59ffF1BuGJpLSa9DkKMp0DgiMDm4iYMj70gZWKYbI706tWS" crossorigin="anonymous">
    {% endblock %}
</head>

<body>
    <div class='container'>
        <h1>이것은 BASE의 h1입니다.</h1>
        {% block body %}
        {% endblock %}
    </div>


    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.6/umd/popper.min.js" integrity="sha384-wHAiFfRlMFy6i5SRaxvfOCifBUQy1xHdJ/yoi7FRNXMRBu5WHdZYu1hA6ZOblgut" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.2.1/js/bootstrap.min.js" integrity="sha384-B0UglyR+jN6CkvvICOB2joaf5I4l3gm9GU6Hc1og6Ls7i6U/mkkaduKaBhlAXv9k" crossorigin="anonymous"></script>
</body>

</html>
```



5. edit.html

```html
{% extends "base.html" %}
{% block body %}
    <h1>여기는 수정페이지입니다.</h1>
    <form action='/users/update/{{ user.id }}'>
        <input type="text" value="{{ user.username }}" name="username"/>
        <input type="text" value="{{ user.email }}" name="email"/>
        <input type="submit" name="Submit"/>
    </form>
{% endblock %}
```

