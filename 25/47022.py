for i in range(300000001, 400010000):
    count = 0
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            count += 1
            if count == 5:
                print(i // j)


