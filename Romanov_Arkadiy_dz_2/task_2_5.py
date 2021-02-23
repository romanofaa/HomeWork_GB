prices = [57.8, 46.51, 97, 48.05, 34.23, 7.6, 23, 45.45, 67.3, 8]

for i in range(len(prices)):
    prices[i] = str(prices[i])
    prices[i] = prices[i].split('.')

for i in range(len(prices)):
    if len(prices[i]) < 2:
        prices[i].append('00')
    # if len(prices[i][0]) < 2:
    #     prices[i][0] = '0' + prices[i][0]
    if len(prices[i][1]) < 2:
        prices[i][1] = '0' + prices[i][1]

for i in range(len(prices)):
    prices[i][0] = prices[i][0] + ' руб'
    prices[i][1] = prices[i][1] + ' коп'
    prices[i] = ' '.join(prices[i])

print(prices)