"""
Populate PP database with fake data using the SQLAlchemy ORM.
"""

import random
import string
import hashlib
import secrets
from faker import Faker
from twitter.src.models import User, Post, Photo, db, user_friends_table
from twitter.src import create_app

USER_COUNT = 10
POST_COUNT = 20
PHOTO_COUNT = 15
FRIEND_COUNT = 10
SEX = ('M', 'F')
LANGUAGE = ('Chinese', 'Spanish', 'English', 'Hindi', 'Arabic',
            'Portuguese', 'Bengali', 'Russian', 'Japanese', 'Italian', 'French')

# LIKE_COUNT = 400
# assert LIKE_COUNT <= (USER_COUNT * TWEET_COUNT)


def random_passhash():
    """Get hashed and salted password of length N | 8 <= N <= 15"""
    raw = ''.join(
        random.choices(
            string.ascii_letters + string.digits + '!@#$%&',  # valid pw characters
            k=random.randint(8, 15)  # length of pw
        )
    )

    salt = secrets.token_hex(16)

    return hashlib.sha512((raw + salt).encode('utf-8')).hexdigest()


def truncate_tables():
    """Delete all rows from database tables"""
    db.session.execute(user_friends_table.delete())
    Post.query.delete()
    User.query.delete()
    db.session.commit()


def main():
    """Main driver function"""
    app = create_app()
    app.app_context().push()
    truncate_tables()
    fake = Faker()

    last_user = None  # save last user
    for _ in range(USER_COUNT):
        last_user = User(
            account_name=fake.name(),
            account_email=fake.email(),
            account_phone=random.randint(1111111111, 9999999999),
            account_country=fake.country(),
            account_sex=random.choice(SEX),
            account_language=random.choice(LANGUAGE),
            user_birthdate=fake.date(),
            user_age=random.randint(15, 100),
            account_login=fake.unique.first_name().lower() + str(random.randint(1, 150)),
            account_password=random_passhash()
        )
        db.session.add(last_user)

    # insert users
    db.session.commit()

    last_post = None  # save last post
    for _ in range(POST_COUNT):
        last_post = Post(
            post_text=fake.sentence(),
            account_id=random.randint(
                last_user.account_id - USER_COUNT + 1, last_user.account_id)
        )
        db.session.add(last_post)

    # insert posts
    db.session.commit()

    last_photo = None  # save last photo
    for _ in range(PHOTO_COUNT):
        last_photo = Photo(
            photo_name=fake.sentence(),
            photo_size=random.randint(111, 999999),
            account_id=random.randint(
                last_user.account_id - USER_COUNT + 1, last_user.account_id)
        )
        db.session.add(last_photo)

    # insert photos
    db.session.commit()

    # FRIEND
    # user_friend_pairs = set()
    # end_number = last_user.account_id
    user_friend_pairs = []
    while len(user_friend_pairs) < FRIEND_COUNT:
        candidate = []
        candidate.append(random.randint(1, USER_COUNT))
        candidate.append(random.randint(1, USER_COUNT))
        if len(set(candidate)) < 2 or candidate in user_friend_pairs:
            continue  # pairs must be unique
        user_friend_pairs.append(candidate)

    new_friends = [{"user_account_id": pair[0], "friend_account_id": pair[1]}
                   for pair in list(user_friend_pairs)]
    insert_likes_query = user_friends_table.insert().values(new_friends)
    db.session.execute(insert_likes_query)

    # insert friends
    db.session.commit()


# run script
main()

# random.randint(last_user.account_id - USER_COUNT +
#                1, last_user.account_id),
# random.randint(last_user.account_id - USER_COUNT +
#                1, last_user.account_id)
