variety = [50, 10, 5, 1]
summa = int(input('Enter the amount: '))
tot = 0
number = [0, 0, 0, 0]


def delivery(summa, tot):
    while summa > 0:
        if summa >= 50:
            summa -= 50
            tot += 1
        elif 50 > summa >= 10:
            summa -= 10
            tot += 1
        elif 10 > summa >= 5:
            summa -= 5
            tot += 1
        elif 5 > summa >= 1:
            summa -= 1
            tot += 1
    print('Quantity of coins: ', tot)
delivery(summa, tot)

for i in range(len(variety)):
    while int(summa) >= variety[i]:
        summa -= variety[i]
        number[i] += 1
    print(variety[i], ' coins', '-', number[i], ' piece(s)')


