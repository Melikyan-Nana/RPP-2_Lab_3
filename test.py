import requests

url_base = 'http://127.0.0.1:5000/v1/'
calc_car_tax_url = f'{url_base}calc/tax'

calc_car_tax_url_result = requests.get(url=calc_car_tax_url)
print(f'Результат расчета транспортного налога "{calc_car_tax_url_result.status_code}": {calc_car_tax_url_result.content}')


calc_tax_url = f'{url_base}fetch/calc'
calc_tax_url_tax_result = requests.get(url=calc_tax_url)
print(f'Результат расчета земельного налога "{calc_tax_url_tax_result.status_code}": {calc_tax_url_tax_result.content}')
