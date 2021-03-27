import requests
import json
from dotenv import dotenv_values
import pandas as pd

#load_dotenv()
config = dotenv_values(".env")

key = config['VANTAGEAPI']
ticker = 'AAPL'
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={}&apikey={}'.format(ticker, key)
response = requests.get(url)
data = [row.strip().split(',') for row in response.text.split('\n')]

df_API = pd.DataFrame(data[1:-1], columns=data[0])

print(df_API.head())









###Citations:
#https://github.com/theskumar/python-dotenv
#https://www.alphavantage.co/documentation/#
#https://medium.com/@patrick.collins_58673/stock-api-landscape-5c6e054ee631