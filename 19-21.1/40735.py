"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней.
Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень, добавить два камня
или увеличить количество камней в куче в два раза. При этом нельзя повторять ход, который только что сделал второй игрок.
Чтобы делать ходы, у каждого игрока есть неограниченное количество камней. Игра завершается, когда количество камней в
куче становится не менее 34. Победителем считается игрок, сделавший последний ход, то есть первым получивший кучу,
в которой будет 34 или больше камней. В начальный момент в куче было S камней, 1⩽S⩽33.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.
19: Укажите такое значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть
своим первым ходом.
20: Существует несколько таких значений S, при которых у Пети есть выигрышная стратегия, причём Петя не может выиграть
первым ходом, но может выиграть своим вторым ходом независимо от того, как будет ходить Ваня. Найдите наименьшее и
наибольшее из таких значений S.
21: Найдите значение S, при котором у Вани есть выигрышная стратегия, позволяющая ему выиграть вторым ходом при любой игре Пети,
но у Вани нет стратегии, которая позволяла бы ему гарантированно выиграть первым ходом.
"""


def game(heap, moves, step, op):
    if heap >= 34:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    if op == 1:
        result = [game(heap + 2, moves + 1, step, 2), game(heap * 2, moves + 1, step, 3)]
    elif op == 2:
        result = [game(heap + 1, moves + 1, step, 1), game(heap * 2, moves + 1, step, 3)]
    elif op == 3:
        result = [game(heap + 1, moves + 1, step, 1), game(heap + 2, moves + 1, step, 2)]
    else:
        result = [game(heap + 1, moves + 1, step, 1), game(heap + 2, moves + 1, step, 2),
                  game(heap * 2, moves + 1, step, 3)]
    return any(result) if ((moves + 1) % 2 == step % 2) else all(result)


print(f'19: {min(s for s in range(1, 34) if not game(s, 0, 1, 0) and game(s, 0, 2, 0))}')
print(f'20: {[s for s in range(1, 34) if not game(s, 0, 1, 0) and game(s, 0, 3, 0)]}')
print(f'21: {[s for s in range(1, 34) if game(s, 0, 4, 0) and not game(s, 0, 2, 0)]}')
