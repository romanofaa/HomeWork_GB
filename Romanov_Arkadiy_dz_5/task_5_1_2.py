# первый вариант решения задачи

# def odd_nums(numer):
#     for i in range(1, numer + 1, 2):
#         yield i
#
# gen_to_15 = odd_nums(15)
# print(next(gen_to_15))
# print(next(gen_to_15))

#-------------------------------------------------------------

# второй вариант решения задачи:

number = int(input('enter to number: '))
odd_to = (n for n in range(1, number + 1, 2))
print(*odd_to)
