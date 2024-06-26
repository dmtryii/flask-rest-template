
from flask import jsonify
from app.users import bp
from app.exceptions.user_exception import InvalidUsage

@bp.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
