from flask import Flask

from routes.region_route import bp as region_route_bp
from routes.car_route import bp as car_route_bp
from routes.area_route import bp as area_route_bp

app = Flask(__name__)
app.register_blueprint(region_route_bp)
app.register_blueprint(car_route_bp)
app.register_blueprint(area_route_bp)

if __name__ == '__main__':
    app.run()
