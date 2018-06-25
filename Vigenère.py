abcEng = 'abcdefghijklmnopqrstuvwxyz'
abcRu = 'абвгдеёжзийклмнопрстуфхцчшщъьыэюя'
text = input('Input text: ').lower()
k = input('Enter key word: ')
new = ''
d=[]

for c in text:
    if c in abcEng:
        d.append(abcEng[(abcEng.index(c) + len(k)) % (len(abcEng))])
    elif c in abcRu:
        d.append(abcRu[(abcRu.index(c) + len(k)) % (len(abcRu))])
    elif c not in abcRu or abcEng:
        d.append(c)
for c in range(len(d)):
    new += d[c]
print('The encrypted word: ', new)
