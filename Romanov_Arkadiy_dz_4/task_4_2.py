import requests

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = requests.get(url)
print(response.text)


# def currency_rates(money):
#     if money == 'USD':
