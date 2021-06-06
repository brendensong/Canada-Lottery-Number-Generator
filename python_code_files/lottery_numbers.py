import random

a = random.randint(1, 49)
b = random.randint(1, 49)
c = random.randint(1, 49)
d = random.randint(1, 49)
e = random.randint(1, 49)
f = random.randint(1, 49)

#int_number = [a, b, c, d, e, f]
#print(sorted(int_number))

while b == a:
    b = random.randint(1, 49)

while c == a or c == b:
    c = random. randint(1, 49)
    
while d == a or d == b or d == c:
    d = random. randint(1, 49)

while e == a or e == b or e == c or e == d:
    e = random. randint(1, 49)

while f == a or f == b or f == c or f == d or f == e:
    f = random. randint(1, 49)

print(sorted([a, b, c, d, e, f]))


