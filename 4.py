# Задание на защиту:
# Беларусь, Гомель, Советская, 25, 3;   Россия, Москва, Ленина, 2;   Украина, Победы, 17, 5, 4;   Россия, Москва, Радости, 58, 48, 14


import re

s = input()
m = re.findall("[А-Я][а-я]*, [А-Я][а-я]*, [А-Я][а-я]*, [0-9]*, [0-9]*,? ?[0-9]*", s)
print(m)