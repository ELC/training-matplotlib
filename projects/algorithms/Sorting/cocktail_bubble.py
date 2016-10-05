def main(iterable):
    d = 0
    l = len(iterable) - 1
    while d * 2 < l:
        a = range(d, l - d)
        bare = range(l - d, d, -1)
        for i, j in zip(a, bare):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = \
                    iterable[i + 1], iterable[i]
            if iterable[j] < iterable[j - 1]:
                iterable[j], iterable[j - 1] = \
                    iterable[j - 1], iterable[j]
        d += 1
    return iterable