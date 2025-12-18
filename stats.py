from collections import defaultdict

def count_words(text):
    return len(text.split())


def count_chars(text):
    text = text.lower()
    num_chars = defaultdict(int)
    
    for char in text:
        num_chars[char] += 1
    
    return num_chars


def sort_on(items):
    return items['num']


def sort_dict_list(lista):
    lista.sort(reverse=True, key=sort_on)
    return lista