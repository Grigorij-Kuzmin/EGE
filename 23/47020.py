"""
Исполнитель преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 2
3. Умножить на 2
Первая команда увеличивает число на экране на 1, вторая увеличивает его на 2, третья — умножает на 2.
Программа для исполнителя — это последовательность команд. Сколько существует программ, которые
преобразуют исходное число 1 в число 9 и при этом не содержат двух команд умножения подряд?
"""


def f(x, y, flag):
    if x == y:
        return 1
    if x > y:
        return 0
    if flag:
        return f(x + 1, y, True) + f(x + 2, y, True) + f(x * 2, y, False)
    else:
        return f(x + 1, y, True) + f(x + 2, y, True)


print(f(1, 9, True))