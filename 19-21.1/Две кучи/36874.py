def game(heap1, heap2, moves, to):
    if heap1 + heap2 >= 88:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    result = [game(heap1 + 1, heap2, moves + 1, to),
               game(heap1 * 3, heap2, moves + 1, to),
                game(heap1, heap2 + 1, moves + 1, to),
                 game(heap1, heap2 * 3, moves + 1, to)]
    return any(result) if (to + 1) % 2 == moves % 2 else all(result)


def game1(heap1, heap2, moves, to):
    if heap1 + heap2 >= 88:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    result = [game1(heap1 + 1, heap2, moves + 1, to),
               game1(heap1 * 3, heap2, moves + 1, to),
                game1(heap1, heap2 + 1, moves + 1, to),
                 game1(heap1, heap2 * 3, moves + 1, to)]
    return any(result)


print(f'19: {min([s for s in range(1, 72) if not game1(6, s, 0, 1) and game1(6, s, 0, 2)])}')
print(f'20: {[s for s in range(1, 72) if not game(6, s, 0, 1) and game(6, s, 0, 3)]}')
print(f'21: {max([s for s in range(1, 72) if game(6, s, 0, 2)])}')