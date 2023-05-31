def game(heap, moves, step, op):
    if heap >= 50:
        return moves % 2 == step % 2
    if step == moves:
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


print('19:', [s for s in range(1, 50) if not game(s, 0, 1, 0) and game(s, 0, 2, 0)])
print('20:', [s for s in range(1, 50) if not game(s, 0, 1, 0) and game(s, 0, 3, 0)])
print('21:', [s for s in range(1, 50) if not game(s, 0, 2, 0) and (game(s, 0, 2, 0) or game(s, 0, 4, 0))])