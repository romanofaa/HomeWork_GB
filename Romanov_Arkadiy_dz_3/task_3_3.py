def thesaurus(*users):
    users_dict = {}

    for i in users:
        if i[0] in users_dict:
            users_dict[i[0]] = [users_dict[i[0]]] + [i]
        users_dict.setdefault(i[0], i)

    print(users_dict)


thesaurus('Ваня', 'Петя', 'Дима', 'Вениамин', 'Женя', 'Даниил')

