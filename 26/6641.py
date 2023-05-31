f = open('6641.txt')
n, m = map(int, f.readline().split())

products = []
w_products = []
s_count = 0

for i in range(n):
    a, b = f.readline().split()
    products.append([int(a), b])

products.sort()

i = 0
while m >= products[i][0] and i < n:
    m -= products[i][0]
    if products[i][1] == 'S':
        s_count += 1
    if products[i][1] == 'W':
        w_products.append(products[i][0])
    i += 1

k = -1
while (w_products[k] + m) >= products[i][0] and i < n:
    if products[i][1] == 'S':
        m -= products[i][0] - w_products[k]
        k -= 1
        s_count += 1
    i += 1

print(s_count, m)