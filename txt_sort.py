# 9.11.7
import sys
import re
from operator import itemgetter


def main(txt: str) -> None:
    return printer(sorter(counter(modificator(txt))))


def modificator(txt: str) -> list:
    filtered_words = []
    for string in list(map(lambda x: x.split(), txt)):
        for word in string:
            word = re.sub(r'[^\w\s]', '', word)
            filtered_words.append(word.strip().lower())

    filtered_words_len = [word for word in filtered_words if len(word) >= 3]
    return filtered_words_len


def counter(filtered: list) -> dict:
    counted_words = {word: filtered.count(word) for word in filtered}
    return counted_words


def sorter(counted_words: dict) -> dict:
    first_sort = sorted(counted_words.items(), key=itemgetter(0))
    second_sort = sorted(first_sort, key=itemgetter(1), reverse=True)
    words = dict(second_sort[0:10])
    return words


def printer(words: dict) -> None:
    print('10 самых часто встречающихся слов в этом тексте:\n')
    for key, value in words.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    main(sys.stdin.readlines())
