"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди,
первый ход делает Петя. За один ход игрок может добавить в кучу один камень или увеличить количество камней
в куче в два раза. Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.

Игра завершается в тот момент, когда количество камней в куче становится не менее 129. Победителем считается игрок,
сделавший последний ход, т.е. первым получивший кучу из 129 или больше камней.

В начальный момент в куче было S камней, 1 ≤ S ≤ 128.

Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.

19:
Укажите такое значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть
своим первым ходом.

20:
Найдите два наименьших значения S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два
условия:
— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
Найденные значения запишите в ответе в порядке возрастания.

21:
Найдите минимальное значение S, при котором одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
Если найдено несколько значений S, в ответе запишите минимальное из них.
"""


def game(heap, moves, step):
    """
    Игровая функция
    :param heap: размер кучи
    :param moves: текущий ход
    :param step: номер шага, до которого идём
    :return:
    """
    if heap >= 129:
        return moves % 2 == step % 2
    # Дошли до необходимого хода
    if moves == step:
        return 0
    result = [game(heap + 1, moves + 1, step),
              game(heap * 2, moves + 1, step)]
    return any(result) if (moves + 1) % 2 == step % 2 else all(result)


print(f'19: {min(s for s in range(1, 128) if not game(s, 0, 1) and game(s, 0, 2))}')
print(f'20: {[s for s in range(1, 128) if not game(s, 0, 1) and game(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 128) if not game(s, 0, 2) and game(s, 0, 4))}')