def game(heap, step, moves):
    if heap > 200:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    result = [game(heap + 1, step + 1, moves),
              game(heap * 5, step + 1, moves)]
    return any(result)


def game1(heap, step, moves):
    if heap > 200:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    result = [game1(heap + 1, step + 1, moves),
              game1(heap * 5, step + 1, moves)]
    return any(result) if (moves + 1) % 2 == step % 2 else all(result)


print(f'19: {min(s for s in range(1, 201) if not game(s, 0, 1) and game(s, 0, 2))}')
print(f'20: {[s for s in range(1, 201) if not game1(s, 0, 1) and game1(s, 0, 3)]}')
print(f'21: {min(s for s in range(1, 201) if (game1(s, 0, 2) or game1(s, 0, 4)) and not game1(s, 0, 2))}')