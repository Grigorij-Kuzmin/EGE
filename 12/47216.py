def f(str):
    while '>1' in str or '>2' in str or '>0' in str:
        if '>1' in str:
            str = str.replace('>1', '22>')
        if '>2' in str:
            str = str.replace('>2', '2>')
        if '>0' in str:
            str = str.replace('>0', '1>')
    return str

def simple(x):
    y = 2
    while y * y <= x:
        if x % y == 0:
            return False
        y += 1
    return True

for n in range(39):
    str = '>' + 39 * '0' + n * '1' + 39 * '2'
    str1 = f(str)
    x = str1.count('1') + 2 * str1.count('2')
    if simple(x):
        print(n)

