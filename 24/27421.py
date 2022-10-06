with open('27421.txt') as f:
    line = f.readline()
    # 1 потому что при сравнении соседних символов в конце
    # один символ не учитывается
    # ПРИВЕТ ГРИША
    count = 1
    m = 0
    for i in range(len(line) - 1):
        if line[i] != line[i + 1]:
            count += 1
        else:
            m = max(m, count)
            count = 1
print(m)