def game(heap, moves, step, op):
    if heap >= 34:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    result = []
    if moves % 2 == 1:
        if op == 1:
            result = [game(heap + 2, moves + 1, step, op), game(heap * 2, moves + 1, step, op)]
        elif op == 2:
            result = [game(heap + 1, moves + 1, step, op), game(heap * 2, moves + 1, step, op)]
        elif op == 3:
            result = [game(heap + 1, moves + 1, step, op), game(heap + 2, moves + 1, step, op)]
    else:
        result = [game(heap + 1, moves + 1, step, 1), game(heap + 2, moves + 1, step, 2),
                  game(heap * 2, moves + 1, step, 3)]
    return any(result) if ((moves + 1) % 2 == step % 2) else all(result)


def game1(heap, moves, step, op):
    if heap >= 34:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    result = []
    if moves % 2 == 1:
        if op == 1:
            result = [game1(heap + 2, moves + 1, step, op), game1(heap * 2, moves + 1, step, op)]
        elif op == 2:
            result = [game1(heap + 1, moves + 1, step, op), game1(heap * 2, moves + 1, step, op)]
        elif op == 3:
            result = [game1(heap + 1, moves + 1, step, op), game1(heap + 2, moves + 1, step, op)]
    else:
        result = [game1(heap + 1, moves + 1, step, 1), game1(heap + 2, moves + 1, step, 2),
                  game1(heap * 2, moves + 1, step, 3)]
    return any(result) if ((moves + 1) % 2 == step % 2) else all(result)


print(f'19: {min(s for s in range(1, 33) if not game(s, 0, 1, 0) and game(s, 0, 2, 0))}')
print(f'20: {[s for s in range(1, 33) if not game(s, 0, 1, 0) and game(s, 0, 3, 0)]}')
print(f'21: {[s for s in range(1, 33) if game1(s, 0, 4, 0) and not game1(s, 0, 2, 0)]}')
