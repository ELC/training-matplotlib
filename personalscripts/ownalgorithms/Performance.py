from time import time


def helper(func, *arg):
    start = time()
    func(*arg)
    total = round(time()-start, 5)*100
    return total


def testPerformance(arg, *funcs):
    """
    First parameter is a tuple with all the arguments for each function
    Each function should take the same amount of parameters in the
    same order
    The output is a dict with function:timeFromMinimum pair
    """
    times = []
    for func in funcs:
        times.append(helper(func, *arg))
    minimum = min(times)
    sustractivetimes = [i - minimum for i in times]
    result = {i: j for i, j in zip(funcs, sustractivetimes)}
    return result
