from dict import tax_dict
from flask import Blueprint, request, jsonify, abort

bp = Blueprint('area_route', __name__)


@bp.route("/v1/add/tax", methods=['POST'])
def add_tax():
    data = request.get_json()
    code = data['city_id']
    tax = data['rate']
    if code in tax_dict:
        abort(400)
    else:
        tax_dict[code] = tax
        message = {'message': 'Tax with code added'}
        return jsonify(message), 201


@bp.route("/v1/update/tax", methods=['POST'])
def update_tax():
    data = request.get_json()
    code = data['code']
    tax = data['tax']
    if code in tax_dict:
        tax_dict[code] = tax
        message = {'message': f'Tax with code updated'}
        return jsonify(message), 201
    else:
        abort(400)


@bp.route("/v1/fetch/taxes", methods=['GET'])
def fetch_taxes():
    return jsonify(tax_dict), 200


@bp.route('/v1/fetch/tax', methods=['GET'])
def fetch_tax():
    code = request.args.get('code')
    if code in tax_dict:
        message = {"Tax": tax_dict[code]}
        return jsonify(message), 200
    else:
        abort(400)


@bp.route('/v1/fetch/calc', methods=['GET'])
def fetch_calc():
    code = request.args.get('city_id')
    cadastral_value = int(request.args.get('rate'))
    # month_of_ownership = int(request.args.get('month_of_ownership'))
    if code in tax_dict:
        tax = int(tax_dict[code])
        # tax_for_year = (cadastral_value * tax * month_of_ownership)/12
        tax = cadastral_value * tax
        # message = {"Tax amount for the year": tax_for_year}
        message = {"Tax amount": tax}
        return jsonify(message), 200
    else:
        abort(400)

