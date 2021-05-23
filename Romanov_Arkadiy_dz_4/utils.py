def currency_rates(money):
    import requests
    money = money.upper()

    # data retrieval
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.text.split("</NumCode><CharCode>")

    # create list
    list_money = []
    for idx in range(1, len(content)):
        list_money.append(content[idx][0:3])

    if money not in list_money: return None
    for idx in content:
        if idx[:3] == money:
            course = idx.split('</Name><Value>')
    return course[1][:7]

