def main(iterable):
    first = 0
    last = len(iterable) - 1
    while first < last:
        minimo = iterable[first]
        maximo = iterable[last]
        for i in range(first, last + 1):
            if iterable[i] > maximo:
                maximo = iterable[i]
            if iterable[i] < minimo:
                minimo = iterable[i]
        minindex = iterable.index(minimo)
        iterable[first], iterable[minindex] = \
            iterable[minindex], iterable[first]
        maxindex = iterable.index(maximo)
        iterable[last], iterable[maxindex] = \
            iterable[maxindex], iterable[last]
        first += 1
        last -= 1
    return iterable