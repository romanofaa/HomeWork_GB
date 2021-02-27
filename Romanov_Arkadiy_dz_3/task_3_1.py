def num_translate(num = input('> ')):
    dict_1 = {
        'one': 'один',
        'two': 'два',
        'thrie': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }

    for _ in dict_1:
        if _ == num:
            print(dict_1[_])
            break
    else:
        print('Нет таких')
        return None

num_translate()

