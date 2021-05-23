import utils

for i in range(0, 3):
    money = input('\nenter the currency: ')
    print(f'exchange rate {money} today is equal to ', utils.currency_rates(money), '\n')