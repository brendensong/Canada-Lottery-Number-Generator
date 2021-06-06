import random

a = random.randint(1, 49)

while True:
    b = random.randint(1, 49)
    if a != b:
        break

while True:
    c = random.randint(1, 49)
    if a != c and b != c:
        break

while True:
    d = random.randint(1, 49)
    if a != d and b != d and c != d:
        break

while True:
    e = random.randint(1, 49)
    if a != e and b != e and c != e and d != e:
        break

while True:
    f = random.randint(1, 49)
    if a != f and b != f and c != f and d != f and e != f:
        break

lottery = sorted([a, b, c, d, e, f])

for num in lottery:
    print(num, end=' ')
