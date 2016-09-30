def myquicksortslice(iterable):
    first = 0
    last = len(iterable) - 1
    pivote = (iterable[last] + iterable[first]) // 2
    while True:
        while first <= last and iterable[first] < pivote:
            first += 1
        while first <= last and iterable[last] > pivote:
            last -= 1
        if first >= last:
            break
        else:
            iterable[first], iterable[last] = \
                iterable[last], iterable[first]
    if len(iterable) - last > 2:
        iterable[last + 1:] = myquicksortslice(iterable[last + 1:])
    elif len(iterable) - last == 2 and iterable[0] > iterable[1]:
        iterable[0], iterable[1] = \
            iterable[1], iterable[0]
    if last > 2:
        iterable[:last] = myquicksortslice(iterable[:last])
    elif last == 2 and iterable[0] > iterable[1]:
        iterable[0], iterable[1] = \
            iterable[1], iterable[0]
    return iterable


def myquicksortmejorado(iterable):
    myquicksorthelper(iterable, 0, len(iterable) - 1)
    return iterable


def myquicksorthelper(iterable, first, last):
    if first < last:
        pivoteindex = sorthelper(iterable, first, last)
        myquicksorthelper(iterable, first, pivoteindex - 1)
        myquicksorthelper(iterable, pivoteindex + 1, last)


def sorthelper(iterable, f, last):
    pivote = (iterable[last] + iterable[f]) // 2
    first = f
    while True:
        while first <= last and iterable[first] < pivote:
            first += 1
        while first <= last and iterable[last] > pivote:
            last -= 1
        if first >= last:
            break
        else:
            iterable[first], iterable[last] = iterable[last], iterable[first]
    return last


def myquicksortinternet(alist):
    quicksorthelper(alist, 0, len(alist) - 1)
    return alist


def quicksorthelper(alist, first, last):
    if first <= last:
        splitpoint = partition(alist, first, last)
        quicksorthelper(alist, first, splitpoint - 1)
        quicksorthelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark


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
        b = range(l - d, d, -1)
        for i, j in zip(a, b):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = \
                    iterable[i + 1], iterable[i]
            if iterable[j] < iterable[j - 1]:
                iterable[j], iterable[j - 1] = \
                    iterable[j - 1], iterable[j]
        d += 1
    return iterable


def gnome(iterable):
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


def main():
    return 0


if __name__ == '__main__':
    status = main()
