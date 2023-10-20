from tax_param_dict import tax_param_dict
from flask import Blueprint, request, jsonify, abort

bp = Blueprint('car_route', __name__)


@bp.route('/v1/add/tax-param', methods=['POST'])
def add_tax_param():
    data = request.get_json()
    city_id = data['city_id']
    from_hp_car = data['from_hp_car']
    to_hp_car = data['to_hp_car']
    from_production_year_car = data['from_production_year_car']
    to_production_year_car = data['to_production_year_car']
    rate = data['rate']

    if city_id in tax_param_dict:
        abort(400)
    else:
        message = {'message': 'Tax-param with city_id added'}
        return jsonify(message), 200


@bp.route('/v1/calc/tax', methods=['GET'])
def calc_car_tax():
    data = request.get_json()
    code = data['city_id']
    rate = data['rate']
    horse_power = data['from_hp_car']
    horse_power = data['to_hp_car']

    if code in tax_param_dict:
        tax = rate * horse_power
        return {'message': 'Результат расчета налога: '}, tax, 200
    else:
        message = {'message': 'Error calculation tax'}
        return jsonify(message), 400
