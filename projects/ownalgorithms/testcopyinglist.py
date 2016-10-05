def semievenprimes():
    n = 2
    while True:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            yield n
        n += 1

def main():
    cosa = semievenprimes()
    primes = []
    for i in range(100):
        nextnumber = next(cosa)
        primes.append(nextnumber)
    print(primes)