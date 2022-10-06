line = '>' + '1' * 26 + '2' * 10 + '3' * 14
while '>1' in line or '>2' in line or '>3' in line:
    line = line.replace('>1', '22>')
    line = line.replace('>2', '2>')
    line = line.replace('>3', '1>')
print(line.count('1') + line.count('2') * 2)