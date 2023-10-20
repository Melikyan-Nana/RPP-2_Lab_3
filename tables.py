from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)


class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)


new_region = Region(name='Новосибирск')
db.session.add(new_region)

filtered_regions = Region.query.filter(Region.name == 'Новосибирск')


class CarTaxParam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, foreign_key=Region.id, nullable=False)
    from_hp_car = db.Column(db.Integer, nullable=False)
    to_hp_car = db.Column(db.Integer, nullable=False)
    from_production_year_car = db.Column(db.Integer, nullable=False)
    to_production_year_car = db.Column(db.Integer, nullable=False)
    rate = db.Column(db.Integer, nullable=False)


new_car_tax_param = CarTaxParam(city_id=1, from_hp_car=150, to_hp_car=200, from_production_year_car=2022,
                                to_production_year_car=2023, rate=5)
db.session.add(new_car_tax_param)


class AreaTaxParam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city_id = db.Column(db.Integer, foreign_key=Region.id, nullable=False)
    rate = db.Column(db.Integer, nullable=False)


new_area_tax_param = AreaTaxParam(city_id=1, rate=5)
db.session.add(new_area_tax_param)
