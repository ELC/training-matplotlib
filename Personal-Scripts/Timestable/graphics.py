import change
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

A = change.init()
XS = [a[0]]
YS = [a[1]]
LAST = ys[0]


def animate():
    a = change.stuff()[-1]
    xs.append(a[0])
    ys.append(a[1])
    ax1.clear()
    ax1.plot(xs, ys)

style.use('fivethirtyeight')
FIG = plt.figure()
AX1 = fig.add_subplot(1, 1, 1)
ANI = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
