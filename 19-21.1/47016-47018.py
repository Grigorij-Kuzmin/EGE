def game(heap, step, op):
    if step == 4 and heap >= 29:
        return 1
    elif step == 4 and heap < 29:
        return 0
    elif heap >= 29 and step < 4:
        return 0
    else:
        if step % 2 != 0:
            if step == 1:
                return game(heap + 1, step + 1, 1) or game(heap + 2, step + 1, 2) or game(heap * 2, step + 1, 3)
            elif step == 3:
                if op == 1:
                    return game(heap + 2, step + 1, op) or game(heap * 2, step + 1, op)
                elif op == 2:
                    return game(heap + 1, step + 1, op) or game(heap * 2, step + 1, op)
                elif op == 3:
                    return game(heap + 1, step + 1, op) or game(heap + 2, step + 1, op)
        else:
            return game(heap + 1, step + 1, op) and game(heap + 2, step + 1, op) and game(heap * 2, step + 1, op)


print(f'19: {min(s for s in range(1, 29) if game(s, 1, 0))}')
