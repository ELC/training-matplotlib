def main(iterable):
    done = False
    while not done:
        done = True
        for i in range(len(iterable) - 1):
            if not iterable[i] < iterable[i + 1]:
                done = False
                j = i
                while not (iterable[j] < iterable[j + 1]) and j >= 0:
                    iterable[j], iterable[j + 1] = \
                        iterable[j + 1], iterable[j]
                    j -= 1
    return iterable