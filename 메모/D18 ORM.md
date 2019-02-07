# D18 ORM

20190207 목요일



* CRUD

* ORM (Object-Relational Mapping)

----------------------

> sql   <=>    orm  <=>   python object 

-------------------------

**장점**

1. 체지향적인 코드로 인해 직관적이고 비즈니스 로직에 더 집중할 수 있게 한다.

2. 객체 지향적으로 접근할 수 있다.

3. 재사용, 유지보수가 편하다. (재활용 가능)

4. DB에 대한 종속성이 줄어든다.



**단점**

1. 오로지 ORM으로만은 거대한 서비스를 구현하기가 어렵다.
2. 어느정도의 속도 저하.(중간에 단계가 하나 더 생긴 것이기 때문.)



**단점보다 장점이 더 크기 때문에 ORM을 사용한다.**

--------

### 1. 설치 (bash에서)

```bash
pip install Flask-SQLALchemy
pip install Flask-Migrate

pip install flask_sqlalchemy
pip install flask_migrate
```

### 2. 초기설정 (app.py)

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# flask app에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
# ㄴ> sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등을 추적함. 과도한 메모리 사용.
```

### 3. sqlalchemy 초기화

```python
db = SQLAlchemy(app)
migrate = Migrate(app, db)
```

### 4. Table 만들기 (py에서는 class 만들기)

```python
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
     def __repr__(self):
        return f"<User '{self.username}'>"
```

* bash에

```bash
flask db init
flask db migrate
flask db upgrade
```
### 5. sqlite와의 차이
* 값 넣기

```bash
python
Python 3.6.7 (default, Jan 30 2019, 06:16:48) 
[GCC 4.8.4] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from app import *  # app 메소드를 사용하겠다.
>>> user = User(username='woonji', email='example@gmail.com')
>>> db.session.add(user)
>>> db.session.commit()
>>> user.username
'woonji'
>>> user.email
'example@gmail.com'
```

***아래와 같음 **

```sql
INSERT INTO users (username, email)
VALUES ('woonji', 'example@gmail.com');
```

=

```python
user = User(username='woonji', email='example@gmail.com')
```

* SELECT 

```sql
SELECT * FROM users;
users = User.query.all()
```

```sql
SELECT * FROM users WHERE username='woonji';
users = User.query.filter_by(username='woonji').all()
```

```sql
SELECT * FROM users WHERE username='woonji' LIMIT 1;
user = User.query.filter_by(username='woonji').first()
```

* 찾는 값이 없을 때

```python
miss = User.query.filter_by(username='ssafy').first()
# 값이 없을 때.
type(miss)
<class 'NoneType'>
```

* primary key 접근 >> 얘만 get으로 가져올 수 있음.

```sql
SELECT * FROM users WHERE id=1;
user = User.query.get(1)
```

* LIKE

```python
user = User.query.filter(User.email.like('%exam')).all()
user = User.query.limit(1).offset(2).all()
```

* update

```python
user = User.query.get(1)
user.username = 'NewName'
db.sesstion.commit()
user.username # 이름이 달라져 있다.
```

* delete

```python
user = User.query.get(1)
db.session.delete(user)
db.session.commit()
```

---------------------------

### 모델 분리

app.py

```python
from flask import Flask
from flask_migrate import Migrate
from models import db, User

app = Flask(__name__)

# flask app에 sqlalchemy 관련 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 
# ㄴ> sqlalchemy 데이터베이스 객체 수정 및 신호 방출 등을 추적함. 과도한 메모리 사용.

#sqlalchemy 초기화(달라짐)
db.init_app(app)
migrate = Migrate(app, db)
```

models.py

```python
from flask_sqlalchemy import SQLAlchemy

#  모델 초기화 여기서 다시
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

<bash 에서>

```
flask db init
flask db migrate
flask db upgrade
```



CREATE Read(for)

DELETE

UPDATE (기존의 값을 불ㄹ온 다음에 새로운값 넣고 이걸 다시 넣어줘야)