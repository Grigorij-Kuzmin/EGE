"""
Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход
делает Петя. За один ход игрок может добавить в кучу один камень, добавить два камня или увеличить количество камней в
куче в два раза. При этом нельзя повторять ход, который этот же игрок делал на предыдущем ходу. Повторять чужие ходы и
свои более старые ходы разрешается.
Чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается, когда количество камней в куче становится не менее 29. Победителем считается игрок, сделавший
последний ход, то есть первым получивший кучу, в которой будет 29 или больше камней. В начальный момент в куче было S
камней, 1⩽S⩽28.
Будем говорить, что игрок имеет выигрышную стратегию, если он может выиграть при любых ходах противника.

19: Укажите наименьшее значение S, при котором Петя не может выиграть за один ход, но у Пети есть выигрышная стратегия,
позволяющая ему выиграть вторым ходом.

"""
def game(heap, step, op):
    if step == 4 and heap >= 29:
        return 1
    elif step == 4 and heap < 29:
        return 0
    elif heap >= 29 and step < 4:
        return 0
    else:
        if step % 2 != 0:
            if step == 1:
                return game(heap + 1, step + 1, 1) or game(heap + 2, step + 1, 2) or game(heap * 2, step + 1, 3)
            elif step == 3:
                if op == 1:
                    return game(heap + 2, step + 1, op) or game(heap * 2, step + 1, op)
                elif op == 2:
                    return game(heap + 1, step + 1, op) or game(heap * 2, step + 1, op)
                elif op == 3:
                    return game(heap + 1, step + 1, op) or game(heap + 2, step + 1, op)
        else:
            return game(heap + 1, step + 1, op) and game(heap + 2, step + 1, op) and game(heap * 2, step + 1, op)


def g(heap, moves, step, op):
    if heap >= 29:
        return moves % 2 == step % 2
    elif moves == step:
        return 0
    if (moves + 1) % 2 == step % 2:
        if (moves + 1) != step:
            return g(heap + 1, moves + 1, step, 1) or g(heap + 2, moves + 1, step, 2) or g(heap * 2, moves + 1, step, 3)
        else:
            if op == 1:
                return g(heap + 2, moves + 1, step, op) or g(heap * 2, moves + 1, step, op)
            elif op == 2:
                return g(heap + 1, moves + 1, step, op) or g(heap * 2, moves + 1, step, op)
            elif op == 3:
                return g(heap + 1, moves + 1, step, op) or g(heap + 2, moves + 1, step, op)
    else:
        return g(heap + 1, moves + 1, step, op) and g(heap + 2, moves + 1, step, op) and g(heap * 2, moves + 1, step, op)

#(f'19: {[s for s in range(1, 29) if game(s, 1, 0)]}')
print(f'19: {[s for s in range(1, 29) if not g(s, 0, 1, 0) and g(s, 0, 3, 0)]}')
