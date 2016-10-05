def main(iterable):
    l = len(iterable)
    for i in range(0, l - 1):
        for j in range(0, l):
            if iterable[i] > iterable[j] and j > i:
                iterable[i], iterable[j] = iterable[j], iterable[i]
    return iterable