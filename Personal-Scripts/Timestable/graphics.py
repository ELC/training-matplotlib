import change
import matplotlib.animation as animation
import matplotlib.pyplot as plt
from matplotlib import style

a = change.init()
xs = [a[0]]
ys = [a[1]]
last = ys[0]


def animate():
    a = change.stuff()[-1]
    xs.append(a[0])
    ys.append(a[1])
    ax1.clear()
    ax1.plot(xs, ys)

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()
