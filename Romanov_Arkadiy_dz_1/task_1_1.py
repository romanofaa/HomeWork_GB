print("Эта программа оптимизирует количество секунд в поняттный для человека вид.")
time = int(input("\nВведите количество секунд до предстоящего события: \n> "))

min = 60
hour = min * 60
day = hour * 24

# меньше минуты
bef_min = time >= 0 and time < min
# от минуты до часа
bef_hour = time >= min and time < hour
# от часа до суток
bef_day = time >= hour and time < day

rem_days = time // day  # остаток дней
rem_hour = (time % day) // hour # остаток часов
rem_min = ((time % day) % hour) // min # остаток минут
rem_sec = time % 60 # остаток секунд


if time < 0:
    print("Число должно быть положительным")
# до минуты
elif bef_min:
    print(f'До события осталось {time} секунд.')
# до часа
elif bef_hour:
    print(f"До события осталось {rem_min} минут(ы) {rem_sec} секунд(ы)")
# до суток
elif bef_day:
    print(f"До события осталось {rem_hour} часов, {rem_min} минут(ы) и {rem_sec} секунд(ы)")
# от суток и более
else:
    print(f"До события осталось {rem_days} дней, {rem_hour} часов, {rem_min} минут(ы) и {rem_sec} секунд(ы)")