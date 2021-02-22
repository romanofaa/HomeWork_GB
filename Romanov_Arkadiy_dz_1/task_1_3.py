use = int(input('введите количество процентов от 1 до 20 \n> '))
perc = "процент"
percent = "процента"
percents = "процентов"


if use < 1 and use > 20:
    print('вы ввели не правильную сумму!')
elif use == 1:
    print(f'получилось {use} {perc}')
elif use > 1 and use < 5:
    print(f'получилось {use} {percent}')
else:
    print(f'получилось {use} {percents}')