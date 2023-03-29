def game(heep, step, moves):
    if heep <= 12:
        return step % 2 == moves % 2
    if step == moves:
        return 0
    result = [game(heep // 3, step + 1, moves),
              game(heep - 12, step + 1, moves)]
    return any(result)


def game1(heep, step, moves):
    if heep <= 12:
        return step % 2 == moves % 2
    if step == moves:
        return 0
    result = [game1(heep // 3, step + 1, moves),
              game1(heep - 12, step + 1, moves)]
    return any(result) if (step + 1) % 2 == moves % 2 else all(result)


print(max(s for s in range(13, 10000) if not game(s, 0, 1) and game(s, 0, 2)))
print(max(s for s in range(13, 10000) if not game1(s, 0, 1) and game1(s, 0, 3)))
print(min(s for s in range(13, 10000) if not game1(s, 0, 1) and game1(s, 0, 3)))
print([s for s in range(13, 10000) if not game1(s, 0, 2) and (game1(s, 0, 2) or game1(s, 0, 4))])