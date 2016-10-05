def bubblesfalsefromi(iterable):
    l = len(iterable)
    for i in range(0, l - 1):
        for j in range(i, l):
            if iterable[i] > iterable[j]:
                iterable[i], iterable[j] = iterable[j], iterable[i]
    return iterable


def bubblesortfalsefrom0(iterable):
    l = len(iterable)
    for i in range(0, l - 1):
        for j in range(0, l):
            if iterable[i] > iterable[j] and j > i:
                iterable[i], iterable[j] = iterable[j], iterable[i]
    return iterable


def bubbleoriginal(iterable):
    done = False
    while not done:
        done = True
        for i in range(len(iterable) - 1):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
                done = False
    return iterable


def selection(iterable):
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


def cocktailselection(iterable):
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


def cocktailbubble(iterable):
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


def insertion(iterable):
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