a = [0, 3, 5, 7, 10, 20, 24, 30, 45, 56, 64]
x = 7
i = 0
j = len(a) - 1
m = int(j / 2)
while a[m] != x and i < j:
    if x > a[m]:
        i = m + 1
    else:
        j = m - 1
    m = int((i + j) / 2)

if i > j:
    print('Элемент не найден')
else:
    print('Индекс элемента: ', m)