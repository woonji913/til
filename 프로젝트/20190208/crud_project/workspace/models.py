from flask_sqlalchemy import SQLAlchemy

# sqlalchemy 초기화
db = SQLAlchemy()


class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20), unique=True, nullable=False)
    title_en = db.Column(db.String(20), unique=True, nullable=False)
    audience = db.Column(db.Integer, nullable=False)
    open_date = db.Column(db.String(20), nullable=False)
    genre = db.Column(db.String(20), nullable=False)
    watch_grade = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float, nullable=False)
    poster_url = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    