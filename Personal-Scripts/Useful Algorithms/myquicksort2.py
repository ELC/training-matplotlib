import random
from time import time as pc


def myquicksort2(iterable, first=1, last=-10):
    length = len(iterable)
    if length < 2:
        return iterable
    if last == -10:
        last = length - 1
    pivote = iterable[0]  # Selecci
    while True:
        while first <= last and iterable[first] < pivote:
            first += 1
        while first <= last and iterable[last] > pivote:
            last -= 1
        if first >= last:
            break
        else:
            iterable[first], iterable[last] = iterable[last], iterable[first]
    iterable[0], iterable[last] = iterable[last], iterable[0]
    a = iterable[last + 1:]
    indexmin = iterable.index(a[0])
    indexmax = iterable.index(a[-1])
    myquicksort(iterable)
    a = iterable[:last]
    indexmin = iterable.index(a[0])
    indexmax = iterable.index(a[-1])
    myquicksort(iterable[:last])


def myquicksort(iterable):
    inicial(iterable, 0, len(iterable))
    return iterable


def inicial(iterable, first, last):
    lenght = last - first
    if lenght < 2:
        return iterable
    f = first
    last -= 1
    pivote = (iterable[last] + iterable[first]) // 2
    while True:
        while first <= last and iterable[first] < pivote:
            first += 1
        while first <= last and iterable[last] > pivote:
            last -= 1
        if first >= last:
            break
        else:
            iterable[first], iterable[last] = iterable[last], iterable[first]
    last += 1
    if last != f:
        a = iterable[last:]
        if not len(a) < 2:
            indexmin = iterable.index(a[0])
            inicial(iterable, indexmin, len(iterable))
    if last != f:
        a = iterable[f:last - 1]
        if not len(a) < 2:
            indexmax = iterable.index(a[-1])
            inicial(iterable, f, indexmax + 1)
    # iterable[last + 1:] = myquicksort(iterable[last + 1:])
    # iterable[:last] = myquicksort(iterable[:last])
    return iterable


def iniciar(iterable):
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


def myquicksortmejorado(alist):
    quicksorthelper(alist, 0, len(alist) - 1)
    return alist


def quicksorthelper(alist, first, last):
    if first < last:
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
            if iterable[i] > iterable[j]:
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


def bubblealternativo(iterable):
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
        iterable[first], iterable[minindex] = iterable[minindex], iterable[
            first]
        maxindex = iterable.index(maximo)
        iterable[last], iterable[maxindex] = iterable[maxindex], iterable[last]
        first += 1
        last -= 1
    return iterable


def cocktail(iterable):
    d = 0
    l = len(iterable) - 1
    while d * 2 < l:
        for i in range(d, l - d):
            if iterable[i] > iterable[i + 1]:
                iterable[i], iterable[i + 1] = iterable[i + 1], iterable[i]
        for i in range(l - d, d, -1):
            if iterable[i] < iterable[i - 1]:
                iterable[i], iterable[i - 1] = iterable[i - 1], iterable[i]
        d += 1
    return iterable


def test(n, iterable):
    if n == "Quicksort:             ":
        myquicksort(iterable)
    elif n == "Cocktail               ":
        cocktail(iterable)
    elif n == "Bubblesfalsefromi:     ":
        bubblesfalsefromi(iterable)
    elif n == "Bubblesortfalsefrom0:  ":
        bubblesortfalsefrom0(iterable)
    elif n == "Bubbleoriginal:        ":
        bubbleoriginal(iterable)
    elif n == "Bubblealternativo:     ":
        bubblealternativo(iterable)
    elif n == "Python                 ":
        sorted(iterable)


def mostrar(n=100, v=False):
    index2 = "\nCONJUNTO ORDENADO ALETORIAMENTE              %   s/ " \
             "\nCONJUNTO ORDENADO INVERSAMENTE               %   s/ " \
             "\nCONJUNTO ORDENADO                            %   s/ ".split(
        "/")
    index = "Quicksort:             /" \
            "Bubblesfalsefromi:     /" \
            "Bubblesortfalsefrom0:  /" \
            "Bubbleoriginal:        /" \
            "Bubblealternativo:     /" \
            "Python                 /" \
            "Cocktail               ".split("/")
    index3 = [[i for i in range(n)] for _ in range(3)]
    random.shuffle(index3[0])
    index3[1].reverse()
    rap, slo = [], []
    for j in range(len(index2) - 1):
        if v:
            print("{}".format(index2[j]))
        time = []
        for i in index:
            b = index3[j]
            start = pc()
            test(i, b)
            time.append(pc() - start)
        for i in index:
            if v:
                print("Tiempo de demora del {}".format(i),
                      time[index.index(i)])
        rap.append(index[time.index(min(time))])
        slo.append(index[time.index(max(time))])
        if v:
            print("El más rápido fue: ", rap[j])
    print("\nEl top 3 es : \n {0[0]}\n {0[1]}\n {0[2]}".format(rap))
    print(
        "\nLos 3 más lentos fueron : \n {0[0]}\n {0[1]}\n {0[2]}".format(slo))

# mostrar(100, True)
