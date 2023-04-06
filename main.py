import ui
import requests


OPEN_EXCHANGE_API_ID= '00723b00bfa342669f1a6deb7a81c5e5'
OPEN_EXCHANGE_API_URL= 'https://openexchangerates.org/api'


OPEN_EXCHANGE_HEARDERS={"accept": "application/json"}
data=requests.get(f'{OPEN_EXCHANGE_API_URL}/currencies.json', OPEN_EXCHANGE_API_ID)
currencies=data.json()

currency_list=[f'{key}:{value}' for (key,value) in currencies.items()]




ui=ui.FrontPage(currency_list)

# Write your function below!