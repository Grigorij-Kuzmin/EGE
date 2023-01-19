def game(heep, step, moves):
    if heep > 164:
        return moves % 2 == step % 2
    if moves == step:
        return 0
    result = [game(heep + 1, step + 1, moves),
              game(heep * 2, step + 1, moves),
              game(heep + 4, step + 1, moves)]
    return any(result) if (moves + 1) % 2 == step % 2 else all(result)

print(f'19: {[s for s in range(1, 164) if not game(s, 0, 1) and game(s, 0, 2)]}')
print(f'20: {[s for s in range(1, 164) if not game(s, 0, 1) and game(s, 0, 3)]}')
print(f'21: {[s for s in range(1, 164) if not game(s, 0, 2) and game(s, 0, 4)]}')