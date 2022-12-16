def game(heap, moves, step, op):
    if heap >= 29:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    result = []
    if op == 1:
        result = [game(heap + 2, moves + 1, step, op), game(heap * 2, moves + 1, step, op)]
    elif op == 2:
        result = [game(heap + 1, moves + 1, step, op), game(heap * 2, moves + 1, step, op)]
    elif op == 3:
        result = [game(heap + 1, moves + 1, step, op), game(heap + 2, moves + 1, step, op)]
    if moves % 2 == 0:
        return all(result)
    else:
        return any(result)


print(f'19: {min(s for s in range(1, 28) if not game(s, 0, 1, 0) and game(s, 0, 3, 0))}')