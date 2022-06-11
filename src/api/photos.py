from flask import Blueprint, jsonify, abort, request
from ..models import Photo, User, db

bp = Blueprint('photos', __name__, url_prefix='/photos')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def get_photos():
    photos = Photo.query.all()  # ORM performs SELECT query
    result = []
    for p in photos:
        result.append(p.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def get_photo(id: int):
    p = Photo.query.get_or_404(id)
    return jsonify(p.serialize())


@bp.route('', methods=['POST'])
def create_photo():
    # req body must contain user_id and photo_size
    if 'account_id' not in request.json or 'photo_size' not in request.json:
        return abort(400)
    if 'photo_name' in request.json:
        photo_name = request.json['photo_name']
    # user with id of user_id must exist
    User.query.get_or_404(request.json['account_id'])
    # construct Tweet
    p = Photo(
        photo_name=photo_name if photo_name else None,
        photo_size=request.json['photo_size'],
        account_id=request.json['account_id']
    )
    db.session.add(p)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(p.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update_photo(id: int):
    # req body must contain account_id
    if 'account_id' not in request.json:
        return abort(400)
    # user account_id must exist
    User.query.get_or_404(request.json['account_id'])
    p = Photo.query.get_or_404(id)
    # update photo
    if 'photo_name' in request.json:
        p.photo_name = request.json['photo_name']
    if 'photo_size' in request.json:
        p.photo_size = request.json['photo_size']
    # execute PUT statement
    db.session.commit()
    return jsonify(p.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    p = Photo.query.get_or_404(id)
    try:
        db.session.delete(p)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)
