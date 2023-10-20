from regions_dict import regions_dict
from flask import Blueprint, request, jsonify, abort

bp = Blueprint('add_region', __name__)


@bp.route('/v1/add/region', methods=['POST'])
def add_region():
    data = request.get_json()
    code = data['id']
    name = data['name']

    if code in regions_dict:
        abort(400)
    else:
        regions_dict[code] = name
        message = {'message': 'Region with code added'}
        return jsonify(message), 200
