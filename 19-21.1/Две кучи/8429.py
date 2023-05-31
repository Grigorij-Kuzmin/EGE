def game(heep1, heep2, moves, to):
    if heep1 >= 40 or heep2 >= 40:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    if heep1 > heep2:
        result = [game(heep1 + 1, heep2, moves + 1, to),
                  game(heep1 + 2, heep2, moves + 1, to),
                  game(heep1 + 3, heep2, moves + 1, to),
                  game(heep1, heep2 * 2, moves + 1, to)]
    if heep1 < heep2:
        result = [game(heep1, heep2 + 1, moves + 1, to),
                  game(heep1, heep2 + 2, moves + 1, to),
                  game(heep1, heep2 + 3, moves + 1, to),
                  game(heep1 * 2, heep2, moves + 1, to)]
    if heep1 == heep2:
        result = [game(heep1 + 1, heep2, moves + 1, to),
                  game(heep1 + 2, heep2, moves + 1, to),
                  game(heep1 + 3, heep2, moves + 1, to),
                  game(heep1, heep2 + 1, moves + 1, to),
                  game(heep1, heep2 + 2, moves + 1, to),
                  game(heep1, heep2 + 3, moves + 1, to)]
    return any(result) if (moves + 1) % 2 == to % 2 else all(result)


def game1(heep1, heep2, moves, to):
    if heep1 >= 40 or heep2 >= 40:
        return moves % 2 == to % 2
    if moves == to:
        return 0
    if heep1 > heep2:
        result = [game1(heep1 + 1, heep2, moves + 1, to),
                  game1(heep1 + 2, heep2, moves + 1, to),
                  game1(heep1 + 3, heep2, moves + 1, to),
                  game1(heep1, heep2 * 2, moves + 1, to)]
    if heep1 < heep2:
        result = [game1(heep1, heep2 + 1, moves + 1, to),
                  game1(heep1, heep2 + 2, moves + 1, to),
                  game1(heep1, heep2 + 3, moves + 1, to),
                  game1(heep1 * 2, heep2, moves + 1, to)]
    if heep1 == heep2:
        result = [game1(heep1 + 1, heep2, moves + 1, to),
                  game1(heep1 + 2, heep2, moves + 1, to),
                  game1(heep1 + 3, heep2, moves + 1, to),
                  game1(heep1, heep2 + 1, moves + 1, to),
                  game1(heep1, heep2 + 2, moves + 1, to),
                  game1(heep1, heep2 + 3, moves + 1, to)]
    return any(result)

m = 100
for i in range(1, 40):
    for j in range(1, 40):
        if game1(i, j, 0, 1):
            m = min(m, i + j)
print('19:', m)
print('20:', [s for s in range(1, 40) if not game(11, s, 0, 1) and game(11, s, 0, 3)])
print('21:', [s for s in range(1, 40) if game(31, s, 0, 4)])