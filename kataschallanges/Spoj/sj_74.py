def tes(l, t, k):
    e = 1
    y = t
    t = l ** 0.5
    c = int(t)
    if l % t == 0:
        e -= c
    while y <= c:
        if l % y == 0:
            e += y + (l // y)
        y += k
    return e


def divider(a):
    if a % 2 == 0:
        return tes(a, 2, 1)
    else:
        return tes(a, 3, 2)

def main():
    for i in range(int(input())):
        print(divider(int(input())))