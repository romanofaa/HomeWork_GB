list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for idx in range(len(list_1)):
   # выявляем числа со знаком
   # которые < 10
    if (list_1[idx][0] == '+' or list_1[idx][0] == '-') and list_1[idx][1:].isdigit():
        if int(list_1[idx][1:]) < 10:
            list_1[idx] = '"' + list_1[idx][0] + '0' + list_1[idx][1] + '"'
        # остальные
        else:
            list_1[idx] = '"' + list_1[idx][0] + list_1[idx][1] + '"'
    # выявляем числа без знака
    if list_1[idx].isdigit():
        if int(list_1[idx]) < 10:
            list_1[idx] = '0' + list_1[idx]
        list_1[idx] = '"' + list_1[idx] + '"'

use_str = ' '.join(list_1) # объединяем в строку
print(use_str)










# # объединяем все элементы списка в строку
# use_str = ' '.join(list_1)
# print(use_str)
# print(len(use_str))
#
# # присваиваем всем числам тип int и создаем новый список
# use_list = []
# for idx in range(len(use_str)):
#     if use_str[idx].isdigit():
#         use_list.append(int(use_str[idx]))
#     else:
#         use_list.append(use_str[idx])
#
# for idx in range(len(use_list)):
#     if type(use_l








