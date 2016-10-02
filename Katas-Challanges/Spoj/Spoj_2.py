import timeit


def isprime(a, s):
    b = 2
    g = a ** 0.5
    while b <= g:
        if a != b and a % b == 0:
            return False
        b += 1
    return True

for i in range(int(1)):
    p = "1 31622".split()
    h = []
    start_time = timeit.default_timer()
    for j in range(int(p[0])+1, int(p[1])-1):
        if isprime(j, len(str(j))):
            h.append(j)
    print(len(h), "-----", h)
    print(timeit.default_timer() - start_time)
