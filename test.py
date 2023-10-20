import requests

url_base = 'http://127.0.0.1:5000/v1/'
add_region_url = f'{url_base}add/region'
add_region_url_result = requests.post(url=add_region_url, json={"id": 54, "name": 'Новосибирск'})
print(f'Результат добавления региона "{add_region_url_result.status_code}": {add_region_url_result.content}')


add_area_tax_url = f'{url_base}add/tax'
add_area_tax_url_tax_result = requests.post(url=add_area_tax_url, json={"city_id": 54, "rate": 100})
print(f'Результат добавления земельного налога "{add_area_tax_url_tax_result.status_code}": {add_area_tax_url_tax_result.content}')

add_car_tax_url = f'{url_base}add/tax-param'
add_car_tax_url_tax_result = requests.post(url=add_car_tax_url, json={"city_id": 54, "from_hp_car": 200,
                                                                      "to_hp_car": 150,
                                                                      "from_production_year_car": 2022,
                                                                      "to_production_year_car": 2023, "rate": 5})
print(f'Результат добавления транспортного налога "{add_car_tax_url_tax_result.status_code}": '
      f'{add_car_tax_url_tax_result.content}')


calc_car_tax_url = f'{url_base}calc/tax'
calc_car_tax_url_result = requests.get(url=calc_car_tax_url)
print(f'Результат расчета транспортного налога "{calc_car_tax_url_result.status_code}": {calc_car_tax_url_result.content}')


calc_tax_url = f'{url_base}fetch/calc'
calc_tax_url_tax_result = requests.get(url=calc_tax_url)
print(f'Результат расчета земельного налога "{calc_tax_url_tax_result.status_code}": {calc_tax_url_tax_result.content}')

