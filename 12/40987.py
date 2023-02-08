for x in range(200, 300):
        line = x * '1'
        while '1111' in line:
                line = line.replace('1111', '22', 1)
                line = line.replace('222', '1', 1)
                if line.count('1') == 0:
                        print(x)