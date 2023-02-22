def game(heap1, heap2, moves, to):
    if heap1 + heap2 >= 91:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    result = [game(heap1 + 1, heap2,moves + 1, to),
              game(heap1 * 4, heap2, moves + 1, to),
              game(heap1, heap2 + 1, moves + 1, to),
              game(heap1, heap2 * 4, moves + 1, to)]
    return any(result) if (to + 1) % 2 == moves % 2 else all(result)


print(f'19: {[s for s in range (1, 86) if not game(5, s, 0, 1) and game(5, s, 0, 2)]}')
print(f'20: {[s for s in range (1, 86) if not game(5, s, 0, 1) and not game(5, s, 0, 2) and game(5, s, 0, 3)]}')
print(f'21: {[s for s in range (1, 86) if not game(5, s, 0, 2) and game(5, s, 0, 4) and  not game(5, s, 0, 2)]}')