strings = []

while True:
    usin = input()
    if usin == 'END':
        break
    strings.append(usin)

for string in strings:
    print(''.join(reversed(string)))
