# Дан список, содержащий искажённые данные с должностями и именами сотрудников:

work_list = [
    'инженер-конструктор Игорь',
    'главный бухгалтер МАРИНА',
    'токарь высшего разряда нИКОЛАй',
    'директор аэлита']

for idx in range(len(work_list)):
    work_list[idx] = work_list[idx].split(' ')
    work_list[idx][-1] = work_list[idx][-1].title()
    work_list[idx] = ' '.join(work_list[idx])

print(work_list)