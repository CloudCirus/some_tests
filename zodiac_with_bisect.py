# 9.9.3
from bisect import bisect

signs = [(1, 19, "Козерог"), (2, 18, "Водолей"), (3, 20, "Рыбы"), (4, 20, "Овен"),
         (5, 20, "Телец"), (6, 20, "Близнецы"), (7, 22, "Рак"), (8, 22, "Лев"),
         (9, 22, "Дева"), (10, 22, "Весы"), (11, 21, "Скорпион"), (12, 21, "Стрелец"),
         (12, 31, "Козерог")]


def main(inp: str) -> str:
    return print(zodiac_sign(validation(inp)))


def zodiac_sign(date: tuple) -> str:
    return signs[bisect(signs, date)][2]


def validation(inp: str) -> tuple:
    inp = inp.split()
    try:
        month, day = map(int, inp)
    except:
        _ooops()
        exit()
    if month > 12 or day > 31 or month == 2 and day > 29:
        _ooops()
        exit()
    return month, day


def _ooops() -> None:
    return print('некорректная дата')


main(input())
