def main(iterable):
    done = False
    while not done:
        done = True
        for i in range(len(iterable) - 1):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
                done = False
    return iterable