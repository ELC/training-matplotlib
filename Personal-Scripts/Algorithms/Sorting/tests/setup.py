from random import shuffle, choice

n = 500
a = [i for i in range(n)]
length = 5
c = [a[:] for _ in range(length)]
for i in range(len(c)):
    shuffle(c[i])
b = [choice(c) for _ in range(length)]


def per():
    return b[:]
