"""
ПРИВЕТ ГРИША
Исполнитель преобразует число на экране. У исполнителя есть три команды, которым присвоены номера:
1. Прибавить 1
2. Умножить на 2
3. Умножить на 3
Первая команда увеличивает число на экране на 1, вторая умножает его на 2, третья — умножает на 3.
Программа для исполнител — это последовательность команд. Сколько существует программ, которые
преобразуют исходное число 2 в число 39, и при этом траектория вычислений содержит число 13 и не содержит числа 30?
"""

def f(x, y):
    if x == y:
        return 1
    if x > y or x == 30:
        return 0
    return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)


print(f(2, 13) * f(13, 39))
