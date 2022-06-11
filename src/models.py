from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index
import datetime

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user_accounts'
    # account_id SERIAL PRIMARY KEY
    account_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # account_name TEXT NOT NULL,
    account_name = db.Column(db.String(128), nullable=False)
    # account_email TEXT NOT NULL UNIQUE,
    account_email = db.Column(db.String(64), unique=True, nullable=False)
    # account_phone BIGINT NOT NULL UNIQUE,
    account_phone = db.Column(db.BigInteger, unique=True, nullable=False)
    # account_country TEXT NOT NULL,
    account_country = db.Column(db.String(32), nullable=False)
    # account_sex CHAR(1) NOT NULL,
    account_sex = db.Column(db.String(1), nullable=False)
    # account_language TEXT NOT NULL,
    account_language = db.Column(db.String(16), nullable=False)
    # account_verified BOOLEAN, -- '0', 'F'
    account_verified = db.Column(db.Boolean, default=0, nullable=False)
    # user_birthdate DATE NOT NULL, -- 'YYYY-MM-DD'
    user_birthdate = db.Column(db.Date, nullable=False)
    # user_age SMALLINT NOT NULL,
    user_age = db.Column(db.SmallInteger, index=True,
                         nullable=False)  # bTree Index
    # account_creation TIMESTAMP NOT NULL,
    account_creation = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    # account_login TEXT NOT NULL UNIQUE,
    account_login = db.Column(db.String(128), unique=True, nullable=False)
    # account_password TEXT NOT NULL
    account_password = db.Column(db.String(128), nullable=False)
    # user posts
    user_posts = db.relationship('Post', backref='User', cascade="all,delete")

    def __init__(self, account_name: str, account_email: str, account_phone: int, account_country: str,
                 account_sex: str, account_language: str, user_birthdate: str, user_age: int, account_login: str, account_password: str):
        self.account_name = account_name
        self.account_email = account_email
        self.account_phone = account_phone
        self.account_country = account_country
        self.account_sex = account_sex
        self.account_language = account_language
        self.user_birthdate = user_birthdate
        self.user_age = user_age
        self.account_login = account_login
        self.account_password = account_password

    def serialize(self):
        return {
            'account_id': self.account_id,
            'account_name': self.account_name,
            'account_email': self.account_email,
            'account_phone': self.account_phone,
            'account_country': self.account_country,
            'account_sex': self.account_sex,
            'account_language': self.account_language,
            'account_verified': self.account_verified,
            'user_birthdate': self.user_birthdate,
            'user_age': self.user_age,
            'account_creation': self.account_creation.isoformat(),
            'account_login': self.account_login
        }


# user_age_index = SQLAlchemy.Index('user_age_idx', User.user_age)
# Index('my_index', my_table.c.data, postgresql_using='gin')
account_verified_index = Index(
    'account_verified_index', User.account_verified, postgresql_using='hash')


class Post(db.Model):
    __tablename__ = 'user_posts'
    # post_id SERIAL PRIMARY KEY,
    post_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # post_text TEXT NOT NULL,
    post_text = db.Column(db.Text, nullable=False)
    # post_time TIMESTAMP NOT NULL,
    post_time = db.Column(
        db.DateTime, default=datetime.datetime.utcnow, nullable=False)
    # account_id INT UNIQUE NOT NULL
    account_id = db.Column(db.Integer, db.ForeignKey(
        'user_accounts.account_id'), nullable=False)
    # liking_users = db.relationship(
    #     'User', secondary=likes_table,
    #     lazy='subquery',
    #     backref=db.backref('liked_tweets', lazy=True)
    # )

    def __init__(self, post_text: str, account_id: int):
        self.post_text = post_text
        self.account_id = account_id

    def serialize(self):
        return {
            'post_id': self.post_id,
            'post_text': self.post_text,
            'post_time': self.post_time.isoformat(),
            'account_id': self.account_id
        }


class Photo(db.Model):
    __tablename__ = 'user_photos'
    # photo_id SERIAL PRIMARY KEY,
    photo_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # photo_name TEXT
    photo_name = db.Column(db.Text)
    # photo_size INT NOT NULL,
    photo_size = db.Column(db.Integer, nullable=False)
    # user_account_id INT UNIQUE NOT NULL
    account_id = db.Column(db.Integer, db.ForeignKey(
        'user_accounts.account_id'), nullable=False)

    def __init__(self, photo_name: str, photo_size: int, account_id: int):
        self.photo_name = photo_name
        self.photo_size = photo_size
        self.account_id = account_id

    def serialize(self):
        return {
            'photo_id': self.photo_id,
            'photo_name': self.photo_name,
            'photo_size': self.photo_size,
            'account_id': self.account_id
        }

# CREATE TABLE user_friends (
#     user_account_id INT UNIQUE NOT NULL,
#     friend_account_id INT UNIQUE NOT NULL,
#     PRIMARY KEY (user_account_id)
# );
#
# ALTER TABLE user_friends
# ADD CONSTRAINT fk_user_account
# FOREIGN KEY (user_account_id)
# REFERENCES user_accounts (account_id);
# ALTER TABLE user_friends
# ADD CONSTRAINT fk_friend_account
# FOREIGN KEY (friend_account_id)
# REFERENCES user_accounts (account_id);


# FRIENDS
user_friends_table = db.Table(
    'user_friends',
    db.Column(
        'user_account_id', db.Integer,
        db.ForeignKey('user_accounts.account_id'),
        primary_key=True
    ),

    db.Column(
        'friend_account_id', db.Integer,
        db.ForeignKey('user_accounts.account_id')
    )
)
