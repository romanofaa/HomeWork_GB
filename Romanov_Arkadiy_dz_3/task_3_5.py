import random

def get_jokes(n):
    """Эта функция генерирует шутки"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    get = []
    i = 0
    while i < n:
        one = random.randrange(len(nouns))
        two = random.randrange(len(adverbs))
        thrie = random.randrange(len(adjectives))
        get = [nouns[one]] + [adverbs[two]] + [adjectives[thrie]]
        del nouns[one], adverbs[two], adjectives[thrie]
        print(get)
        i += 1

get_jokes(2)



