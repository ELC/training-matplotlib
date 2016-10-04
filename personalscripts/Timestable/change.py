import random

import personal_scripts.Timestable.conf

random.seed()


def init():
    x = 0
    y = func(x)
    conf.init(x, y)
    return conf.data[0]

def func(a):
    return int(a+a**0.5+a**(1/3))

def stuff():
    a = conf.data[-1][0] + 1
    conf.data.append((a, func(a)))
    return conf.data
