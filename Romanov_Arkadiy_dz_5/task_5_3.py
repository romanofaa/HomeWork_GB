tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б']

def my_gen(one, two):
    for el in range(0, len(one)):
        list_1 = []
        if el < len(two):
            list_1.append(one[el])
            list_1.append(two[el])
        else:
            list_1.append(one[el])
            list_1.append(None)
        yield tuple(list_1)


print(type(my_gen(tutors, klasses)), *my_gen(tutors, klasses), sep='\n')