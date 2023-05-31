def game(heap, step, moves):
    if heap >= 64:
        return moves % 2 == step % 2
    if step == moves:
        return 0
    result = [game(heap + 1, step + 1, moves),
              game(heap * 3, step + 1, moves)]
    return any(result)


def game1(heap, step, moves):
    if heap >= 64:
        return moves % 2 == step % 2
    if step == moves:
        return 0
    result = [game1(heap + 1, step + 1, moves),
              game1(heap * 3, step + 1, moves)]
    return any(result) if (moves + 1) % 2 == step % 2 else all(result)


print('19:', [s for s in range(1, 64) if not game1(s, 0, 1) and game1(s, 0, 2)])
print('20:', [s for s in range(1, 64) if not game1(s, 0, 1) and game1(s, 0, 3)])
print('21:', [s for s in range(1, 64) if not game1(s, 0, 2) and (game1(s, 0, 2) or game1(s, 0, 4))])