# D19 Project 선수학습

첫 설정

1. app.py

```python
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db에 app 연동
db.init_app(app)

# migrate 초기화
migrate = Migrate(app, db)

@app.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)
    

# @app.route('/users/create') #unique한 페이지 url
@app.route('/users/create/') # 후방 슬레쉬 없이 엑세스 하면 슬레쉬가 있는 url로 잡아줌
def create():
    nickname = request.args.get('nickname')
    address = request.args.get('address')
    user = User(nickname=nickname, address=address)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)
```

2. models.py

```python
from flask_sqlalchemy import SQLAlchemy

# sqlalchemy 초기화
db = SQLAlchemy()

# sqlalchemy datatype
# ㄴ> Integer / String(*size) / Text / DateTime / Float / Boolean
# *은 안써도 됨

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(20), nullable=False)
```

3. index.html

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
    <h1>INDEX</h1>
    <form action='/users/create/'>
        <input type="text" name="nickname" required/>
        <input type="text" name="address" required />
        <input type="submit" value="Submit"/>
    </form>
    
    <h2>주소록</h2>
    <ul>
        {% for user in users %}
            <li>
                닉네임: {{ user.nickname }} / 주소: {{ user.address }}
            </li>
        {% endfor %}
    </ul>
</body>
</html>
```

