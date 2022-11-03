import unicodedata

s = 'Röd'
print('\nRed String:', s)
print('Type:', type(s), '\tLength:', len(s))

s = s.encode('utf-8')
print('\nEncoded string:', s)
print('Type:', type(s), '\tLength:', len(s))

s = s.decode('utf-8')
print('\nDecoded string', s)
print('Type', type(s), '\tLength:', len(s))
print()

for i in range(len(s)):
    print(s[i], unicodedata.name(s[i]), sep=':')
