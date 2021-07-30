import itertools
for el in itertools.count(3):
    if el == 10:
        break
    print(el)
c = 0
for el in itertools.cycle('ABC'):
    if c > 5:
        break
    print(el, end=' ')
    c += 1