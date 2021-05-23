import requests

def currency_rates(money):
    if money not in list_money: return None
    for idx in content:
        if idx[:3] == money:
            course = idx.split('</Name><Value>')
    return course[1][:7]

# data retrieval
response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
my_string = response.text
content = my_string.split("</NumCode><CharCode>")

# create list
list_money = []
for idx in range(1, len(content)):
    list_money.append(content[idx][0:3])
    print(content[idx][0:3])

money = input('\nenter the currency from the given list or enter "0": ')
money = money.upper()
result = currency_rates(money)

print(f'exchange rate {money} today is equal to {result}')