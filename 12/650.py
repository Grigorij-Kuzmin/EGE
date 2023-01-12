line = '>' + '1' * 25 + '2' * 17 + '3' * 10
while '>1' in line or '>2' in line or '>3' in line:
    if '>1' in line:
        line = line.replace('>1', '22>3')
    if '>2' in line:
        line = line.replace('>2', '2>')
    if '>3' in line:
        line = line.replace('>3', '11>2')
print(line.count('1') + line.count('2') * 2 + line.count('3') * 3)