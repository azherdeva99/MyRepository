abcEng = 'abcdefghijklmnopqrstuvwxyz'
abcRu = 'абвгдеёжзийклмнопрстуфхцчшщъьыэюя'
text = input('Input text: ').lower()
k = int(input('Enter the shift number: '))
new = ''

for c in text:
    if c in abcEng:
        new += abcEng[(abcEng.index(c) + k) % (len(abcEng))]
for c in text:
    if c in abcRu:
        new += abcRu[(abcRu.index(c) + k) % (len(abcRu))]

print('Ciphertext: ', new)


