lst = list(map(int, input().split()))
# lst=[15, 39, 71]
table = list(range(10))
table.extend(['A', 'B', 'C', 0])
print('#', end='')
for i in range(3):
    quotient = lst[i]//13
    remainder = lst[i] % 13
    print('{0}{1}'.format(table[quotient], table[remainder]), end='')
