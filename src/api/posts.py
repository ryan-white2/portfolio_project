from flask import Blueprint, jsonify, abort, request
from ..models import Post, User, db

bp = Blueprint('posts', __name__, url_prefix='/posts')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def get_posts():
    posts = Post.query.all()  # ORM performs SELECT query
    result = []
    for p in posts:
        result.append(p.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def get_post(id: int):
    p = Post.query.get_or_404(id)
    return jsonify(p.serialize())


@bp.route('', methods=['POST'])
def create_post():
    # req body must contain user_id and content
    if 'account_id' not in request.json or 'post_text' not in request.json:
        return abort(400)
    # user with id of user_id must exist
    User.query.get_or_404(request.json['account_id'])
    # construct Tweet
    p = Post(
        post_text=request.json['post_text'],
        account_id=request.json['account_id']
    )
    db.session.add(p)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(p.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update_post(id: int):
    # req body must contain user_id and content
    if 'account_id' not in request.json or 'post_text' not in request.json:
        return abort(400)
    post_text = request.json['post_text']
    # user/post id must exist
    User.query.get_or_404(request.json['account_id'])
    p = Post.query.get_or_404(id)
    # update post
    p.post_text = post_text
    # execute PUT statement
    db.session.commit()
    return jsonify(p.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Post.query.get_or_404(id)
    try:
        db.session.delete(p)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
