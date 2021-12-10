import os
from kucoin.client import Client
import config

client = Client(config.API_KEY,config.API_SECRET,config.API_Passphrase)

#currencies = client.get_currencies()
price = client.get_ticker()
#print(price)

for coin in price['ticker']:
    print(coin['symbol']+': '+coin['buy'])

# for currency in currencies:
#     print(currency['fullName']+": "+)