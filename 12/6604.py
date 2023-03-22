s = 0
count = 0
import itertools
for m in range(1, 100):
    strings = itertools.product('123', repeat=m)
    for str in strings:
        if str.count('1') == 15 and str.count('2') == 35 and str.count('3') == m:
            str = '>' + ''.join(str)
        while '>1' in str or '>2' in str or '>3' in str:
            if '>1' in str:
                str = str.replace('>1', '2>', 1)
            if '>2' in str:
                str = str.replace('>2', '3>', 1)
            if '>3' in str:
                str = str.replace('>3', '11>', 1)
        for i in range(len(str) - 1):
            s += int(str[i])
        for i in range(2, s):
            if s % i == 0:
                count += 1
        if count != 3:
            count = 0
        else:
            print(m)
            break