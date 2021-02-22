# создаем и наполняем список
list_1 = []
x = 1
y = None

while x <= 1000:
    if (x % 2) > 0:
        y = x
        y **= 3
        list_1.append(y)
    x += 1

# вычисляем сумму элементов списка, у которых сумма цифр кратна 7-ми
glob_sum = 0
for idx in range(len(list_1)): # проходим по списку
    elem = str(list_1[idx])     # вытаскиваем элемент
    sum = 0
    for idx_elem in range(len(elem)): # получаем сумму цифр элемента
        sum += int(elem[idx_elem])
    if sum % 7 == 0:                   # проверяем на кратность 7-ми
        glob_sum += list_1[idx]

print(glob_sum)

# Прибавляем 17 к каждому элементу списка (вариант с доп списком)
list_2 = []
for idx_17_1 in range(len(list_1)):
    list_2.append(list_1[idx_17_1] + 17)

print(list_2)

# снова вычисляем сумму элементов списка, у которых сумма цифр кратна 7-ми
glob_sum = 0
idx = 0
for idx in range(len(list_2)): # проходим по списку
    elem = str(list_2[idx])     # вытаскиваем элемент
    sum = 0
    idx_elem = 0
    for idx_elem in range(len(elem)): # получаем сумму цифр элемента
        sum += int(elem[idx_elem])
    if sum % 7 == 0:                   # проверяем на кратность 7-ми
        glob_sum += list_1[idx]

print(glob_sum)

# Прибавляем 17 к каждому элементу списка (вариант без доп списка)
for idx_17_2 in range(len(list_1)):
    list_1[idx_17_2] += 17

print(list_1)


