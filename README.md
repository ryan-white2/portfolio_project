# Social Media App

Ryan White

## Portfolio Project

This is a simple social media app with users, posts, photos

### API Reference Table of endpoint paths, methods, parameters

| Name         | endpoint paths      | methods | parameters       |
| ------------ | ------------------- | ------- | ---------------- |
| get_users    | `/users`            | GET     | None             |
| get_user     | `/users/account_id` | GET     | <int:account_id> |
| create_user  | `/users`            | POST    | <int:account_id> |
| update_user  | `/users/account_id` | PUT     | <int:account_id> |
| delete_user  | `/users/account_id` | DELETE  | <int:account_id> |
| get_posts    | `/posts`            | GET     | None             |
| get_post     | `/posts/post_id`    | GET     | <int:post_id>    |
| create_post  | `/posts`            | POST    | <int:post_id>    |
| update_post  | `/posts/post_id`    | PUT     | <int:post_id>    |
| delete_post  | `/posts/post_id`    | DELETE  | <int:post_id>    |
| get_photos   | `/photos`           | GET     | None             |
| get_photo    | `/photos/photo_id`  | GET     | <int:photo_id>   |
| create_photo | `/photos`           | POST    | <int:photo_id>   |
| update_photo | `/photos/photo_id`  | PUT     | <int:photo_id>   |
| delete_photo | `/photos/photo_id`  | DELETE  | <int:photo_id>   |

## Retrospective answering of the following questions:

#### **How did the project's design evolve over time?**

I had to consolidate the user account and login tables into one table for simplicity.

#### **Did you choose to use an ORM or raw SQL? Why?**

I used ORM with Flask and SQLalchemy because I wanted more experience with that.

#### **What future improvements are in store, if any?**

It would be good to implement a like and unlike functionality.
