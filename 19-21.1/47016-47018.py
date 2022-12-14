def game(heap, moves, step):
    if heap >= 29:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    result = [game(heap + 1, moves + 1, step),
              game(heap * 2, moves + 1, step),
              game(heap + 2, moves + 1, step)]
    return any(result) if ((moves + 1) % 2 == step % 2) else all(result)


print(f'19:{[for s in range(1, 29) if not game(s, 0, 1) and game(s, 0, 3)}')