def main(iterable):
    first = 0
    last = len(iterable) - 1
    while first < last:
        minimo = iterable[first]
        for i in range(first, last + 1):
            if iterable[i] < minimo:
                minimo = iterable[i]
        minindex = iterable.index(minimo)
        iterable[first], iterable[minindex] = \
            iterable[minindex], iterable[first]
        first += 1
    return iterable